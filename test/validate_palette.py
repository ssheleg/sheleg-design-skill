#!/usr/bin/env python3
"""Palette validator for the sheleg-design-skill token layers (stdlib only).

The repo already checks that a pack is *structurally* whole. Nothing checked the
colours themselves, so a pack could ship a status green and a status red that a
red-green colourblind reader cannot tell apart, and every gate would stay green.

Colour separation is computable, so it is computed here rather than eyeballed:

  1. Every colour token parses. A token the parser cannot read is a FAIL, never
     a silent skip -- a check that skips is not a check.
  2. Primary ink on the primary field meets WCAG AA (4.5:1), and the measured
     ratio is printed so a pack can be held to what it claims.
  3. Semantic status colours stay distinguishable from each other and from the
     accent -- under normal vision AND under the three dichromacies. Green-vs-red
     is the classic failure and the one nobody catches by looking.
  4. A palette landing in a known AI-default cluster must prove provenance: an
     addressable Origin in the pack. The cluster is not forbidden -- atrium is a
     cream field with a terracotta accent because functionhealth.com is -- but a
     pack that lands there *and* cannot say where it read it is inventing.

Thresholds follow the OKLab convention: distance x100. Adjacent semantic colours
need >= 15 under normal vision and >= 8 under each simulated dichromacy.

Exit 0 with "OK (<n> checks)" when clean; 1 with FAIL: lines otherwise.
"""

from __future__ import annotations

import math
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOKENS = ROOT / "plugins/sheleg-design/skills/sheleg-design/styles/tokens"
PACKS = ROOT / "plugins/sheleg-design/skills/sheleg-design/styles"

# Packs name their field and ink differently -- bg / base / paper. Resolution is
# an explicit ordered list rather than a guess, so adding a pack that uses a new
# word fails loudly here instead of quietly checking nothing.
FIELD_TOKENS = ("bg", "base", "paper", "canvas", "surface")
INK_TOKENS = ("ink", "fg", "text", "foreground")

# Solid semantic colours worth separating. Suffixed variants (-soft, -weak,
# -tint, -dim) are backgrounds or de-emphasised fills, not peers.
STATUS_TOKENS = ("good", "ok", "success", "warn", "warning", "danger", "error", "red", "info")
VARIANT_SUFFIXES = ("-soft", "-weak", "-tint", "-dim", "-deep", "-bright", "-light", "-on-dark")

DELTA_NORMAL = 15.0
DELTA_CVD = 8.0
# Below this, no icon and no label rescue the pair: two semantic states rendered
# in one colour is a palette error, not a labelling one. Secondary encoding buys
# separation for readers who cannot distinguish two *different* colours -- it
# cannot buy meaning for two colours that are the same.
DELTA_HARD = 10.0

# Machado et al. (2009), severity 1.0, applied in linear sRGB.
CVD_MATRICES = {
    "protanopia": (
        (0.152286, 1.052583, -0.204868),
        (0.114503, 0.786281, 0.099216),
        (-0.003882, -0.048116, 1.051998),
    ),
    "deuteranopia": (
        (0.367322, 0.860646, -0.227968),
        (0.280085, 0.672501, 0.047413),
        (-0.011820, 0.042940, 0.968881),
    ),
    "tritanopia": (
        (1.255528, -0.076749, -0.178779),
        (-0.078411, 0.930809, 0.147602),
        (0.004733, 0.691367, 0.303900),
    ),
}

# The clusters an unguided model reaches for regardless of subject. Landing here
# is allowed; landing here without an addressable reference is not.
AI_DEFAULT_CLUSTERS = (
    ("warm cream field with a high-contrast serif and a terracotta accent",
     (0.95, 0.02, 85.0), (0.60, 0.12, 45.0)),
    ("near-black field with a single acid-green or vermilion accent",
     (0.15, 0.02, 260.0), (0.75, 0.22, 140.0)),
)

failures: list[str] = []
notes: list[str] = []
checks = 0


def check(ok, msg):
    global checks
    checks += 1
    if not ok:
        failures.append(msg)
    return ok


# --- colour parsing -------------------------------------------------------

DECL = re.compile(r"^\s*(--[a-z0-9-]+)\s*:\s*([^;]+);", re.I | re.M)
VAR_REF = re.compile(r"var\(\s*(--[a-z0-9-]+)\s*(?:,[^)]*)?\)", re.I)
HEX = re.compile(r"^#([0-9a-f]{3,8})$", re.I)
RGB = re.compile(r"^rgba?\(([^)]*)\)$", re.I)
OKLCH = re.compile(
    r"^oklch\(\s*([0-9.]+%?)\s+([0-9.]+)\s+([0-9.]+)(?:\s*/\s*([0-9.]+%?))?\s*\)$", re.I
)


BLOCK = re.compile(r"([^{}/]+?)\{([^{}]*)\}", re.S)

# Anything that claims to be a colour. A value we cannot compute is a FAIL with a
# clear ask, not a skip: an unverified colour must not ship behind a green gate.
#
# Two of these used to be uncomputable and are not any more. `color-mix()` in
# srgb / srgb-linear / oklab / oklch, and relative colour `rgb(from …)`, are
# computed below, which is what lifted their ban from the pack skeleton: a token
# layer had been forced to hand-write `rgba(38, 109, 240, 0.35)` where the
# derivation is `rgb(from var(--accent) r g b / .35)`, and a hand-derived literal
# stops tracking the token it was derived from the moment either one moves.
# Everything else in this pattern is still refused, on purpose.
COLOR_SHAPED = re.compile(
    r"^(#|rgba?\(|hsla?\(|oklch\(|oklab\(|lab\(|lch\(|color\(|color-mix\(|"
    r"(?:white|black|red|green|blue|transparent|currentcolor)\b)", re.I
)

# color-mix(in <space>, <colour> <pct>?, <colour> <pct>?)
COLOR_MIX = re.compile(r"^color-mix\(\s*in\s+([a-z-]+)\s*,\s*(.+)\)$", re.I | re.S)
MIX_SPACES = ("srgb", "srgb-linear", "oklab", "oklch")
TRAILING_PCT = re.compile(r"^(.*?)\s+([0-9.]+)%$", re.S)
# Relative colour. Only the rgb() form is computed, because it is the one the
# library needs (an alpha variant of an existing token) and the one whose channel
# grammar stays small enough to be checkable. oklch(from …) and any calc() inside
# a channel are refused rather than guessed at.
RELATIVE = re.compile(r"^rgb\(\s*from\s+(.+)\)$", re.I | re.S)
# A var() anywhere inside a value, not only as the whole value.
VAR_INLINE = re.compile(r"var\(\s*(--[a-z0-9-]+)\s*(?:,\s*([^;]*?))?\)", re.I)


def declarations(text: str) -> dict[str, str]:
    return {m.group(1): m.group(2).strip() for m in DECL.finditer(text)}


def themes(text: str) -> list[tuple[str, dict[str, str]]]:
    """Every colour theme in the file, as (label, fully-resolved declarations).

    A token layer is not one flat namespace. workbench declares a light :root
    and then a dark [data-theme] override, and a naive parse that folds them
    into one dict silently validates whichever came last -- which is how the
    light half of four packs went unchecked until a planted defect refused to
    fail. Each override is validated as base + override, under its own label.
    """
    blocks = []
    for m in BLOCK.finditer(text):
        selector = " ".join(m.group(1).split())
        decls = declarations(m.group(2) + ";")
        if decls:
            blocks.append((selector, decls))
    if not blocks:
        return []
    base_label, base = blocks[0]
    out = [(base_label, dict(base))]
    for label, decls in blocks[1:]:
        # A block that overrides no colour (a reduced-motion duration reset, say)
        # is not a theme; validating it again would just double the count.
        #
        # The test asks COLOR_SHAPED rather than listing prefixes, because the
        # hand-written list was `#` or `oklch(` — so a dark theme written in
        # `color-mix()` or in relative colour would have been read as "overrides no
        # colour" and skipped entirely. Teaching the parser two new forms without
        # widening this test would have opened a blind spot in the same commit that
        # closed a limitation: the exact shape of defect this docstring is about.
        if not any(COLOR_SHAPED.match(v.strip()) for v in decls.values()):
            continue
        merged = dict(base)
        merged.update(decls)
        out.append((label, merged))
    return out


def resolve(name: str, decls: dict[str, str], seen=None) -> str | None:
    """Follow var() references to a literal value; None on a cycle or a miss."""
    seen = seen or set()
    if name in seen or name not in decls:
        return None
    seen.add(name)
    value = decls[name]
    ref = VAR_REF.fullmatch(value.strip())
    if ref:
        return resolve(ref.group(1), decls, seen)
    # A reference can also sit *inside* the value — `rgb(from var(--accent) …)`.
    return substitute_vars(value, decls)


def srgb_to_linear(c: float) -> float:
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def substitute_vars(value: str, decls: dict[str, str], depth: int = 0) -> str:
    """Replace var() references *inside* a value, not only whole-value ones.

    `resolve()` follows a var() that is the entire value, which was enough while
    every colour in the library was a literal. A colour derived from another token
    carries its reference inside a function — `rgb(from var(--accent) r g b / .35)`
    — and without this the parser reads the word `var` and refuses the value, which
    is what made hand-written rgba the only option. Depth-bounded, because a cycle
    here is a stack overflow rather than a finding.
    """
    if depth > 8:
        return value

    def one(m):
        name, fallback = m.group(1), m.group(2)
        if name in decls:
            return substitute_vars(decls[name].strip(), decls, depth + 1)
        return fallback.strip() if fallback else m.group(0)

    return VAR_INLINE.sub(one, value)


def split_top_level(s: str, sep: str = ",") -> list[str]:
    """Split on `sep` at paren depth zero, so nested functions survive."""
    parts, depth, cur = [], 0, []
    for ch in s:
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
        if ch == sep and depth == 0:
            parts.append("".join(cur))
            cur = []
        else:
            cur.append(ch)
    parts.append("".join(cur))
    return [p.strip() for p in parts]


def _to_gamma(c: float) -> float:
    c = max(0.0, min(1.0, c))
    return 12.92 * c if c <= 0.0031308 else 1.055 * (c ** (1 / 2.4)) - 0.055


def parse_color_mix(value: str):
    """color-mix(in srgb | srgb-linear | oklab | oklch, A p%?, B q%?).

    Interpolation is premultiplied by alpha, as the spec requires, and the polar
    space takes the shorter hue arc — the default. A space this does not implement
    returns None and fails loudly rather than being approximated in the wrong one:
    mixing in srgb and mixing in oklab give visibly different midpoints, and a gate
    that guessed would certify a colour nobody rendered.
    """
    m = COLOR_MIX.match(value)
    if not m:
        return None
    space = m.group(1).lower()
    if space not in MIX_SPACES:
        return None
    parts = split_top_level(m.group(2))
    if len(parts) != 2:
        return None

    colours, weights = [], []
    for part in parts:
        pct = TRAILING_PCT.match(part)
        if pct:
            part, w = pct.group(1).strip(), float(pct.group(2))
        else:
            w = None
        parsed = parse_color(part)
        if parsed is None:
            return None
        colours.append(parsed)
        weights.append(w)

    if weights[0] is None and weights[1] is None:
        weights = [50.0, 50.0]
    elif weights[0] is None:
        weights[0] = max(0.0, 100.0 - weights[1])
    elif weights[1] is None:
        weights[1] = max(0.0, 100.0 - weights[0])
    total = weights[0] + weights[1]
    if total <= 0:
        return None
    # Below 100% the result is not fully opaque; above it, the pair is normalised.
    alpha_multiplier = min(1.0, total / 100.0)
    w0, w1 = weights[0] / total, weights[1] / total

    (rgb0, a0), (rgb1, a1) = colours
    alpha = a0 * w0 + a1 * w1
    # Premultiply, mix, un-premultiply.
    p0 = [c * a0 for c in rgb0]
    p1 = [c * a1 for c in rgb1]

    if space == "srgb-linear":
        mixed = [p0[i] * w0 + p1[i] * w1 for i in range(3)]
    elif space == "srgb":
        g0 = [_to_gamma(c) for c in p0]
        g1 = [_to_gamma(c) for c in p1]
        mixed = [srgb_to_linear(g0[i] * w0 + g1[i] * w1) for i in range(3)]
    else:
        l0 = linear_to_oklab(tuple(p0))
        l1 = linear_to_oklab(tuple(p1))
        if space == "oklab":
            lab = tuple(l0[i] * w0 + l1[i] * w1 for i in range(3))
        else:  # oklch — polar, shorter hue arc
            def polar(lab):
                L, a, b = lab
                return L, math.hypot(a, b), math.degrees(math.atan2(b, a)) % 360
            L0, C0, H0 = polar(l0)
            L1, C1, H1 = polar(l1)
            dh = ((H1 - H0 + 180) % 360) - 180
            H = (H0 + dh * w1) % 360
            L, C = L0 * w0 + L1 * w1, C0 * w0 + C1 * w1
            lab = (L, C * math.cos(math.radians(H)), C * math.sin(math.radians(H)))
        mixed = list(oklab_to_linear(lab))

    if alpha > 0:
        mixed = [c / alpha for c in mixed]
    return tuple(mixed), alpha * alpha_multiplier


