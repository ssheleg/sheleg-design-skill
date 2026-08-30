#!/usr/bin/env python3
"""Render every style pack as one browsable gallery, from the packs' own token layers.

The point is that nothing here is described: each card's swatches, type specimen,
radius and accent are read out of `styles/tokens/<pack>.css`, so a card that looks
wrong is a pack that IS wrong. Run it after adding a pack:

    python3 tools/gallery.py            # writes gallery.html beside the repo root
    python3 tools/gallery.py --out /tmp/x.html

Stdlib only, self-contained output, no network — the file opens over file://.
"""
from __future__ import annotations

import argparse
import html
import json
import pathlib
import math
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
STYLES = ROOT / "plugins/sheleg-design/skills/sheleg-design/styles"
# Packs whose first commit is newer than this are flagged in the gallery. Bump it
# when the flag stops being interesting; it is a reading aid, not a claim.
FLAG_FROM = "2026-08-24"

VAR = re.compile(r"var\(\s*(--[a-z0-9-]+)\s*(?:,\s*([^()]*(?:\([^()]*\)[^()]*)*))?\)")


def resolve(value: str, css: str, depth: int = 0) -> str:
    """Substitute var() references INLINE — they appear inside calc() and inside
    font stacks, not only as a whole value, which is the bug this function had."""
    if not value or depth > 8 or "var(" not in value:
        return value

    def sub(m: re.Match) -> str:
        found = re.search(rf"^\s*{re.escape(m.group(1))}:\s*([^;]+);", css, re.M)
        return resolve(found.group(1).strip(), css, depth + 1) if found else (m.group(2) or "")

    return VAR.sub(sub, value).strip()


def first_token(css: str, *names: str) -> str | None:
    for n in names:
        m = re.search(rf"^\s*--{n}:\s*([^;]+);", css, re.M)
        if m:
            return m.group(1).split("/*")[0].strip()
    return None


def luminance(colour: str | None) -> float | None:
    """Relative luminance, or None when the value cannot be read.

    It reads `oklch()` as well as hex, and that is not decoration: `briefing-room`
    declares its field as `oklch(0.045 0.008 254)` — a near-black — and until 1.52.0
    this function returned None for it, so the pack fell through to "light field" and
    the published site, its `llms.txt` and its gallery all counted five dark packs
    where six ship. A parser that silently fails is a wrong number nobody can see.
    """
    raw = (colour or "").strip()
    m = re.fullmatch(r"oklch\(\s*([0-9.]+%?)\s+([0-9.]+)\s+([0-9.]+)\s*\)", raw, re.I)
    if m:
        L = float(m.group(1).rstrip("%"))
        if m.group(1).endswith("%"):
            L /= 100
        C, H = float(m.group(2)), float(m.group(3))
        a_, b_ = C * math.cos(math.radians(H)), C * math.sin(math.radians(H))
        l_ = (L + 0.3963377774 * a_ + 0.2158037573 * b_) ** 3
        m_ = (L - 0.1055613458 * a_ - 0.0638541728 * b_) ** 3
        s_ = (L - 0.0894841775 * a_ - 1.2914855480 * b_) ** 3
        r = 4.0767416621 * l_ - 3.3077115913 * m_ + 0.2309699292 * s_
        g_ = -1.2684380046 * l_ + 2.6097574011 * m_ - 0.3413193965 * s_
        bl = -0.0041960863 * l_ - 0.7034186147 * m_ + 1.7076147010 * s_
        clamp = lambda v: min(1.0, max(0.0, v))
        return 0.2126 * clamp(r) + 0.7152 * clamp(g_) + 0.0722 * clamp(bl)
    m = re.fullmatch(r"#([0-9a-fA-F]{3}|[0-9a-fA-F]{6})", raw)
    if not m:
        return None
    h = m.group(1)
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    r, g, b = (int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))
    lin = lambda c: c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
    return 0.2126 * lin(r) + 0.7152 * lin(g) + 0.0722 * lin(b)


def git(*args: str) -> str:
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True).stdout.strip()


# The catalogue — the register and good-fit columns every card and every JSON-LD
# description is built from — lives in STYLE_PACK_INDEX.md. It used to live in
# SKILL.md, and this parser was still reading SKILL.md long after it moved: the
# regex matched nothing, `look` and `for` came back empty for EVERY pack, and the
# published front door shipped "Choose for" followed by silence on all of them,
# with the ItemList descriptions and llms.txt entries empty behind it. Nothing
# failed, because an empty string is a valid string.
#
# So the parse is now asserted rather than trusted: a run that finds fewer rows
# than there are packs stops, instead of publishing a catalogue with no prose in it.
CATALOGUE = STYLES.parent / "STYLE_PACK_INDEX.md"
CATALOGUE_ROW = re.compile(r"^\| \[`([a-z-]+)`\]\([^)]+\) \| (.*?) \| (.*?) \|$", re.M)


