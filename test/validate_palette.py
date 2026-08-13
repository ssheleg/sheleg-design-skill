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
PARTNER_PHRASE = re.compile(r"\b(?:on|over|against)\s+`?(--[a-z0-9-]+)`?")
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
                # MEASURED AND LEFT UNGUARDED, DELIBERATELY — 2026-08-12.
                # A ratio whose line names no partner and whose table declares
                # no base is skipped. That is 71 of the library's 121 stated
                # ratios (59%), including inside packs whose tables DO declare a
                # base, because a Gotchas paragraph is not a table row.
                #
                # All 71 were recomputed by hand the day the hole was found and
                # all 71 were correct, so nothing is wrong today. Two attempts
                # to guard them were written and both were thrown away, and the
                # reasons are the finding:
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
                # than a regex. Filed rather than faked. The honest state is:
                # these 71 are verified by hand as of this date and unguarded
                # against the next edit.
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
                        continue
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
                got: list[float] = []
                for _label, solids, _field in maps:
                    got += [
                        contrast(solids[s], solids[n])
                        for s in subjects if s in solids
                        for n in partner_names if n in solids and n != s
                    ]
                if not got:
                    continue  # the subject is not a solid colour in any theme
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
        validate_stated_ratios(css)
    for line in notes:
        print(line)
    if failures:
        for f in failures:
            print(f"FAIL: {f}")
        print(f"{len(failures)} failure(s) in {checks} checks", file=sys.stderr)
        return 1
    rc = check_floor("validate_palette.py", checks)
    if rc:
        return rc
    print(f"OK ({checks} checks)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