def parse_relative(value: str):
    """rgb(from <colour> <r> <g> <b> [/ <alpha>]).

    A channel is the matching keyword, a number, a percentage or `none`. A calc()
    inside a channel returns None on purpose: computing it would mean implementing
    CSS maths, and a gate that half-implements it is worse than one that says so.
    """
    m = RELATIVE.match(value)
    if not m:
        return None
    body = m.group(1).strip()
    # The origin colour is the first token, and it may itself be a function.
    depth, cut = 0, None
    for i, ch in enumerate(body):
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
        elif ch.isspace() and depth == 0:
            cut = i
            break
    if cut is None:
        return None
    origin = parse_color(body[:cut].strip())
    if origin is None:
        return None
    rest = body[cut:].strip()
    if "calc(" in rest.lower():
        return None
    chan_part, _, alpha_part = rest.partition("/")
    chans = chan_part.split()
    if len(chans) != 3:
        return None

    rgb_gamma = [_to_gamma(c) * 255.0 for c in origin[0]]
    keywords = ("r", "g", "b")
    out = []
    for i, tok in enumerate(chans):
        t = tok.strip().lower()
        if t == keywords[i]:
            out.append(rgb_gamma[i])
        elif t == "none":
            out.append(0.0)
        elif t.endswith("%"):
            try:
                out.append(float(t[:-1]) / 100.0 * 255.0)
            except ValueError:
                return None
        else:
            try:
                out.append(float(t))
            except ValueError:
                return None

    alpha = origin[1]
    if alpha_part.strip():
        t = alpha_part.strip().lower()
        if t == "alpha":
            pass
        elif t.endswith("%"):
            try:
                alpha = float(t[:-1]) / 100.0
            except ValueError:
                return None
        else:
            try:
                alpha = float(t)
            except ValueError:
                return None
    return tuple(srgb_to_linear(max(0.0, min(1.0, c / 255.0))) for c in out), alpha


def parse_color(value: str):
    """-> (linear_rgb, alpha) or None when the value cannot be computed."""
    value = value.strip()
    if value.lower().startswith("color-mix("):
        return parse_color_mix(value)
    if RELATIVE.match(value):
        return parse_relative(value)
    m = RGB.match(value)
    if m:
        parts = [p.strip() for p in re.split(r"[,\s/]+", m.group(1)) if p.strip()]
        if len(parts) not in (3, 4):
            return None
        try:
            ch = [float(p.rstrip("%")) / (100 if p.endswith("%") else 255) for p in parts[:3]]
            a = 1.0
            if len(parts) == 4:
                a = float(parts[3].rstrip("%")) / (100 if parts[3].endswith("%") else 1)
        except ValueError:
            return None
        return tuple(srgb_to_linear(c) for c in ch), a
    m = HEX.match(value)
    if m:
        h = m.group(1)
        if len(h) in (3, 4):
            h = "".join(ch * 2 for ch in h)
        if len(h) not in (6, 8):
            return None
        r, g, b = (int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))
        a = int(h[6:8], 16) / 255 if len(h) == 8 else 1.0
        return (srgb_to_linear(r), srgb_to_linear(g), srgb_to_linear(b)), a
    m = OKLCH.match(value)
    if m:
        L = float(m.group(1).rstrip("%"))
        if m.group(1).endswith("%"):
            L /= 100
        C, H = float(m.group(2)), float(m.group(3))
        alpha = m.group(4)
        a = 1.0
        if alpha is not None:
            a = float(alpha.rstrip("%")) / (100 if alpha.endswith("%") else 1)
        return oklab_to_linear((L, C * math.cos(math.radians(H)), C * math.sin(math.radians(H)))), a
    return None


def linear_to_oklab(rgb):
    r, g, b = rgb
    l = 0.4122214708 * r + 0.5363325363 * g + 0.0514459929 * b
    m = 0.2119034982 * r + 0.6806995451 * g + 0.1073969566 * b
    s = 0.0883024619 * r + 0.2817188376 * g + 0.6299787005 * b
    l_, m_, s_ = (math.copysign(abs(v) ** (1 / 3), v) for v in (l, m, s))
    return (
        0.2104542553 * l_ + 0.7936177850 * m_ - 0.0040720468 * s_,
        1.9779984951 * l_ - 2.4285922050 * m_ + 0.4505937099 * s_,
        0.0259040371 * l_ + 0.7827717662 * m_ - 0.8086757660 * s_,
    )


def oklab_to_linear(lab):
    L, a, b = lab
    l_ = L + 0.3963377774 * a + 0.2158037573 * b
    m_ = L - 0.1055613458 * a - 0.0638541728 * b
    s_ = L - 0.0894841775 * a - 1.2914855480 * b
    l, m, s = (v ** 3 for v in (l_, m_, s_))
    return (
        4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s,
        -1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s,
        -0.0041960863 * l - 0.7034186147 * m + 1.7076147010 * s,
    )


def simulate(rgb, kind):
    mx = CVD_MATRICES[kind]
    return tuple(sum(mx[i][j] * rgb[j] for j in range(3)) for i in range(3))


def delta(rgb_a, rgb_b) -> float:
    a, b = linear_to_oklab(rgb_a), linear_to_oklab(rgb_b)
    return 100 * math.dist(a, b)


def luminance(rgb) -> float:
    r, g, b = rgb
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast(rgb_a, rgb_b) -> float:
    la, lb = luminance(rgb_a), luminance(rgb_b)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)


def oklch_of(rgb):
    L, a, b = linear_to_oklab(rgb)
    return L, math.hypot(a, b), math.degrees(math.atan2(b, a)) % 360


# --- checks ---------------------------------------------------------------

def pick(decls, candidates):
    """First exact token match, in the declared priority order."""
    for stem in candidates:
        if f"--{stem}" in decls:
            return f"--{stem}"
    return None


def is_variant(name: str) -> bool:
    return any(name.endswith(sfx) for sfx in VARIANT_SUFFIXES)


def near_cluster(field, accent, cluster) -> bool:
    _, want_field, want_accent = cluster
    fL, fC, fH = oklch_of(field)
    aL, aC, aH = oklch_of(accent)
    def close(got, want, dL, dC, dH):
        gL, gC, gH = got
        wL, wC, wH = want
        hue_gap = min(abs(gH - wH), 360 - abs(gH - wH))
        return abs(gL - wL) <= dL and abs(gC - wC) <= dC and hue_gap <= dH
    return close((fL, fC, fH), want_field, 0.08, 0.05, 40) and \
        close((aL, aC, aH), want_accent, 0.15, 0.10, 35)


def validate_pack(css: Path) -> None:
    stem = css.stem
    text = css.read_text(encoding="utf-8")
    found = themes(text)
    check(bool(found), f"tokens/{stem}.css: no declaration block the parser could read")
    for label, decls in found:
        validate_theme(stem, label, decls)


def validate_theme(stem: str, label: str, decls: dict) -> None:
    where = f"tokens/{stem}.css [{label}]"

    solids: dict[str, tuple] = {}
    for name in decls:
        raw = resolve(name, decls)
        if raw is None:
            continue
        # Colour-shaped means "claims to be a colour", not "is one we can read".
        # Filtering on readability first is how an unparseable value slips
        # through as a non-colour -- the silent skip this file exists to refuse.
        if not COLOR_SHAPED.match(raw):
            continue
        parsed = parse_color(raw)
        if not check(parsed is not None, f"{where}: '{name}: {raw}' claims to be a colour the validator cannot compute -- "
                                    f"express it as a hex or an oklch() literal so it can be checked"):
            continue
        rgb, alpha = parsed
        if alpha >= 0.999:
            solids[name] = rgb

    check(len(solids) >= 4, f"{where}: only {len(solids)} solid colour tokens found -- the parser is probably missing the syntax")

    field_name = pick(decls, FIELD_TOKENS)
    ink_name = pick(decls, INK_TOKENS)
    if not check(field_name in solids if field_name else False,
                 f"{where}: no field token found (looked for {', '.join('--' + t for t in FIELD_TOKENS)})"):
        return
    if not check(ink_name in solids if ink_name else False,
                 f"{where}: no ink token found (looked for {', '.join('--' + t for t in INK_TOKENS)})"):
        return

    field, ink = solids[field_name], solids[ink_name]
    ratio = contrast(field, ink)
    check(ratio >= 4.5,
          f"{where}: {ink_name} on {field_name} is {ratio:.2f}:1, below WCAG AA 4.5:1")
    notes.append(f"  {stem} [{label}]: {ink_name} on {field_name} = {ratio:.2f}:1")

    # Semantic peers: statuses plus the accent. These carry meaning by colour, so
    # they are exactly the set that must survive a dichromacy.
    peers = {n: rgb for n, rgb in solids.items()
             if not is_variant(n) and (
                 n.lstrip("-") in STATUS_TOKENS or
                 any(n == f"--{s}" for s in STATUS_TOKENS) or
                 n in ("--accent", "--primary", "--cta"))}
    # A pack whose values were read off a production site cannot answer a CVD
    # collision by re-stepping the hex -- that would invent a colour, which is
    # the one thing a pack may never do. The answer is the one the dataviz
    # discipline already gives: below the floor is legal *with* secondary
    # encoding, and the pack has to say so in writing.
    pack_md = PACKS / f"{stem}.md"
    pack_text = pack_md.read_text(encoding="utf-8") if pack_md.is_file() else ""
    encoded = bool(re.search(r"never\s+by\s+colou?r\s+alone", pack_text, re.I))

    names = sorted(peers)
    for i, a in enumerate(names):
        for b in names[i + 1:]:
            d = delta(peers[a], peers[b])
            both_status = sum(
                1 for n in (a, b) if n.lstrip("-") in STATUS_TOKENS) == 2
            if d < 0.5 and not both_status:
                # Identical values are an alias (workbench points --info at the
                # accent on purpose), not a collision. Aliases are a design
                # decision; flagging them would train the author to ignore us.
                # Two *statuses* sharing a value is never an alias, though --
                # that is one colour carrying two meanings, so it falls through
                # to the hard floor below.
                notes.append(f"  {stem} [{label}]: {a} is an alias of {b}")
                continue
            below = [] if d >= DELTA_NORMAL else [f"{d:.1f} at full colour"]
            for kind in CVD_MATRICES:
                dc = delta(simulate(peers[a], kind), simulate(peers[b], kind))
                if dc < DELTA_CVD:
                    below.append(f"{dc:.1f} under {kind}")
            if d < DELTA_HARD:
                check(False,
                      f"{where}: {a} and {b} are {d:.1f} apart at full colour (hard floor "
                      f"{DELTA_HARD}) -- two semantic states in one colour; secondary "
                      f"encoding does not excuse this one")
                continue
            if below:
                check(encoded,
                      f"styles/{stem}.md: {a} and {b} separate by only {'; '.join(below)} "
                      f"(floors {DELTA_NORMAL}/{DELTA_CVD}) and the pack does not state that "
                      f"status is 'never by colour alone' -- declare the secondary encoding")
                if encoded:
                    notes.append(
                        f"  {stem} [{label}]: {a}/{b} tight ({'; '.join(below)}) -- covered by secondary encoding")

    # Provenance gate for the known default clusters.
    accent_name = next((n for n in ("--accent", "--primary", "--cta") if n in solids), None)
    if accent_name:
        pack_md = PACKS / f"{stem}.md"
        head = (pack_md.read_text(encoding="utf-8")[:1500] if pack_md.is_file() else "")
        addressable = bool(re.search(r"Origin:.{0,300}?(https?://|\b[a-z0-9-]+\.[a-z]{2,}\b)", head, re.S | re.I))
        for cluster in AI_DEFAULT_CLUSTERS:
            if near_cluster(field, solids[accent_name], cluster):
                check(addressable,
                      f"styles/{stem}.md: palette sits in the '{cluster[0]}' default cluster "
                      f"and Origin names no addressable reference -- prove it was read, not reached for")
                if addressable:
                    notes.append(f"  {stem} [{label}]: in the '{cluster[0]}' cluster, provenance present")