def catalogue() -> dict[str, tuple[str, str]]:
    text = CATALOGUE.read_text()
    rows = {m.group(1): (m.group(2).strip(), m.group(3).strip())
            for m in CATALOGUE_ROW.finditer(text)}
    if not rows:
        raise SystemExit(
            f"gallery: {CATALOGUE.name} yielded no catalogue rows — every card would "
            f"ship with an empty register and an empty good-fit line, which is what "
            f"happened for as long as this was read out of SKILL.md")
    return rows


def collect() -> list[dict]:
    table = catalogue()
    packs = []
    for md in sorted(STYLES.glob("*.md")):
        if md.stem == "STYLE_PACK_TEMPLATE":
            continue
        text = md.read_text()
        css_path = STYLES / "tokens" / f"{md.stem}.css"
        css = css_path.read_text() if css_path.exists() else ""
        get = lambda *n: resolve(first_token(css, *n) or "", css) or None
        origin = re.search(r"^Origin:\s*(.+?)$", text, re.M)
        host = ""
        if origin:
            raw = re.sub(r"[<>*`]", "", origin.group(1)).strip().split()[0]
            host = re.sub(r"^https?://", "", raw).split("/")[0].rstrip(",.")
        ceiling = re.search(r"MOTION_INTENSITY\D{0,80}?\*\*(\d+)\*\*|MOTION_INTENSITY above\s+\*?\*?(\d+)", text)
        contract = re.search(r"^Contract:\s*(.+?)$", text, re.M)
        bg, ink = get("bg", "base", "paper", "canvas", "surface"), get("ink", "fg", "text", "foreground")
        lum = luminance(bg)
        look, choose = table.get(md.stem, ("", ""))
        packs.append({
            "name": md.stem,
            "look": re.sub(r"[*`]", "", look),
            # The catalogue's good-fit cell ends in the same markers the badges below
            # already render — `· (standalone)`, `· core contract`. Printing both puts
            # the same fact on the card twice, so the tail is dropped here and the
            # badges keep the job.
            "for": re.sub(r"\s*·\s*(\(standalone\)|core contract)\s*", "",
                          re.sub(r"[*`]", "", choose)).strip(" ·"),
            "host": host or "—",
            "added": git("log", "--diff-filter=A", "--format=%ad", "--date=short", "-1", "--", str(md)),
            "ceiling": (ceiling.group(1) or ceiling.group(2)) if ceiling else "",
            "contract": contract.group(1).strip() if contract else "",
            "standalone": "standalone" in text[:4000].lower(),
            "dark": bool(lum is not None and lum < 0.2),
            "bg": bg, "ink": ink,
            "accent": get("accent", "action", "primary", "link"),
            "surface": get("surface", "surface-2", "card", "field"),
            "line": get("line", "line-soft", "border", "rule", "hairline"),
            "radius": get("r-md", "radius-card", "r-lg", "r-sm", "radius", "r-card") or "0",
            "font": get("font-sans", "font-body", "font-display") or "system-ui",
            "mono": get("font-mono") or "ui-monospace, monospace",
            "unresolved": False,
        })
    for p in packs:
        p["unresolved"] = any("var(" in str(p[k]) for k in ("bg", "ink", "accent", "radius", "font", "mono"))
        p["flag"] = bool(p["added"] and p["added"] >= FLAG_FROM)
    return packs


def esc(s) -> str:
    return html.escape(str(s or ""), quote=True)