def _reset():
    global failures, notes, checks
    failures, notes, checks = [], [], 0


def _ratio_plants() -> list[str]:
    """The classification itself, watched discriminating.

    The arithmetic already had a negative control. What did not was the TALLY:
    before this, a claim naming a partner the pack cannot pair was added to
    `guarded` before any pair was computed, so fifteen claims counted as coverage
    the gate never held. A number that cannot be watched being wrong is the thing
    this file exists to refuse, so each bucket gets a plant.
    """
    import tempfile
    global TOKENS, PACKS
    problems = []
    css = (":root {\n  --bg: #ffffff;\n  --ink: #1a1a1a;\n  --line: #dddddd;\n"
           "  --surface-2: #eeeeee;\n  --accent: #8a2b1f;\n"
           "  --muted: rgba(26,26,26,.55);\n}\n")
    plants = [
        # 1. a table declaring a base its own arithmetic contradicts. `blueprint`
        #    shipped exactly this: the header said `--bg` and the numbers were
        #    computed against pure white.
        ("a table header declaring a base the numbers contradict",
         "| Token | Value | Role on `--bg` |\n|---|---|---|\n"
         "| `--accent` | `#8a2b1f` | 9.99:1 |\n",
         lambda: [f for f in failures if "against --bg" in f],
         None),
        # 2. the same claim with the base removed: no longer checked, and it must
        #    land in a named bucket rather than nowhere.
        ("the same claim with no declared base, counted as a table row",
         "| Token | Value | Role |\n|---|---|---|\n"
         "| `--accent` | `#8a2b1f` | 9.99:1 |\n",
         lambda: [] if _tally["un_table"] == 1 else None,
         "un_table"),
        # 3. prose with no partner. Until 2026-08-20 this asserted only that the
        #    claim landed in the `un_prose` bucket, because the broad pairing pass
        #    below was unreachable. It runs now, narrowed to the token named on the
        #    line, so the assertion is the stronger one: a WRONG number in prose is
        #    refused rather than counted. The old form of this fixture kept passing
        #    while the pass it should have been exercising did not exist.
        ("prose stating a ratio that no pair in the pack produces",
         "Body text sits on the panel at 9.99:1 with `--accent`.\n",
         lambda: [f for f in failures if "nothing in this pack pairs" in f],
         None),
        # 4. prose arguing a floor rather than asserting a pair.
        # A floor or a rejected candidate never reaches the classifier at all --
        # RATIO_SKIP drops it one step earlier. What reaches it is a position in
        # a gradient, which is the form `cyclorama` and `awning` actually write.
        ("prose placing a ratio at a gradient stop rather than asserting a pair",
         "The `--accent` reaches 3.10:1 by the 85% stop.\n",
         lambda: [] if _tally["un_argued"] == 1 else None,
         "un_argued"),
        # 5. THE DEFECT THIS CHANGE CLOSED: a partner is named, the subject is a
        #    composite, nothing computes -- and it must not read as coverage.
        ("a named partner whose subject this pack cannot pair",
         "`--muted` composites to 4.13:1 on `--bg` here.\n",
         lambda: [] if _tally["unresolved"] == 1 and _tally["computed"] == 0 else None,
         "unresolved"),
    ]
    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d)
        (tmp / "tokens").mkdir()
        old_tokens, old_packs = TOKENS, PACKS
        TOKENS, PACKS = tmp / "tokens", tmp
        try:
            for label, md, verdict, bucket in plants:
                _reset()
                _tally.update({k: 0 for k in
                               ("computed", "unresolved", "unguarded",
                                "un_table", "un_argued", "un_prose")})
                _unresolved.clear()
                (TOKENS / "_planted_.css").write_text(css, encoding="utf-8")
                (PACKS / "_planted_.md").write_text(md, encoding="utf-8")
                validate_stated_ratios(TOKENS / "_planted_.css")
                got = verdict()
                ok = got is not None and (got or bucket)
                print(f"  {'caught ' if ok else 'MISSED '} {label}")
                if not ok:
                    problems.append(
                        f"{label} — tally was "
                        + ", ".join(f"{k}={_tally[k]}" for k in
                                    ("computed", "unresolved", "un_table",
                                     "un_argued", "un_prose")))
        finally:
            TOKENS, PACKS = old_tokens, old_packs
            _reset()
            _tally.update({k: 0 for k in
                           ("computed", "unresolved", "unguarded",
                            "un_table", "un_argued", "un_prose")})
            _unresolved.clear()
    return problems


def _declared_set_plants() -> list[str]:
    """The declared-set check, watched discriminating.

    Four cases, and the third is the one that matters: a file-wide "never by
    colour alone" must NOT excuse a pair below the hard floor. Without that the
    check is a phrase-detector, and any pack could add one sentence to silence
    it.
    """
    import tempfile
    global TOKENS, PACKS
    problems = []
    # --a and --b collide (one hue family); --c is far from both.
    css = (":root {\n  --bg: #ffffff;\n  --ink: #1a1a1a;\n  --line: #dddddd;\n"
           "  --surface-2: #eeeeee;\n"
           "  --a: #8f3f1f;\n  --b: #9a3016;\n  --c: #0a7558;\n"
           "  /* [ONE] -> --a * [TWO] -> --b * [THREE] -> --c */\n}\n")
    cases = [
        ("a state map whose two states are one colour, with nothing said",
         "The pack ships three states.\n",
         "below the hard floor"),
        ("a file-wide secondary-encoding phrase reaching a hard-floor pair",
         "Status is never by colour alone in this pack.\n",
         "below the hard floor"),
        ("the pair named, with what separates it -- accepted",
         "- `--a` and `--b` are one hue family, told apart by the word.\n",
         None),
        ("the pair named, and the figure it states is wrong",
         "- `--a` and `--b` are one hue family, 9.9 apart at full colour.\n",
         "the disclosure for"),
    ]
    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d)
        (tmp / "tokens").mkdir()
        old_tokens, old_packs = TOKENS, PACKS
        TOKENS, PACKS = tmp / "tokens", tmp
        try:
            for label, md, expect in cases:
                _reset()
                _tally["delta_unbound"] = 0
                (TOKENS / "_planted_.css").write_text(css, encoding="utf-8")
                (PACKS / "_planted_.md").write_text(md, encoding="utf-8")
                validate_declared_semantic_sets(TOKENS / "_planted_.css")
                fired = [f for f in failures if expect in f] if expect else []
                ok = bool(fired) if expect else not failures
                print(f"  {'caught ' if ok else 'MISSED '} {label}")
                if not ok:
                    problems.append(f"{label} — failures: {failures or 'none'}")
        finally:
            TOKENS, PACKS = old_tokens, old_packs
            _reset()
            _tally["delta_unbound"] = 0
    return problems


def _composite_plants() -> list[str]:
    """The composited fill, watched discriminating.

    Case four is the false positive this check shipped with for one run: a
    Components row is resting | hover | active | disabled, and reading the whole
    row made `cyclorama`'s hover fill the resting chip's text colour -- 1.26:1
    reported against a row that renders at 12.4:1.
    """
    import tempfile
    global TOKENS, PACKS
    problems = []
    css = (":root {\n  --bg: #ffffff;\n  --ink: #1a1a1a;\n  --line: #dddddd;\n"
           "  --surface-2: #f4f4f4;\n}\n")
    cases = [
        ("a label composited onto a composited fill, below AA",
         "| **Button** | `--surface-2` fill at 4% ink, `--ink` at 30%, "
         "`4px 8px`, 10-12px/600 | none | none | none |\n",
         "below 4.5"),
        ("the same row with the label at full strength",
         "| **Button** | `--surface-2` fill at 4% ink, `--ink` at 100%, "
         "`4px 8px`, 10-12px/600 | none | none | none |\n",
         None),
        ("a composite with no type size on the row -- a wash, not text",
         "| **Wash** | ink at 6%, `--radius-sm` | none | none | none |\n",
         None),
        # Both fills are light and both pass on their own. Read as ONE cell, the
        # hover's 12% becomes the resting chip's text colour and the row reports
        # 1.26:1 -- which is exactly what `cyclorama` got on this check's first
        # run, against a chip that renders at 12.4:1.
        ("a hover cell's composite must not become the resting text",
         "| **Chip** | ink at 6%, `4px 8px`, Mono 14px | fill -> ink at 12% "
         "| none | none |\n",
         None),
    ]
    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d)
        (tmp / "tokens").mkdir()
        old_tokens, old_packs = TOKENS, PACKS
        TOKENS, PACKS = tmp / "tokens", tmp
        try:
            for label, md, expect in cases:
                _reset()
                _tally["composite_unsized"] = 0
                (TOKENS / "_planted_.css").write_text(css, encoding="utf-8")
                (PACKS / "_planted_.md").write_text(md, encoding="utf-8")
                validate_composited_fill_contrast(TOKENS / "_planted_.css")
                if expect:
                    ok = any(expect in f for f in failures)
                else:
                    ok = not failures
                print(f"  {'caught ' if ok else 'MISSED '} {label}")
                if not ok:
                    problems.append(f"{label} — failures: {failures or 'none'}")
        finally:
            TOKENS, PACKS = old_tokens, old_packs
            _reset()
            _tally["composite_unsized"] = 0
    return problems


def _prescribed_pair_plants() -> list[str]:
    """The Components sweep, watched discriminating.

    Case two is the one B-050 was filed for: the resting pair is fine and the
    HOVER swaps the fill out from under a label that stays. That is the shape of
    B-039 -- a press dimmed the fill and nothing recomputed the label.
    """
    import tempfile
    global TOKENS, PACKS
    problems = []
    css = (":root {\n  --bg: #ffffff;\n  --ink: #1a1a1a;\n  --line: #dddddd;\n"
           "  --surface-2: #eeeeee;\n  --accent: #1f5fb0;\n  --accent-dim: #7f9fd0;\n"
           # White on --accent is 6.3:1 and on --accent-dim is 2.6:1, so the
           # RESTING pair passes and only the dimmed state fails -- which is the
           # shape of B-039. The first version of this fixture used B-039's own
           # values, where resting already failed, so every case went red for the
           # wrong reason and three plants proved nothing.
           "  --on-accent: #ffffff;\n}\n")
    cases = [
        ("a resting pair below AA",
         "| **Btn** | `--accent-dim` fill, `--on-accent` label, 14px/600 | none | none | none |\n",
         "the resting state prescribes"),
        ("a hover that swaps the fill out from under the label",
         "| **Btn** | `--accent` fill, `--on-accent` label, 14px/600 "
         "| fill -> `--accent-dim` | none | none |\n",
         "the hover state prescribes"),
        ("a hover that swaps the fill AND the label with it",
         "| **Btn** | `--accent` fill, `--on-accent` label, 14px/600 "
         "| fill -> `--accent-dim`, label -> `--ink` | none | none |\n",
         None),
        ("a passing pair with `as above` in every state",
         "| **Btn** | `--accent` fill, `--on-accent` label, 14px/600 "
         "| as above | as above | as above |\n",
         None),
        ("half a pair -- a fill and no label",
         "| **Card** | `--surface-2` fill, `--radius`, 14px/400 | none | none | none |\n",
         None),
    ]
    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d)
        (tmp / "tokens").mkdir()
        old_tokens, old_packs = TOKENS, PACKS
        TOKENS, PACKS = tmp / "tokens", tmp
        try:
            for label, md, expect in cases:
                _reset()
                _tally["pair_half_stated"] = _tally["pair_unresolved"] = 0
                (TOKENS / "_planted_.css").write_text(css, encoding="utf-8")
                (PACKS / "_planted_.md").write_text(md, encoding="utf-8")
                validate_prescribed_pairs(TOKENS / "_planted_.css")
                if expect:
                    ok = any(expect in f for f in failures)
                elif "half a pair" in label:
                    ok = not failures and _tally["pair_half_stated"] == 1
                else:
                    ok = not failures
                print(f"  {'caught ' if ok else 'MISSED '} {label}")
                if not ok:
                    problems.append(f"{label} — failures: {failures or 'none'}, "
                                    f"half={_tally['pair_half_stated']}")
        finally:
            TOKENS, PACKS = old_tokens, old_packs
            _reset()
            _tally["pair_half_stated"] = _tally["pair_unresolved"] = 0
    return problems


def self_test() -> int:
    """Plant a defect of each class and require the matching check to fire.

    Without this the suite proves only that the checks ran. It has to be shown
    saying no, and shown staying quiet on clean input -- a validator that fails
    nothing and a validator that fails everything are both green from here.

    `_planted_` stems deliberately match no styles/*.md, so the "declare the
    secondary encoding" and "prove it was read" branches see a pack that says
    nothing, which is the state those checks exist to catch.
    """
    cases = [
        (
            "ink that misses WCAG AA on its own field",
            {"--bg": "#ffffff", "--ink": "#a0a0a0", "--accent": "#8a2b1f", "--line": "#dddddd"},
            "below WCAG AA",
        ),
        (
            "a colour the parser cannot compute",
            {"--bg": "#ffffff", "--ink": "#1a1a1a", "--accent": "color(display-p3 1 0 0)",
             "--line": "#dddddd", "--surface2": "#eeeeee"},
            "cannot compute",
        ),
        (
            "two semantic states rendered in one colour",
            {"--bg": "#ffffff", "--ink": "#1a1a1a", "--line": "#dddddd",
             "--good": "#2f7d4f", "--danger": "#2f7d52"},
            "two semantic states in one colour",
        ),
        (
            # Green and red are far apart at full colour and collapse under
            # deuteranopia -- the textbook pair, and the reason this check exists.
            "statuses a deuteranope cannot separate, with nothing declared",
            {"--bg": "#ffffff", "--ink": "#1a1a1a", "--line": "#dddddd",
             "--good": "#1f7a3d", "--danger": "#b3261e"},
            "never by colour alone",
        ),
        (
            # The class measured on 2026-08-13: twenty-eight semantic colours below AA
            # on their own field across eleven packs, invisible because validate_theme
            # checked ink against field and never a status against field.
            "a status below AA on its own field with nothing saying it is not text",
            None,
            ("_planted_", ":root {\n  --bg: #ffffff;\n  --ink: #1a1a1a;\n"
                          "  --line: #dddddd;\n  --surface2: #eeeeee;\n"
                          "  --good: #7bd48f;\n}\n", ""),
            "nothing says it is not text",
        ),
        (
            "a declared non-text status below the 3:1 floor whose pack never says the word carries it",
            None,
            ("_planted_", "/* @role non-text: --good */\n:root {\n"
                          "  --bg: #ffffff;\n  --ink: #1a1a1a;\n  --line: #dddddd;\n"
                          "  --surface2: #eeeeee;\n  --good: #b6f0c6;\n}\n", ""),
            "below the 3.0:1 non-text floor",
        ),
        (
            "a generated-default palette with no provenance",
            {"--bg": "#f4f1ea", "--ink": "#1a1a1a", "--accent": "#b5623f",
             "--line": "#e0dcd2", "--surface": "#ffffff"},
            "default cluster",
        ),
        # The four below exist because two colour forms became computable in
        # 1.22.0. Two of them prove the new code paths are CHECKED rather than
        # merely tolerated: a mix and a relative colour that miss AA have to fail
        # on the ratio, which is only possible if the parser really computed them.
        # The other two prove the refusals still refuse.
        (
            "a color-mix() in a space this gate does not implement",
            {"--bg": "#ffffff", "--ink": "#1a1a1a", "--line": "#dddddd",
             "--surface2": "#eeeeee",
             "--accent": "color-mix(in lab, #ff0000 40%, #0000ff)"},
            "cannot compute",
        ),
        (
            "a computed color-mix() whose ink misses AA on its own field",
            {"--bg": "#ffffff", "--line": "#dddddd", "--surface2": "#eeeeee",
             "--ink": "color-mix(in oklab, #000000 35%, #ffffff)"},
            "below WCAG AA",
        ),
        (
            "a relative colour whose ink misses AA on its own field",
            {"--bg": "#ffffff", "--line": "#dddddd", "--surface2": "#eeeeee",
             "--ink": "rgb(from #999999 r g b)"},
            "below WCAG AA",
        ),
        (
            # One hex doing two jobs. `showroom` and `atrium` both shipped a hairline
            # the same colour as a surface, which is 1.00:1 -- no rule at all -- and
            # nothing here compared a line against a surface.
            "a hairline the same colour as a surface, undeclared",
            None,
            ("_planted_", ":root {\n  --bg: #ffffff;\n  --ink: #1a1a1a;\n"
                          "  --surface-2: #eeeeee;\n  --line-weak: #eeeeee;\n}\n", ""),
            "are the same colour",
            _line_surface_collision,
        ),
        (
            # And the escape hatch's own hole: a `drawn-on` list naming a token the
            # pack does not declare exempts the line from every surface that exists.
            "a drawn-on declaration naming a surface the pack does not ship",
            None,
            ("_planted_", "/* @role drawn-on: --surface-9 */\n:root {\n"
                          "  --bg: #ffffff;\n  --ink: #1a1a1a;\n"
                          "  --surface-2: #eeeeee;\n  --line-weak: #eeeeee;\n}\n", ""),
            "which this pack does not declare",
            _line_surface_collision,
        ),
        (
            "a relative colour with a calc() channel, which is refused rather than guessed",
            {"--bg": "#ffffff", "--ink": "#1a1a1a", "--line": "#dddddd",
             "--surface2": "#eeeeee",
             "--accent": "rgb(from #2965ec calc(r * 2) g b)"},
            "cannot compute",
        ),
    ]
    problems = []
    for case in cases:
        # Three-tuple: plant a decls dict into validate_theme. Four-tuple: plant a whole
        # token layer as text, for a check that reads the file rather than the dict.
        if len(case) == 3:
            label, decls, expected = case
            _reset()
            validate_theme("_planted_", ":root", decls)
        elif len(case) == 5:
            # A fifth element names the core to plant into, so a new text-based
            # check does not have to be routed through _status_on_field.
            label, _, (stem, text, _pack), expected, core = case
            _reset()
            core(stem, text)
        else:
            label, _, (stem, text, pack), expected = case
            _reset()
            _status_on_field(stem, text, pack)
        fired = [f for f in failures if expected in f]
        print(f"  {'caught ' if fired else 'MISSED '} {label}")
        if not fired:
            problems.append(label)
    _reset()
    # One status token only: the pair checks have nothing to compare, so this
    # case isolates "does the rest of the suite stay quiet on good input".
    validate_theme(
        "_planted_", ":root",
        {"--bg": "#ffffff", "--ink": "#1a1a1a", "--accent": "#1f4f8a",
         "--line": "#dddddd", "--surface": "#f2f2f2", "--good": "#1f7a3d"},
    )
    print(f"  {'quiet  ' if not failures else 'NOISY  '} a clean palette")
    if failures:
        problems.append("false positive on a clean palette: " + "; ".join(failures))
    _reset()
    problems += _ratio_plants()
    problems += _declared_set_plants()
    problems += _composite_plants()
    problems += _prescribed_pair_plants()
    if problems:
        print("\nself-test FAILED: " + "; ".join(problems))
        return 1
    print("\nself-test OK — every check was watched failing against a planted defect")
    return 0


# --- stated ratios --------------------------------------------------------
#
# The token layer is the single home for a pack's VALUES, and that half is
# honoured -- 829 definitions, zero drift. A contrast ratio is just as derived a
# fact as the hex is, and it was not: every ratio is computed once by hand, then
# copied into the palette table, into the prose, and into a CSS comment, and the
# three copies drift independently. Fourteen stated ratios were wrong when this
# check was written; `blueprint` carried the same wrong number in four places
# across two files, because its ratio column is headed ``On `--bg` `` and was
# computed against pure white while its stock is #FBFBFC.
#
# The check needs no pair-matching heuristic to be trustworthy: the token is
# named on the same line as the number. Subject = the first token on the line;
# the ratio is checked against the pack's field, then against any other token
# named on that line, then against every theme -- so a dark-theme comment and a
# "text ON the accent" row both resolve without special cases. Anything that
# matches nothing in the pack is a number that pack cannot produce.
# The `1` must not be followed by a unit either: `--space-4: 1rem` is a CSS
# declaration, not a 4:1 contrast claim. That false positive sat undetected
# because the old code skipped any claim whose partner it could not name, and
# this one never had a partner -- the same blind spot, one layer down.
RATIO_CLAIM = re.compile(r"(\d+(?:\.\d+)?)\s*:\s*1(?![\d.]|[A-Za-z])")
TOKEN_ON_LINE = re.compile(r"--[a-z][a-z0-9-]*")
# ``| Token | Value | Role | On `--bg` |`` -- the table stating what it measured
# against. blueprint's says `--bg` and its numbers were computed against pure
# white, which is the whole finding: the header was right and the arithmetic was
# not, and nothing read the header.
TABLE_BASE = re.compile(r"[Oo]n\s+`(--[a-z0-9-]+)`")
# The library's uniform way of naming the other side, in a CSS comment or in a
# table cell: "17.74:1 on --bg", "6.1:1 over `--accent-deep`".
PARTNER_PHRASE = re.compile(
    r"\b(?:on|over|against)\s+(?:the|a|an|its)?\s*`?(--[a-z0-9-]+)`?")
# "16.5–17.8:1" spans a set of tokens and has no single right answer. Only a
# dash BETWEEN TWO NUMBERS counts: an earlier version skipped any line
# containing an em dash, which is most prose in this repo, and silently dropped
# four real defects while still reporting green.
RATIO_RANGE = re.compile(r"\d\s*[–—-]\s*\d+(?:\.\d+)?\s*:\s*1")
RATIO_TOL = 0.1
# A hex written on the line the claim sits on. Two places in the library argue
# about a colour the pack deliberately does NOT ship -- blueprint on pure black,
# maquette on pure white -- and for those the literal is the partner.
HEX_ON_LINE = re.compile(r"#[0-9a-fA-F]{6}\b")
# A line that is arguing about a number rather than asserting one.
RATIO_SKIP = re.compile(
    r"(?i)\b(?:floor|minimum|at least|must clear|no better than|no worse than|"
    r"would|were|target|aim|WCAG|AA|AAA|budget|but|"
    r"reject|rejected|candidate|instead|not\b|fails?|failing|below the)\b"
)


def _theme_maps(text: str) -> list[tuple[str, dict, tuple | None]]:
    """(label, {token: linear_rgb}, field_rgb) per theme."""
    out = []
    for label, decls in themes(text):
        solids = {}
        for name in decls:
            raw = resolve(name, decls)
            if raw is None:
                continue
            parsed = parse_color(raw)
            if parsed and parsed[1] >= 0.999:
                solids[name] = parsed[0]
        field_name = pick(decls, FIELD_TOKENS)
        out.append((label, solids, solids.get(field_name)))
    return out


# The tokens that carry meaning by colour. A -wash / -tint / -weak variant is a
# background, not one of these.
SEMANTIC_ROLES = ("good", "ok", "success", "warn", "warning", "danger", "error", "info",
                  "live", "accent", "brand", "cta", "primary", "action", "link")
# The escape, and it extends `@role accent:` rather than inventing a convention.
ROLE_NON_TEXT = re.compile(r"@role\s+non-text\s*:\s*([^\n*]*)", re.I)
# WCAG 1.4.11: a mark that must be understood on its own needs 3:1. Below that a
# colour can only be decorative reinforcement beside a word.
NON_TEXT_FLOOR = 3.0


def validate_status_on_field(css: Path) -> None:
    """Every semantic colour is readable on its own field, or says it is not text.

    validate_theme() computed exactly one contrast -- ink against field -- and then went
    to peer separation, so no status was ever checked against the surface it sits on.
    That hole hid a class across the library: measured 2026-08-13, twenty-one semantic
    colours in eight packs sit below AA on their own field, and ten of them below the
    3:1 non-text floor as well. The worst was mechanical rather than chosen --
    scoreboard's `[data-surface="panel"]` block remaps eleven tokens and not the status
    set, so `var(--good)` painted 3.69:1 on the dark band where `--good-on-dark` had
    10.21 waiting (board B-034).

    Most of the twenty-one are legitimately not text: a dot, a chip tint, a chart
    series. The packs said so -- in five different phrasings ("never text on the field",
    "a FILL and large-text colour", "a fill, not a text colour", "No coral word under
    24px", "category marks"), which is exactly why nothing could check it. So the ask is
    a canonical marker rather than a colour change, and the marker is the one the
    library already uses for the accent role.

    Three tiers, which is what the packs already argue:
      >= 4.5   text, no declaration needed
      >= 3.0   declared non-text: a mark that can carry meaning on its own
      <  3.0   declared non-text AND the pack states status is never by colour alone,
               because below the non-text floor the colour is reinforcement and the
               word is the message
    """
    stem = css.stem
    pack_md = PACKS / f"{stem}.md"
    _status_on_field(stem, css.read_text(encoding="utf-8"),
                     pack_md.read_text(encoding="utf-8") if pack_md.is_file() else "")