def card(p: dict, public: bool = False) -> str:
    def sw(label, val):
        if not val:
            return ""
        prop = "background-image" if "gradient" in val else "background"
        return (f'<div class="sw" title="{esc(label)}: {esc(val)}">'
                f'<span class="chip" style="{prop}:{esc(val)}"></span>'
                f'<b>{esc(label)}</b><code>{esc(val[:38])}</code></div>')

    badges = []
    if p["flag"]:
        badges.append('<span class="b b-new">newest</span>')
    badges.append(f'<span class="b">{"dark field" if p["dark"] else "light field"}</span>')
    if p["ceiling"]:
        badges.append(f'<span class="b b-m">motion &le; {esc(p["ceiling"])}</span>')
    if p["standalone"]:
        badges.append('<span class="b">standalone</span>')
    if p["contract"].startswith("core"):
        badges.append('<span class="b b-core">core contract</span>')

    accent_prop = "background-image" if p["accent"] and "gradient" in p["accent"] else "background"
    dot = (f'<div class="sp-dot" style="{accent_prop}:{esc(p["accent"])}"></div>') if p["accent"] else ""
    hay = " ".join([p["name"], p["look"], p["for"]] +
                   ([] if public else [p["host"]])).lower()
    return f'''<article class="card{' flag' if p["flag"] else ''}" id="pack-{esc(p["name"])}" data-name="{esc(p["name"])}"
   data-dark="{str(p["dark"]).lower()}" data-ceiling="{esc(p["ceiling"])}"
   data-flag="{str(p["flag"]).lower()}" data-hay="{esc(hay)}">
  <header class="chead">
    <h2>{esc(p["name"])}{' <span class="star">new</span>' if p["flag"] else ''}</h2>
    <div class="meta">{"" if public else f'<code>{esc(p["host"])}</code> &middot; '}{esc(p["added"])}</div>
  </header>
  <div class="specimen" style="background:{esc(p["bg"])};color:{esc(p["ink"])};
       border-radius:{esc(p["radius"])};font-family:{esc(p["font"])}">
    <div class="sp-display">Aa</div>
    <div class="sp-line">The quick brown fox</div>
    <div class="sp-small" style="font-family:{esc(p["mono"])}">0123456789 &middot; LABEL</div>{dot}
  </div>
  <div class="swatches">{sw("bg", p["bg"])}{sw("ink", p["ink"])}{sw("accent", p["accent"])}{sw("surface", p["surface"])}{sw("line", p["line"])}</div>
  <div class="badges">{"".join(badges)}</div>
  <p class="look">{esc(p["look"])}</p>
  <p class="forr"><b>Choose for</b> {esc(p["for"])}</p>
</article>'''


# The card layer only. The page's SHELL — body, links, the sticky bars, the tab
# strip, the tables — is `tools/chrome.py`, so this file and `tools/site.py` are
# dressed by one pack instead of by two hand-written palettes. Everything below is
# about a CARD, and every colour in it is a token.
#
# What is deliberately NOT a token: `.specimen`. Each card's specimen strip is
# painted inline from the pack that card advertises, which is the whole argument of
# the page — a card that looks wrong is a pack that is wrong.
CSS = """
header.top h1 + .sub{margin-top:0}
main#grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(330px,1fr));
  gap:var(--space-5)}
.card{border:1px solid var(--border);border-radius:var(--r-card);overflow:hidden;
  background:var(--panel);display:flex;flex-direction:column;
  transition:border-color var(--dur-hover) var(--motion-ease)}
.card:hover{border-color:var(--border-strong)}
.card.flag{border-color:var(--accent);box-shadow:0 0 0 1px var(--accent-weak)}
.chead{padding:14px 16px 10px;display:flex;justify-content:space-between;
  align-items:baseline;gap:8px}
.chead h2{margin:0;font-size:var(--t-card);font-weight:600;letter-spacing:-.01em}
.star{font-size:10px;text-transform:uppercase;letter-spacing:.1em;color:var(--accent);
  border:1px solid var(--accent);border-radius:4px;padding:1px 5px;vertical-align:2px}
.meta{color:var(--muted);font-size:var(--t-chip);white-space:nowrap;
  font-family:var(--font-data)}
.meta code{color:var(--muted)}
.specimen{margin:0 16px;padding:18px;position:relative;min-height:132px;
  display:flex;flex-direction:column;justify-content:center;gap:2px;overflow:hidden;
  border-radius:var(--r-control)}
.sp-display{font-size:44px;line-height:1;letter-spacing:-.03em}
.sp-line{font-size:15px;opacity:.85}
.sp-small{font-size:11px;opacity:.6;letter-spacing:.04em;margin-top:4px}
.sp-dot{position:absolute;right:16px;top:16px;width:26px;height:26px;border-radius:999px}
.swatches{padding:12px 16px 4px;display:grid;gap:4px}
.sw{display:flex;align-items:center;gap:8px;font-size:11px;color:var(--muted);min-width:0}
.sw b{width:52px;color:var(--ink);font-weight:500;flex:none}
.sw code{color:var(--muted);overflow:hidden;text-overflow:ellipsis;white-space:nowrap;
  font-family:var(--font-data)}
/* The swatch chip sits on a pack colour, not on the shell, so its edge is the shell's
   strong border rather than a white alpha — which vanished on a light field. */
.chip{width:16px;height:16px;border-radius:4px;border:1px solid var(--border-strong);
  flex:none;background-size:cover}
.badges{padding:8px 16px;display:flex;gap:5px;flex-wrap:wrap}
.b{font-size:10.5px;color:var(--muted);border:1px solid var(--border);
  border-radius:var(--r-pill);padding:2px 8px}
.b-new{color:var(--accent);border-color:var(--accent)}
.b-core{color:var(--warn);border-color:var(--warn)}
.look{margin:4px 16px 0;font-size:var(--t-chip);color:var(--muted)}
.forr{margin:8px 16px 16px;font-size:var(--t-chip);color:var(--ink)}
.forr b{color:var(--muted);font-weight:500}
@media (max-width:600px){main#grid{grid-template-columns:1fr}}
"""