def _status_on_field(stem: str, text: str, pack: str) -> None:
    """The core, split out so the self-test can plant a token layer as a string.

    A check that can only be exercised by editing a real file is a check whose plant
    drifts from the tree it is meant to protect.
    """
    encoded = bool(re.search(r"never\s+by\s+colou?r\s+alone", pack, re.I))
    declared = set()
    for m in ROLE_NON_TEXT.finditer(text):
        declared |= set(re.findall(r"--[a-z0-9-]+", m.group(1)))

    for label, decls in themes(text):
        solids = {}
        for name in decls:
            raw = resolve(name, decls)
            if not raw:
                continue
            parsed = parse_color(raw)
            if parsed and parsed[1] >= 0.999:
                solids[name] = parsed[0]
        field_name = pick(decls, FIELD_TOKENS)
        if field_name not in solids:
            continue
        field = solids[field_name]
        for name in sorted(solids):
            if is_variant(name) or name.lstrip("-") not in SEMANTIC_ROLES:
                continue
            ratio = contrast(solids[name], field)
            if ratio >= 4.5:
                continue
            where = f"tokens/{stem}.css [{label}]"
            if not check(
                name in declared,
                f"{where}: {name} is {ratio:.2f}:1 on {field_name} and nothing says it is "
                f"not text -- declare it in an '@role non-text:' list with the reason, or "
                f"give the role a value that clears AA",
            ):
                continue
            if ratio < NON_TEXT_FLOOR:
                check(
                    encoded,
                    f"styles/{stem}.md: {name} is {ratio:.2f}:1 on {field_name}, below the "
                    f"{NON_TEXT_FLOOR}:1 non-text floor, so the colour cannot carry the "
                    f"meaning by itself -- the pack must state that status is never by "
                    f"colour alone",
                )
            else:
                notes.append(f"  {stem} [{label}]: {name} at {ratio:.2f}:1 -- declared non-text")


# ------------------------------------------- one hex doing two jobs
#
# A hairline the same colour as the surface it is drawn on is not a faint
# hairline, it is no hairline: 1.00:1. Two packs shipped it. `showroom` declares
# `--line-weak` and `--surface-2` as the same `#edeff3`, so a rule inside the
# sunken well the specimen sits in is invisible; `atrium` declares `--line-ink`
# and `--surface-ink` as the same `#2a2b2f`, and `--line-ink` is the ghost
# control's border while `--surface-ink` is the banner a ghost control most
# plausibly sits on. Neither is caught by anything else here: `validate_theme`
# compares ink against field and then separates semantic peers, and a line is
# neither.
#
# SCOPE: lines against surfaces, and identity rather than a low-contrast
# threshold. Two reasons, both measured on this tree.
#   1. A threshold is arbitrary and this library's hairlines are deliberately
#      almost invisible -- `showroom`'s --line-weak is 1.15:1 on --bg and 1.10:1
#      on --surface, both correct and both under any threshold worth writing.
#      Identity is not a judgement call.
#   2. Other family pairs sharing a hex are usually a designed alias, not a
#      collision: `atrium`'s --on-ink IS --bg because the inverted surface's text
#      is the field colour, and `workbench` points --info at --accent on purpose.
#      validate_theme already reports those as aliases.
#
# The escape is a declaration, in the idiom this file already uses for the accent
# and for non-text status: `@role drawn-on: --a, --b` says which surfaces the line
# is for, and a surface outside that list is out of scope. A collision a reader
# can see in the token layer is a decision; one they discover in a browser is not.
# The token list stops at the em dash that starts the reason. The first draft read
# to the end of the line, so the tokens NAMED IN THE REASON -- "--line-weak is the
# same hex as --surface-2" -- were read as permitted surfaces, and the check passed
# the very collision that sentence was describing. A marker that grants whatever it
# mentions grants everything.
ROLE_DRAWN_ON = re.compile(r"@role\s+drawn-on\s*:\s*([^\n*\u2014\u2013]*)", re.I)
# A marker governs the next token declared after it, which is the convention every
# `@role` comment in this library already follows.
NEXT_DECL = re.compile(r"^\s*(--[a-z0-9-]+)\s*:", re.M)
LINE_ROLES = ("line", "hairline", "rule", "border", "seam", "divider", "stroke")
SURFACE_ROLES = ("bg", "base", "paper", "canvas", "surface", "panel", "field", "well")


def _role_family(name: str, roles) -> bool:
    """True when the token's own name puts it in this family.

    Read from the name's segments rather than by substring: `--line-weak` is a
    line and `--underline-offset` is not, and `--surface-grad-from` is a surface
    while `--on-surface` is ink for one.
    """
    parts = name.lstrip("-").split("-")
    if parts and parts[0] == "on":
        return False
    return any(part in roles for part in parts)


def validate_line_surface_collision(css: Path) -> None:
    _line_surface_collision(css.stem, css.read_text(encoding="utf-8"))


def _line_surface_collision(stem: str, text: str) -> None:
    """The core, split out so the self-test can plant a token layer as a string.

    Same reason as `_status_on_field`: a check exercised only by editing a real
    pack has a plant that drifts away from the tree it protects.
    """
    for label, decls in themes(text):
        solids = {}
        for name in decls:
            raw = resolve(name, decls)
            if not raw:
                continue
            parsed = parse_color(raw)
            if parsed and parsed[1] >= 0.999:
                solids[name] = parsed[0]
        lines = [n for n in sorted(solids) if _role_family(n, LINE_ROLES)]
        surfaces = [n for n in sorted(solids) if _role_family(n, SURFACE_ROLES)
                    and not _role_family(n, LINE_ROLES)]
        # The declarations are read from the whole file, not per theme: a pack states
        # where a line is drawn once, and a theme re-declares values, not roles.
        drawn_on: dict[str, set[str]] = {}
        for m in ROLE_DRAWN_ON.finditer(text):
            owner = NEXT_DECL.search(text, m.end())
            if owner:
                drawn_on.setdefault(owner.group(1), set()).update(
                    re.findall(r"--[a-z0-9-]+", m.group(1)))
        # A surface named in a `drawn-on` list has to exist, or the declaration is
        # satisfied by a typo -- which is how an escape hatch becomes a bypass.
        for owner, named in sorted(drawn_on.items()):
            for tok in sorted(named):
                check(
                    tok in decls,
                    f"tokens/{stem}.css [{label}]: '@role drawn-on:' for {owner} names {tok}, "
                    f"which this pack does not declare -- a list of surfaces that do not "
                    f"exist exempts the line from every surface that does",
                )
        for ln in lines:
            declared = drawn_on.get(ln, set())
            for sf in surfaces:
                if solids[ln] != solids[sf]:
                    continue
                if declared and sf not in declared:
                    continue  # the pack says this line is not drawn there
                check(
                    False,
                    f"tokens/{stem}.css [{label}]: {ln} and {sf} are the same colour, so a "
                    f"rule in {ln} on {sf} is 1.00:1 -- not faint, absent."
                    + (f" '@role drawn-on:' for {ln} names {sf} anyway."
                       if declared else
                       " Give the line its own value, or declare '@role drawn-on: …' naming"
                       " the surfaces it IS drawn on, so the collision is a decision a reader"
                       " can see."),
                )


# Counted, not restated. Every figure the comment inside this function used to
# assert is derived here and printed once per run.
_tally: dict = {"computed": 0, "unresolved": 0, "unguarded": 0,
                "delta_unbound": 0, "composite_unsized": 0,
                "pair_half_stated": 0, "pair_unresolved": 0,
                "un_table": 0, "un_argued": 0, "un_prose": 0, "broad": 0,
                "packs_guarded": set(), "packs_unguarded": set()}
# Every claim that named a partner and still produced no arithmetic, kept with
# its reason. `guarded` used to be incremented BEFORE the pairs were computed,
# so fifteen claims counted as coverage the gate never held -- the same shape
# this whole check exists to refuse, one layer inside its own tally.
_unresolved: list[str] = []

# Why an unguarded claim is unguarded. The single lumped number said 177 and
# said nothing about which of them a person could close: 27 sit in a table whose
# header declares no base, and declaring it makes the existing arithmetic cover
# every row at once. The three markers below are the classes the two thrown-away
# guard attempts kept tripping over -- a floor, a bound, a gradient stop and a
# rejected candidate are arguments ABOUT a measurement, not claims about a pair
# of shipped tokens, and eight of attempt 2's nine findings were exactly these.
# Only the terms that can actually REACH this point. `RATIO_SKIP` above already
# drops a floor, a bound, a rejected candidate and anything mentioning WCAG --
# so listing those here again would be alternatives that never match, which
# reads as coverage and is not. What survives RATIO_SKIP and is still an
# argument rather than an assertion is a position in a gradient, a comparison
# written as a symbol, and a colour dismissed by adjective.
ARGUED = re.compile(
    r"≥|>=|≤|<=|\b\d{1,3}\s*%|\bstop\b|gradient"
    r"|ruled out|refused|discard|rather than|too (?:low|dark|light)"
    # Added 2026-08-20 so the broad pairing check below could be turned ON for
    # prose. Each of these is a shape that is CORRECT writing and cannot be a
    # claim about two shipped tokens, adjudicated one line at a time:
    #   * a comparison against a colour this pack does not ship
    #     (`blueprint.md:115` — "7.53:1 on pure white")
    #   * a bound over a SET of surfaces rather than one pair
    #     (`editorial-luxury.md:145` — "11.8:1 on every tint";
    #      `cyclorama.md:394` — "1.97:1 on any of the six field stops")
    #   * a candidate the pack measures in order to REJECT it
    #     (`cyclorama.css:66` — a list of rejected oranges)
    # The two remaining shapes were NOT excused: they were wrong writing and are
    # fixed in the packs, because in both the figure and its subject had drifted
    # onto different lines or the named token was the REMEDY rather than the
    # subject — and a reader cannot tell those from a claim either.
    r"|pure white|on white\b|every tint|any of the|all six|on any\b"
    r"|large (?:text )?only|under protanopia|candidate|considered"
)


def _pairs(maps, subjects, partners) -> list[float]:
    """Every ratio this pack computes between a subject and a named partner."""
    got: list[float] = []
    for _label, solids, _field in maps:
        got += [
            contrast(solids[s], solids[n])
            for s in subjects if s in solids
            for n in partners if n in solids and n != s
        ]
    return got


# A THIRD ATTEMPT AT A GUARD, WRITTEN AND THROWN AWAY -- recorded because the
# reason is the same one that killed the first two, and it took a measurement to
# see it. A wrapped comment leaves the partner alone with the number
# (``4.40:1 on --bg-deep.``), so reading the subject off the line above looked
# like free coverage: a probe said it resolved 7 of the 15. It did not. The probe
# accepted a match under EITHER comparison mode -- exact or at-least -- so any
# ratio above the claim counted as agreement, and running it inside the gate
# produced two false failures at `ledger.css:33`, where the real subject
# (`--muted`) is a composite and the line above offers `--ink-2` instead.
# Substituting a subject is the same act as guessing a partner. The 15 are
# reported by file:line instead, and a reader who wants them checked names the
# subject on the line.
# The one measurement anybody ever hand-checked, and its date. Kept as data so the
# printed line can say plainly which part of the total was verified and which was
# not -- and so it cannot be mistaken for a statement about the tree today.
HAND_VERIFIED = (71, 121, 16, "2026-08-12")


def check_ratio_coverage(floors: dict) -> list[str]:
    """Coverage is a ratchet, in both directions.

    A check-count floor cannot see this: deleting a `on \u0060--bg\u0060` from one
    table header moves 27 claims out of the arithmetic and the count of *other*
    checks does not move with it. So the three figures are pinned. `computed`
    may only rise, `unresolved` and `unguarded` may only fall, and a commit that
    wants otherwise says so here with the reason -- the same contract the
    check-count floors already carry.
    """
    want = floors.get("validate_palette.py:ratios")
    if not want:
        return ["floors.json has no `validate_palette.py:ratios` block — "
                "coverage that is not pinned is coverage that can leave quietly"]
    bad = []
    if _tally["computed"] < want["computed_at_least"]:
        bad.append(
            f"{_tally['computed']} ratio claims computed, below the pinned "
            f"{want['computed_at_least']}. Arithmetic does not stop running on "
            f"its own: a declared base was removed, or a claim was reworded out "
            f"of reach. Lower the pin in the same commit, with the reason")
    for key, label in (("unresolved", "named a partner this pack cannot pair"),
                       ("unguarded", "reach no check at all")):
        if _tally[key] > want[f"{key}_at_most"]:
            bad.append(
                f"{_tally[key]} claims {label}, above the pinned "
                f"{want[f'{key}_at_most']}. A new claim must name a partner the "
                f"token layer can pair, or the pin moves with a reason")
    return bad


def stated_ratio_report() -> str:
    """The split, never a single number.

    `guarded` is gone as a figure: it counted claims whose arithmetic had not
    run. What is printed is what happened -- computed, named-but-unpairable, and
    the three reasons a claim reached no check at all.
    """
    c, u = _tally["computed"], _tally["unresolved"]
    un, pk = _tally["unguarded"], len(_tally["packs_unguarded"])
    b = _tally["broad"]
    # `broad` belongs in the total or the total shrinks by exactly the number of
    # claims the new pass verified: adding the bucket without adding it here
    # printed 495 claims where 526 exist, which is a report getting quieter as
    # coverage improves.
    total = c + u + un + b
    share = f"{un / total * 100:.0f}%" if total else "n/a"
    v_un, v_total, v_packs, when = HAND_VERIFIED
    return (
        f"stated ratios: {total} claims — {c} computed, {u} named a partner this "
        f"pack cannot pair, {un} unguarded ({share}) at {pk} packs "
        f"[{_tally['un_table']} in a table declaring no base, "
        f"{_tally['un_argued']} placing it at a gradient stop, "
        f"{_tally['un_prose']} prose the broad pass cannot pair], "
        f"{_tally['broad']} verified by the broad pass. "
        f"Hand-verified: {v_un} of {v_total} at "
        f"{v_packs} packs on {when}, and nothing since"
    )


def declared_set_report() -> str:
    """What the disclosure check could not bind, said out loud.

    A figure in a sentence that names three tokens belongs to one of three pairs
    and the document does not say which. Skipping it is right; skipping it
    silently would make this check read as covering every disclosure in the
    library, which is the failure the ratio half of this file spent a day on.
    """
    n = _tally["delta_unbound"]
    return (f"declared sets: {n} disclosure figure(s) left unchecked — their "
            f"sentence names more than two tokens, so which pair the number "
            f"describes is not stated. Name one pair per sentence to gate it")


def validate_stated_ratios(css: Path) -> None:
    stem = css.stem
    maps = _theme_maps(css.read_text(encoding="utf-8"))
    if not maps:
        return
    sources = [(f"tokens/{stem}.css", css)]
    pack_md = PACKS / f"{stem}.md"
    if pack_md.is_file():
        sources.append((f"styles/{stem}.md", pack_md))

    for rel, path in sources:
        base: str | None = None  # the comparison base a table declares in its header
        lines = path.read_text(encoding="utf-8").splitlines()
        for lineno, line in enumerate(lines, 1):
            if not line.startswith("|"):
                base = None
            # Only a real header row declares the base -- the row beneath it is
            # the `|---|` separator. Reading it from any row let a data cell
            # ("4.8:1 on `--dawn-1`") redefine the base for every row below it,
            # which flagged six correct claims in `field-notes`.
            elif TABLE_BASE.search(line) and lineno < len(lines) and set(
                lines[lineno].replace("|", "").replace(" ", "")
            ) <= {"-", ":"} and lines[lineno].strip():
                base = TABLE_BASE.search(line).group(1)
            claims = RATIO_CLAIM.findall(line)
            if not claims or RATIO_SKIP.search(line) or RATIO_RANGE.search(line):
                continue  # a range, or a line arguing about a number
            names = TOKEN_ON_LINE.findall(line)
            if not names:
                continue
            subject, others = names[0], names[1:]
            atleast = "≥" in line or ">=" in line

            # SCOPE, deliberately narrow. A ratio is only checked when the
            # document says what it measured against, because a heuristic that
            # guesses the other side produces a gate nobody trusts: the first
            # draft of this check guessed, and 22 of its 40 findings were prose
            # narrating a rejected candidate or a gradient stop.
            #
            # Two forms count as declared:
            #   1. a palette-table column headed ``On `--bg` `` -- the row's
            #      partner is that token. This is where the real defects were:
            #      blueprint's column says `--bg` (#FBFBFC) and every number in
            #      it was computed against pure white.
            #   2. `--on-X`, whose own name states that it sits on `--X`, or any
            #      other token named on the same line.
            # A `-ink` suffix is deliberately NOT read as "text on X": the
            # convention is pack-dependent. `editorial-luxury`'s `--accent-ink`
            # is text ON the accent; `field-notes`' `--brand-ink` is a text-safe
            # variant of the brand, on the paper. Inferring one meaning flagged
            # six correct claims in `field-notes`.
            # Prose ratios and worst-stop tables (`cyclorama`) are out of scope
            # and stay out until they declare a base; see the board.
            partner_names = PARTNER_PHRASE.findall(line)
            if subject.startswith("--on-"):
                partner_names.append("--" + subject[len("--on-"):])
            if line.startswith("|") and base:
                partner_names.append(base)
            if not partner_names:
                # ------------------------------------------------------------
                # LEFT UNGUARDED, DELIBERATELY — and the size of the hole is
                # COUNTED on every run rather than written here. A ratio whose
                # line names no partner and whose table declares no base is
                # skipped, including inside packs whose tables DO declare a base,
                # because a Gotchas paragraph is not a table row. The counters
                # below feed the `stated ratios:` line this script prints.
                #
                # WHAT WAS VERIFIED, AND WHEN. On 2026-08-12 the library held 121
                # stated ratios, 71 of them unguarded at sixteen packs, and all 71
                # were recomputed by hand that day and found correct. That is the
                # whole of the hand-verification and it has never been repeated.
                # Every claim added since is unguarded AND unverified, and the
                # printed count is the only honest statement of how many: the
                # sentence this comment used to carry — "nothing is wrong today" —
                # was true of a tree with 121 claims in it and was still sitting
                # here at more than four times that, which is the exact failure
                # mode this file exists to refuse.
                #
                # Two attempts to guard them were written and both were thrown
                # away, and the reasons are the finding:
                #
                #   1. "Can any pair of this pack's tokens produce that number?"
                #      cannot fail. Thirty solid tokens are ~435 pairs spanning
                #      1:1 to 20:1; a planted 9.99:1 sailed through. A check
                #      that cannot fail is worse than none, because it reports
                #      coverage it does not have.
                #   2. Narrowing the pool to the token named on the line does
                #      fail — on nine lines, and eight of them are correct
                #      writing. They are floors ("body on cream must clear
                #      4.5:1"), bounds ("no better than 1.97:1 on any of the
                #      six"), positions in a gradient ("4.06:1 by the 85%
                #      stop"), and candidate colours the pack measures in order
                #      to REJECT them. None is a claim about a pair of shipped
                #      tokens, which is the only thing this file can check.
                #
                # So the guard needs to tell a measurement from an argument
                # about a measurement, and that is a real piece of work rather
                # than a regex. Filed rather than faked.
                # NOT counted as unguarded yet. Since 2026-08-20 a prose line goes
                # on to the broad pairing pass below, and a claim that pass verifies
                # is not unguarded — it is checked against every pair the pack can
                # make, subject-narrowed. Counting it here made the printed line say
                # `37 prose` unguarded about 37 claims the run had just verified,
                # which is the same class of untruth as the number it replaced.
                # `unguarded` is incremented at the two places a claim actually
                # escapes: a table row, an argued line, or a prose line the pass
                # cannot pair.
                def _unguarded(n=len(claims)):
                    _tally["unguarded"] += n
                    _tally["packs_unguarded"].add(stem)
                # WHICH KIND, so the closable class is visible. A table row is
                # closable by one edit to the header; an argued claim is out of
                # scope by construction; prose is the residue the board carries.
                # `lstrip()`, not the raw line. Two `cyclorama` rows sit inside an
                # indented table and `line.startswith("|")` read them as prose, so
                # the closable-by-one-header-edit class under-reported and the prose
                # residue over-reported by the same two. Found 2026-08-20 by
                # adjudicating the nine lines the broad check fails on.
                if line.lstrip().startswith("|"):
                    _tally["un_table"] += len(claims)
                    _unguarded()
                elif ARGUED.search(line):
                    _tally["un_argued"] += len(claims)
                    _unguarded()
                # The broad pairing check below was UNREACHABLE from the day the
                # `continue` was written until 2026-08-20: 29 lines that read as a
                # live check and had never run. The comment above explains why it
                # was bypassed — nine lines fail it and eight of those are correct
                # writing — but a bypass written as dead code is a check a reader
                # believes in. Those nine were adjudicated one at a time: three are
                # out of scope by construction and are now named in `ARGUED`, two
                # were an indented table misread as prose, and four were wrong
                # writing, fixed in the packs. The check runs on prose now.
                if line.lstrip().startswith("|") or ARGUED.search(line):
                    continue
                literal = [
                    parsed[0] for parsed in
                    (parse_color(h) for h in HEX_ON_LINE.findall(line))
                    if parsed
                ]
                for claim in claims:
                    want = float(claim)
                    got: list[float] = []
                    for _label, solids, _field in maps:
                        for s in names:
                            if s not in solids:
                                continue
                            got += [contrast(solids[s], o) for o in literal]
                            got += [
                                contrast(solids[s], solids[n])
                                for n in solids if n != s
                            ]
                    if not got:
                        # The pass could not pair it: this is the residue, and it
                        # is the only prose that is genuinely unguarded.
                        _tally["un_prose"] += 1
                        _unguarded(1)
                        continue
                    _tally["broad"] += 1
                    ok = any(c >= want - RATIO_TOL for c in got) if atleast else \
                        any(abs(c - want) <= RATIO_TOL for c in got)
                    check(
                        ok,
                        f"{rel}:{lineno}: states {claim}:1 for "
                        f"{'/'.join(names)} and nothing in this pack pairs with "
                        f"it to produce that. Name the partner if the claim is "
                        f"real, or write the literal it argues about on the line",
                    )
                continue
            # A row often carries several tokens (`--surface-2` / `-3`) and one
            # ratio that belongs to whichever of them it describes. Any of them
            # satisfying the claim is enough; the check is "this pack can produce
            # that number for a token on this row", not "for the first one".
            subjects = names if not subject.startswith("--on-") else [subject]

            for claim in claims:
                want = float(claim)
                got = _pairs(maps, subjects, partner_names)
                if not got:
                    # NOT COVERAGE. The claim names a partner, and this pack
                    # pairs nothing with it: the subject is a composite or an
                    # alpha, or it is nowhere on this line or the one above.
                    # Counted apart and printed, because the alternative is the
                    # defect this change exists to close.
                    _tally["unresolved"] += 1
                    _unresolved.append(
                        f"{rel}:{lineno}: {claim}:1 against "
                        f"{'/'.join(partner_names)} — no pair in this pack "
                        f"computes it; the subject is not on this line"
                    )
                    continue
                _tally["computed"] += 1
                _tally["packs_guarded"].add(stem)
                ok = any(c >= want - RATIO_TOL for c in got) if atleast else \
                    any(abs(c - want) <= RATIO_TOL for c in got)
                check(
                    ok,
                    f"{rel}:{lineno}: states {claim}:1 for {subject} against "
                    f"{'/'.join(partner_names)}, but the token layer computes "
                    f"{', '.join(f'{c:.2f}' for c in sorted(set(round(x, 2) for x in got)))} "
                    f"-- a ratio is derived from the tokens, so it is checked like one",
                )



FLOORS = Path(__file__).resolve().parent / "floors.json"