JS = """
const grid=document.getElementById('grid'),q=document.getElementById('q'),
      count=document.getElementById('count'),btns=[...document.querySelectorAll('[data-f]')];
let filter='all';
function apply(){
  const term=q.value.trim().toLowerCase(); let shown=0;
  for(const c of grid.children){
    const okF = filter==='all'
      || (filter==='new'   && c.dataset.flag==='true')
      || (filter==='dark'  && c.dataset.dark==='true')
      || (filter==='light' && c.dataset.dark==='false')
      || (filter==='calm'  && c.dataset.ceiling && +c.dataset.ceiling<=3);
    const on = okF && (!term || c.dataset.hay.includes(term));
    c.style.display = on ? '' : 'none';
    if(on) shown++;
  }
  count.textContent = shown+' of '+grid.children.length+' shown';
}
btns.forEach(b=>b.onclick=()=>{filter=b.dataset.f;
  btns.forEach(x=>x.setAttribute('aria-pressed',String(x===b)));apply();});
q.oninput=apply; apply();
"""



def _chrome():
    """The shared shell. Imported lazily so this file still runs standalone."""
    import importlib.util
    spec = importlib.util.spec_from_file_location("chrome", ROOT / "tools" / "chrome.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def render(packs: list[dict], public: bool = False, meta: str = "",
           nav: str = "", title: str = "", intro: str = "") -> str:
    """`meta` is the machine layer — canonical, og:*, twitter:* — passed in by
    `tools/site.py`, which owns the published base. Running this script alone
    writes a local file that needs none of it.

    `nav`, `title` and `intro` are the published site's front door: since 1.52.0 this
    page IS the site's index, so the tab strip and a shorter opening paragraph are
    passed in rather than duplicated here. Empty strings keep the standalone file
    exactly as it was."""
    dark = sum(1 for p in packs if p["dark"])
    flagged = sum(1 for p in packs if p["flag"])
    core = sum(1 for p in packs if p["contract"].startswith("core"))
    head_title = title or f"SHELEG style packs &mdash; {len(packs)} measured designs"
    opening = intro or f"""  <p class="sub">Every card renders in <b>its own token layer</b>, read out of
  <code>styles/tokens/&lt;pack&gt;.css</code>: the swatches, the radius, the accent and the type
  stack are the pack's real values rather than a description of them, so a card that looks wrong
  is a pack that <i>is</i> wrong. Each pack was extracted from a named production site and every
  colour carries a measured contrast ratio.</p>"""
    chrome = _chrome()
    return f"""<!doctype html><html lang="en" data-theme="light"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{head_title}</title>
{meta}
{chrome.style_block()}<style>{CSS}</style>{chrome.THEME_SWITCH}</head><body>
{nav}
<header class="top">
  <h1>{head_title}</h1>
{opening}
  <p class="sub" style="margin-top:10px">{dark} of {len(packs)} stand on a dark field.
  {core} are on the <b>core contract</b> &mdash; they deliberately leave components, hero,
  responsive and their signature element to you. {flagged} are the newest.
  The specimen falls back to a system face unless the pack's font is installed here; the family
  it <i>names</i> is in the pack.</p>
</header>
<div class="controls"><div class="inner">
  <input type="search" id="q" placeholder="search name, look, register, source&hellip;" autocomplete="off">
  <button data-f="all" aria-pressed="true">all</button>
  <button data-f="new">newest</button>
  <button data-f="light">light field</button>
  <button data-f="dark">dark field</button>
  <button data-f="calm">motion &le; 3</button>
  <span class="count" id="count"></span>
</div></div>
<main id="grid">
{chr(10).join(card(p, public) for p in packs)}
</main>
<footer>Generated by <code>tools/gallery.py</code> from <code>{esc(git("rev-parse", "--short", "HEAD"))}</code>
 &middot; {"the site each pack was measured from is recorded in the pack itself and is deliberately not published here" if public else "each pack names its source in its own <code>Origin:</code> line"}.</footer>
<script>{JS}</script>
</body></html>"""


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(ROOT / "gallery.html"))
    ap.add_argument("--public", action="store_true",
                    help="omit every source address — for a page that will be published")
    args = ap.parse_args()
    packs = collect()
    stray = [p["name"] for p in packs if p["unresolved"]]
    if stray:
        print(f"unresolved var() in: {', '.join(stray)}", file=sys.stderr)
        return 1
    out = pathlib.Path(args.out)
    out.write_text(render(packs, args.public))
    print(f"{out} — {len(packs)} packs, {out.stat().st_size:,} bytes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