# ------------------------------------- a pack's OWN semantic sets
#
# `validate_theme`'s peer set is `STATUS_TOKENS` plus `--accent`/`--primary`/
# `--cta`, so a pack that carries meaning in tokens of its own naming is compared
# against nothing. `field-notes` exists to render provenance and its three
# provenance inks -- `--verify-ink`, `--brand-ink`, `--witness-ink` -- are all
# excluded by name; two of them were **3.21 apart** (0.83 under deuteranopia) on
# the two labels a reader most needs to tell apart, and no check could see it.
#
# The set is not invented here and it is not a new syntax. Two forms already ship:
#
#   1. the state map a pack writes in its token layer as
#      ``[EXTRACTED] -> --verify-ink * [INFERRED] -> --brand-ink``. Every token in
#      one map carries a different state of one thing, which is exactly the peer
#      relation the CVD floors are about.
#   2. a distinctness CLAIM: ``destructive -- kept distinct from `--witness` ``.
#      A sentence asserting two tokens are told apart is a claim, and a claim
#      carries its check.
#
# What this deliberately does NOT do is guess a set from token names. `--brand`
# and `--brand-ink` are one colour's two jobs; `--witness` and `--danger` are two
# meanings that happen to share a hue family. Nothing in the naming separates
# those cases, which is why the pack has to say which it means.
STATE_MAP = re.compile(r"\[([A-Z][A-Z0-9_ -]*)\]\s*(?:->|→)\s*(--[a-z0-9-]+)")
# "kept distinct from `--witness`", "distinct from --witness"
DISTINCT_CLAIM = re.compile(r"distinct from\s+`?(--[a-z0-9-]+)`?", re.I)
# "3.2 apart", "**2.8** from `--witness`" -- a distance the pack states about a
# pair it names. A disclosure carrying a number is a claim like any other, and
# `validate_stated_ratios` cannot see it: that check reads contrast ratios, and
# this is an OKLab distance.
# Bound to the quantity it names, never to a pool. The first version accepted a
# match against every theme AND every CVD simulation, so a planted 5.9 found
# something to agree with and the plant did not fail -- the "cannot fail" shape
# this file already records twice. `N apart` is a full-colour distance; `N under
# <kind>` is that simulation. A bare number is not checked, because nothing says
# what it measures.
# ONE pattern, because two of them cut a real sentence in half. `maquette` writes
# "`--good` and `--danger` still sit 6.4 apart under deuteranopia": an `apart`
# pattern claimed the figure as full-colour and an `under` pattern needed the
# number adjacent to the word, so the check compared a deuteranopia figure with
# the full-colour distance and called a correct sentence wrong. The qualifier
# decides which quantity it is, and a bare number with no qualifier at all is
# not read.
DELTA_FIGURE = re.compile(
    r"\*{0,2}([0-9]+(?:\.[0-9]+)?)\*{0,2}\s*"
    r"(?:apart\s*)?"
    r"(?:(?P<full>at full colou?r)"
    r"|under\s+(?P<cvd>protanopia|deuteranopia|tritanopia)"
    r"|(?P<bare>apart\b))"
)


def _figures(sentence: str) -> list[tuple[float, str]]:
    """Every distance the sentence states, each bound to what it measured."""
    out = []
    for m in DELTA_FIGURE.finditer(sentence):
        value = float(m.group(1))
        out.append((value, m.group("cvd") if m.group("cvd") else "full colour"))
    return out


DELTA_TOL = 0.15
# The one escape, and it must NAME the carrier. A pack whose values were read off
# a reference cannot re-step a hex, so where the reference itself renders two
# meanings in one hue the honest answer is to say so and say what separates them
# instead -- form, placement, or the word itself. "Never by colour alone" is the
# phrase the status half already uses; the rest are the ways this library
# actually writes it.
NOT_BY_HUE = re.compile(
    r"never by colou?r alone|one hue family|told apart by (?:form|placement|shape|the word)"
    r"|separated by (?:form|placement|shape|the word)|not by hue",
    re.I,
)


def _blocks(text: str) -> list[str]:
    """One claim per block: a paragraph, or a bullet with its continuation lines.

    Per-LINE matching looked right and checked almost nothing -- in `field-notes`
    the phrase "one hue family" sits on the bullet's first line and the two token
    names on its third, so the pack's own numbers were never bound to the pair
    they describe. Whole paragraphs then over-bound: `cyclorama`'s status bullet
    list is one paragraph, and every number in it bound to every pair, which
    reported five failures against five correct sentences.
    """
    out, cur = [], []
    for line in text.splitlines():
        if not line.strip():
            if cur:
                out.append("\n".join(cur)); cur = []
            continue
        # A TABLE ROW is one claim. Without this the palette table -- contiguous
        # lines, no blank line between them -- was a single block holding every
        # token in the pack and every number beside them, so `--danger`'s
        # "(2.8 apart)" bound to `--verify-ink` and reported six failures against
        # six correct rows.
        if line.lstrip().startswith("|"):
            if cur:
                out.append("\n".join(cur)); cur = []
            out.append(line)
            continue
        if re.match(r"\s*[-*]\s", line) and cur:
            out.append("\n".join(cur)); cur = []
        cur.append(line)
    if cur:
        out.append("\n".join(cur))
    return out


def _sentences(block: str) -> list[str]:
    """A number binds to the pair named in ITS OWN sentence, not the block's.

    `cyclorama` writes two pairs and three numbers in one bullet, separated by a
    semicolon: "`--good` and `--danger` separate by 14.0 ... ; `--warning` and
    `--danger` by 14.8." Binding at block level gave `--warning`/`--danger` the
    figure 14.0 and called the pack wrong.
    """
    return [s for s in re.split(r"(?<=[.;])\s+", block) if s.strip()]


def _declared_sets(css_text: str, pack_text: str) -> list[tuple[str, dict[str, str]]]:
    """Every peer group the pack itself declares, as (why, {label: token}).

    A state map contributes one group per contiguous run of arrows -- two maps in
    one file are two groups, because a state of one thing is not a peer of a state
    of another.
    """
    groups: list[tuple[str, dict[str, str]]] = []
    run: dict[str, str] = {}
    for line in css_text.splitlines():
        found = STATE_MAP.findall(line)
        if found:
            for label, token in found:
                run[label.strip()] = token
        elif run and not line.strip().startswith(("*", "/*")) and "-->" not in line:
            if len(run) >= 2:
                groups.append(("the state map in the token layer", dict(run)))
            run = {}
    if len(run) >= 2:
        groups.append(("the state map in the token layer", dict(run)))

    # A distinctness claim: the subject is the first token on the line, the object
    # is the one the phrase names.
    for source, text in (("styles", pack_text), ("tokens", css_text)):
        for line in text.splitlines():
            m = DISTINCT_CLAIM.search(line)
            if not m:
                continue
            names = [n for n in TOKEN_ON_LINE.findall(line) if n != m.group(1)]
            if not names:
                continue
            groups.append((f"a distinctness claim in the {source} file",
                           {names[0]: names[0], m.group(1): m.group(1)}))
        # A DISCLOSURE also declares the pair. Correcting a false "distinct from"
        # into an honest "one hue family" removed the only thing that made the
        # pair observable: the collision was documented and gated by nothing, so
        # a later re-step would have made the prose wrong with the gate green.
        # The sentence that admits the collision is therefore what keeps it
        # measured.
        for block in _blocks(text):
            if not NOT_BY_HUE.search(block):
                continue
            names = list(dict.fromkeys(TOKEN_ON_LINE.findall(block)))
            if len(names) < 2:
                continue
            groups.append((f"the pack's own disclosure in the {source} file",
                           {n: n for n in names}))
    return groups


def _check_stated_delta(stem, a, b, maps, pack_text, css_text) -> None:
    """A distance the pack states about a pair it names is computed, not read.

    The disclosure is the pack's answer to a hard-floor collision, so the number
    in it carries the whole argument: "one hue family, 2.8 apart" is only an
    honest answer while 2.8 is what the values produce. Checked against every
    theme, because a pack states the light-theme figure and often the dark one on
    the same line.
    """
    for src in (pack_text, css_text):
        for block in _blocks(src):
            if not NOT_BY_HUE.search(block):
                continue
            named = set(TOKEN_ON_LINE.findall(block))
            if a not in named or b not in named:
                continue
            wanted: list[tuple[float, str]] = []
            for sentence in _sentences(block):
                named_here = set(TOKEN_ON_LINE.findall(sentence))
                if a not in named_here or b not in named_here:
                    continue
                figures = _figures(sentence)
                # EXACTLY TWO tokens, or the number's owner is a guess. A
                # sentence naming three statuses and three figures -- which is
                # how `pigeonhole`, `paperclip` and `maquette` write theirs --
                # gave every figure to every pair and reported six failures
                # against six correct sentences. The pool that cannot fail and
                # the pool that fails wrongly are the same mistake in two
                # directions; the answer both times is to check only what the
                # document actually pins down.
                if len(named_here) != 2:
                    _tally["delta_unbound"] += len(figures)
                    continue
                wanted += figures
            for want, what in wanted:
                got = []
                for _lbl, solids, _f in maps:
                    if a not in solids or b not in solids:
                        continue
                    if what == "full colour":
                        got.append(delta(solids[a], solids[b]))
                    else:
                        got.append(delta(simulate(solids[a], what),
                                         simulate(solids[b], what)))
                if not got:
                    continue
                check(
                    any(abs(g - want) <= DELTA_TOL for g in got),
                    f"styles/{stem}.md: the disclosure for {a}/{b} states {want} "
                    f"{what} and the token layer produces "
                    f"{', '.join(f'{g:.1f}' for g in sorted({round(x, 1) for x in got}))} "
                    f"-- the number that answers a hard-floor collision is the "
                    f"whole answer, so it is computed like one",
                )


def validate_declared_semantic_sets(css: Path) -> None:
    stem = css.stem
    text = css.read_text(encoding="utf-8")
    maps = _theme_maps(text)
    if not maps:
        return
    pack_md = PACKS / f"{stem}.md"
    pack_text = pack_md.read_text(encoding="utf-8") if pack_md.is_file() else ""
    groups = _declared_sets(text, pack_text)
    if not groups:
        return
    # The file-wide phrase excuses the SOFT floor only, exactly as it does for the
    # status peers. Below the hard floor a boilerplate sentence is not an answer:
    # the pack has to name THIS pair and say what separates it, on one line. That
    # is the difference between a pack disclosing a property of its reference and
    # a pack adding a phrase to turn a gate green.
    soft_excused = bool(NOT_BY_HUE.search(pack_text) or NOT_BY_HUE.search(text))

    def excused_pair(a: str, b: str) -> bool:
        # Tokens compared EXACTLY, never as substrings: `--witness` is a prefix of
        # `--witness-ink`, so a line excusing one pair would silently excuse the
        # other -- a gate passing on a substring is the defect this file hunts.
        for src in (pack_text, text):
            for block in _blocks(src):
                if not NOT_BY_HUE.search(block):
                    continue
                named = set(TOKEN_ON_LINE.findall(block))
                if a in named and b in named:
                    return True
        return False

    # One pair, one verdict. `field-notes` writes its distinctness claim in the
    # pack file AND in the token layer, which is good practice and was reported
    # as two identical failures per theme.
    seen: set[tuple[str, str, str]] = set()
    # The stated figures are a property of the SENTENCE, not of a theme, and the
    # check already looks at every theme itself -- running it per theme reported
    # each wrong number twice.
    figured: set[tuple[str, str]] = set()

    for why, group in groups:
        by_token = {}
        for lbl, token in group.items():
            by_token.setdefault(token, lbl)
        if len(by_token) < 2:
            continue
        for label, solids, _field in maps:
            present = [(tok, by_token[tok]) for tok in by_token if tok in solids]
            if len(present) < 2:
                continue
            for i, (ta, la) in enumerate(present):
                for tb, lb in present[i + 1:]:
                    key = (label, *sorted((ta, tb)))
                    if key in seen:
                        continue
                    d = delta(solids[ta], solids[tb])
                    worst = min(
                        (delta(simulate(solids[ta], k), simulate(solids[tb], k)), k)
                        for k in CVD_MATRICES)
                    if d >= DELTA_HARD and worst[0] >= DELTA_CVD:
                        continue
                    seen.add(key)
                    states = "" if la == ta else f" ({la} vs {lb})"
                    where = f"styles/{stem}.md [{label}]"
                    measured = (f"{d:.1f} apart at full colour and {worst[0]:.1f} "
                                f"under {worst[1]}")
                    if d < DELTA_HARD:
                        check(
                            excused_pair(ta, tb),
                            f"{where}: {ta} and {tb}{states} are {measured} — below "
                            f"the hard floor of {DELTA_HARD}, and they are peers "
                            f"because of {why}. A hue read off a reference may not be "
                            f"re-stepped, so the pack must name THIS pair and say what "
                            f"separates it instead of the hue; a file-wide phrase does "
                            f"not reach a hard-floor pair, and a claim that they are "
                            f"distinct when they are not is itself the defect",
                        )
                    else:
                        check(
                            soft_excused or excused_pair(ta, tb),
                            f"{where}: {ta} and {tb}{states} separate by {measured} "
                            f"(floors {DELTA_HARD}/{DELTA_CVD}) and they are peers "
                            f"because of {why}, and the pack states no secondary "
                            f"encoding — declare what carries the difference",
                        )
                    if excused_pair(ta, tb) or (d >= DELTA_HARD and soft_excused):
                        notes.append(
                            f"  {stem} [{label}]: {ta}/{tb} tight ({measured}) — "
                            f"the pack names what separates them")
                    fig_key = tuple(sorted((ta, tb)))
                    if fig_key not in figured:
                        figured.add(fig_key)
                        _check_stated_delta(stem, ta, tb, maps, pack_text, text)


# ------------------------------------- a fill the pack asks you to COMPOSITE
#
# `validate_stated_ratios` reads a ratio the document states. A Components row
# often states no ratio at all: it states an INSTRUCTION -- "`--surface-2` fill at
# 4% ink, `--ink` at 50%" -- and nothing computed the result. `scoreboard`'s
# secondary button shipped a 10-12px/600 label at **3.2:1** that way, below AA,
# and every gate was green over it because there was no number to check.
#
# Measured before it was built: 44 lines in the library put a token beside a
# percentage, and almost all of them are washes, hairlines, borders and gradient
# stops rather than text on a composited fill. TWO rows state a composite fill
# AND a text size -- `scoreboard`'s secondary button, which fails, and
# `cyclorama`'s chip at 12.4:1, which passes. One subject of each verdict is what
# makes this a check rather than an assertion; a parser for the other 42 would
# have to guess what carries text, which is the mistake this file records twice.
#
# Compositing is done in sRGB gamma space, because that is where the browser does
# it. The first draft composited the linear values this module carries and got
# 1.88:1 where the browser renders 3.2:1 -- a wrong number in the direction that
# would have failed a correct pack.
COMPOSITE_SPEC = re.compile(
    r"(?:`(--[a-z0-9-]+)`\s+)?(?:fill\s+)?(?:at\s+)?(\d{1,3})\s*%\s*(ink)?"
    r"|`(--[a-z0-9-]+)`\s+at\s+(\d{1,3})\s*%")
# A type size, never a padding. `6px 12px` is padding and `10-12px/600` is type:
# the library always writes a size with its weight or after a face. Reading every
# px on the line made the padding the type size.
TYPE_SIZE = re.compile(r"(\d{1,3})(?:\s*[-–]\s*(\d{1,3}))?\s*px\s*/\s*\d{3}"
                       r"|(?:[Mm]ono|[Ss]ans|[Ss]erif|face)\s+(\d{1,3})\s*px")
LARGE_TEXT_PX = 24.0


def linear_to_srgb(c: float) -> float:
    return c * 12.92 if c <= 0.0031308 else 1.055 * (c ** (1 / 2.4)) - 0.055


def composite(fg, bg, alpha: float):
    """`fg` at `alpha` over `bg`, in the space the browser composites in."""
    f = [linear_to_srgb(x) for x in fg]
    b = [linear_to_srgb(x) for x in bg]
    return tuple(srgb_to_linear(f[i] * alpha + b[i] * (1 - alpha)) for i in range(3))


def _composites(cell: str) -> list[tuple[str | None, float]]:
    """Every `(token, alpha)` the cell asks for, in the order it asks."""
    out = []
    for m in COMPOSITE_SPEC.finditer(cell):
        if m.group(2):
            token, pct = m.group(1), m.group(2)
        else:
            token, pct = m.group(4), m.group(5)
        if pct is None:
            continue
        out.append((token, int(pct) / 100.0))
    return out


def _type_floor(line: str) -> tuple[float, str]:
    sizes = []
    for m in TYPE_SIZE.finditer(line):
        sizes += [float(g) for g in m.groups() if g]
    if not sizes:
        return 4.5, "no size stated, so the body floor applies"
    smallest = min(sizes)
    if smallest >= LARGE_TEXT_PX:
        return 3.0, f"{smallest:.0f}px is large text"
    return 4.5, f"{smallest:.0f}px"


def validate_composited_fill_contrast(css: Path) -> None:
    stem = css.stem
    pack_md = PACKS / f"{stem}.md"
    if not pack_md.is_file():
        return
    maps = _theme_maps(css.read_text(encoding="utf-8"))
    if not maps:
        return
    for lineno, line in enumerate(pack_md.read_text(encoding="utf-8").splitlines(), 1):
        if not line.startswith("|"):
            continue
        # PER CELL, not per row. A Components row is resting | hover | active |
        # disabled, and reading the whole row made `cyclorama`'s hover fill
        # ("fill → ink at 12%") the text colour of its resting chip: 1.26:1
        # reported against a row that renders at 12.4:1. The type size is stated
        # once for the row, so that half is read from the row.
        cells = [c for c in line.strip().strip("|").split("|")]
        floor, why = _type_floor(line)
        if "body floor" in why:
            # No type size on the row: it is a wash, a border or a hairline, not
            # text on a fill. Counted so the gap is visible, never guessed at.
            if any(_composites(c) for c in cells):
                _tally["composite_unsized"] += 1
            continue
        for cell in cells:
            specs = _composites(cell)
            if not specs:
                continue
            _one_composited_cell(stem, lineno, maps, specs, floor, why)


def _one_composited_cell(stem, lineno, maps, specs, floor, why) -> None:
        for label, solids, _field in maps:
            base_name = pick(solids, FIELD_TOKENS)
            if not base_name:
                continue
            ink_name = pick(solids, INK_TOKENS)
            if not ink_name:
                continue
            fill_token, fill_alpha = specs[0]
            base = solids.get(fill_token or base_name)
            if base is None:
                continue
            fill = composite(solids[ink_name], base, fill_alpha)
            if len(specs) > 1:
                text_token, text_alpha = specs[1]
                src = solids.get(text_token or ink_name)
                if src is None:
                    continue
                text = composite(src, fill, text_alpha)
                described = (f"{text_token or ink_name} at {text_alpha:.0%} on "
                             f"{fill_token or base_name} at {fill_alpha:.0%} ink")
            else:
                text = solids[ink_name]
                described = (f"{ink_name} on {fill_token or base_name} at "
                             f"{fill_alpha:.0%} ink")
            got = contrast(text, fill)
            check(
                got >= floor,
                f"styles/{stem}.md:{lineno} [{label}]: {described} composites to "
                f"{got:.2f}:1, below {floor} for {why}. The row states an "
                f"instruction rather than a ratio, so nothing computed the "
                f"result — composite it or name a token that passes",
            )
            notes.append(f"  {stem} [{label}]: {described} = {got:.2f}:1 (floor {floor})")



# ------------------------------------- the pair a Components row PRESCRIBES
#
# A ratio is checked when the document states one. A Components row usually
# states none: it prescribes a pair -- "`--accent` fill, `--on-accent` label" --
# and then its hover and active cells REPLACE one half of it. `contrast(label,
# fill)` is derivable at every state and nothing derived it, which is how
# `instrument-console` shipped a pressed label at 3.06:1 (B-039): the press
# swapped the fill to `--accent-dim` and the label stayed.
#
# Measured before it was written: 11 rows across 7 packs name BOTH a fill and a
# label, and they carry 8 state swaps between them. The convention is the
# library's own -- "`--x` fill, `--y` label", "fill -> `--z`" -- and a row that
# does not use it is skipped and counted rather than parsed by guess. This check
# could NOT have caught B-039: `instrument-console` is a core-contract pack with
# no Components table at all, which is also why the defect survived there.
# Both halves, in the two phrasings the library actually uses. The narrow pair
# ("`--x` fill, `--y` label") covers 11 rows; adding "on `--x` fill" and
# "in `--y`" brings it to 13 and both additions found a defect on their first
# run -- `maquette`'s leader label is cream ON cream at 1.00:1, and `prism` puts
# a `$` prompt in a token its own layer calls "furniture only, never text".
ROW_FILL = re.compile(r"`(--[a-z0-9-]+)`\s+fill\b|\bon\s+`(--[a-z0-9-]+)`\s+fill\b")
ROW_LABEL = re.compile(r"`(--[a-z0-9-]+)`\s+(?:label|text)\b|\bin\s+`(--[a-z0-9-]+)`")
ROW_SWAP = re.compile(r"\b(fill|label|text)\s*(?:→|->)\s*`?(--[a-z0-9-]+)`?")
# A state cell that changes nothing about the pair.
ROW_INHERIT = re.compile(r"^\s*(?:as above|same|none|-|—|–|n/a)?\s*$", re.I)


def validate_prescribed_pairs(css: Path) -> None:
    stem = css.stem
    pack_md = PACKS / f"{stem}.md"
    if not pack_md.is_file():
        return
    maps = _theme_maps(css.read_text(encoding="utf-8"))
    if not maps:
        return
    for lineno, line in enumerate(pack_md.read_text(encoding="utf-8").splitlines(), 1):
        if not line.startswith("|") or line.count("|") < 4:
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 2:
            continue
        resting = cells[1]
        fill_m, label_m = ROW_FILL.search(resting), ROW_LABEL.search(resting)
        if not (fill_m and label_m):
            if ROW_FILL.search(resting) or ROW_LABEL.search(resting):
                # Half a pair is not a pair. Counted, because a row naming a fill
                # and no label is exactly where the next one of these hides.
                _tally["pair_half_stated"] += 1
            continue
        floor, why = _type_floor(line)
        base_fill = fill_m.group(1) or fill_m.group(2)
        base_label = label_m.group(1) or label_m.group(2)
        if base_fill == base_label:
            continue        # one token doing both jobs is a row about a surface
        states = [("resting", base_fill, base_label)]
        for cell, name in zip(cells[2:], ("hover", "active", "disabled", "state 4")):
            if ROW_INHERIT.match(cell):
                continue
            fill, label = base_fill, base_label
            swapped = False
            for what, token in ROW_SWAP.findall(cell):
                swapped = True
                if what == "fill":
                    fill = token
                else:
                    label = token
            if swapped:
                states.append((name, fill, label))
        for theme, solids, _field in maps:
            for name, fill, label in states:
                if fill not in solids or label not in solids:
                    _tally["pair_unresolved"] += 1
                    continue
                got = contrast(solids[label], solids[fill])
                check(
                    got >= floor,
                    f"styles/{stem}.md:{lineno} [{theme}]: the {name} state "
                    f"prescribes {label} on {fill} and that is {got:.2f}:1, "
                    f"below {floor} for {why}. The row states a pair rather than "
                    f"a ratio, so nothing computed it -- swap the label with the "
                    f"fill, or state the number the state renders",
                )
                notes.append(f"  {stem} [{theme}]: {name} {label} on {fill} "
                             f"= {got:.2f}:1 (floor {floor})")



def check_floor(script: str, count: int) -> int:
    """The ratchet. See test/floors.json for why a falling count is a defect."""
    import json as _json
    try:
        floors = _json.loads(FLOORS.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        print(f"FAIL: {FLOORS.name} is missing or unreadable", file=sys.stderr)
        return 1
    floor = floors.get(script)
    if floor is None:
        print(f"FAIL: {FLOORS.name} has no floor for {script}", file=sys.stderr)
        return 1
    if count < floor:
        print(
            f"FAIL: {script} ran {count} checks, below its floor of {floor}. "
            f"Checks do not disappear on their own. If the drop is intended, lower "
            f"the floor in {FLOORS.name} in the same commit, with the reason.",
            file=sys.stderr,
        )
        return 1
    return 0


def main() -> int:
    if "--self-test" in sys.argv[1:]:
        return self_test()
    for arg in sys.argv[1:]:
        # An unknown flag silently running the normal pass is how a suite ends
        # up reporting green for a self-test it never ran.
        print(f"FAIL: unknown argument {arg!r} (expected --self-test or none)", file=sys.stderr)
        return 2
    if not TOKENS.is_dir():
        print(f"FAIL: {TOKENS} is missing", file=sys.stderr)
        return 1
    files = sorted(TOKENS.glob("*.css"))
    check(len(files) >= 2, "styles/tokens: expected at least two token layers")
    for css in files:
        validate_pack(css)
        validate_status_on_field(css)
        validate_line_surface_collision(css)
        validate_declared_semantic_sets(css)
        validate_composited_fill_contrast(css)
        validate_prescribed_pairs(css)
        validate_stated_ratios(css)
    for line in notes:
        print(line)
    print(f"  {stated_ratio_report()}")
    # A number nobody can act on is a number nobody acts on. Each of these is a
    # claim whose partner is written down and whose arithmetic still cannot run.
    for line in _unresolved:
        print(f"    unpairable  {line}")
    print(f"  {declared_set_report()}")
    if failures:
        for f in failures:
            print(f"FAIL: {f}")
        print(f"{len(failures)} failure(s) in {checks} checks", file=sys.stderr)
        return 1
    rc = check_floor("validate_palette.py", checks)
    if rc:
        return rc
    # The coverage ratchet runs AFTER the failures, because a red run's tally is
    # about a tree nobody has fixed yet; it runs BEFORE the OK line, because a
    # coverage regression is not an OK.
    import json as _j
    slipped = check_ratio_coverage(_j.loads(FLOORS.read_text(encoding="utf-8")))
    if slipped:
        for s in slipped:
            print(f"FAIL: {s}", file=sys.stderr)
        return 1
    print(f"OK ({checks} checks)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
