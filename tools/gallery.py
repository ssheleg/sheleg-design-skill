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
    m = re.fullmatch(r"#([0-9a-fA-F]{3}|[0-9a-fA-F]{6})", (colour or "").strip())
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


def collect() -> list[dict]:
    skill = (STYLES.parent / "SKILL.md").read_text()
    table = {
        m.group(1): (m.group(2).strip(), m.group(3).strip())
        for m in re.finditer(r"^\| \[`([a-z-]+)`\]\([^)]+\) \| (.*?) \| (.*?) \|$", skill, re.M)
    }
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
            "for": re.sub(r"[*`]", "", choose),
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


def card(p: dict) -> str:
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
    hay = " ".join([p["name"], p["look"], p["for"], p["host"]]).lower()
    return f'''<article class="card{' flag' if p["flag"] else ''}" data-name="{esc(p["name"])}"
   data-dark="{str(p["dark"]).lower()}" data-ceiling="{esc(p["ceiling"])}"
   data-flag="{str(p["flag"]).lower()}" data-hay="{esc(hay)}">
  <header class="chead">
    <h2>{esc(p["name"])}{' <span class="star">new</span>' if p["flag"] else ''}</h2>
    <div class="meta"><code>{esc(p["host"])}</code> &middot; {esc(p["added"])}</div>
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


CSS = """
* { box-sizing: border-box; }
body { margin:0; background:#0e0f11; color:#e8e9ec;
  font:400 15px/1.5 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif; }
header.top { padding:40px 32px 24px; max-width:1600px; margin:0 auto; }
h1 { margin:0 0 8px; font-size:30px; font-weight:600; letter-spacing:-.02em; }
.sub { color:#9a9ca4; max-width:78ch; }
.sub b { color:#e8e9ec; font-weight:600; }
.sub code { color:#c8cad0; }
.controls { position:sticky; top:0; z-index:5; background:#0e0f11ee;
  backdrop-filter:blur(8px); border-bottom:1px solid #24262b; padding:14px 32px; }
.controls .inner { max-width:1600px; margin:0 auto; display:flex; gap:10px; flex-wrap:wrap; align-items:center; }
input[type=search] { background:#191b1f; border:1px solid #2b2e34; color:#e8e9ec;
  border-radius:8px; padding:8px 12px; min-width:260px; font-size:14px; }
button { background:#191b1f; border:1px solid #2b2e34; color:#c8cad0; border-radius:999px;
  padding:6px 14px; font-size:13px; cursor:pointer; }
button[aria-pressed=true] { background:#e8e9ec; color:#0e0f11; border-color:#e8e9ec; }
.count { color:#7d8088; font-size:13px; margin-left:auto; }
main { max-width:1600px; margin:0 auto; padding:24px 32px 80px;
  display:grid; grid-template-columns:repeat(auto-fill,minmax(330px,1fr)); gap:20px; }
.card { border:1px solid #24262b; border-radius:14px; overflow:hidden; background:#141519;
  display:flex; flex-direction:column; }
.card.flag { border-color:#4a7dff; box-shadow:0 0 0 1px #4a7dff55; }
.chead { padding:14px 16px 10px; display:flex; justify-content:space-between; align-items:baseline; gap:8px; }
.chead h2 { margin:0; font-size:17px; font-weight:600; letter-spacing:-.01em; }
.star { font-size:10px; text-transform:uppercase; letter-spacing:.1em; color:#4a7dff;
  border:1px solid #4a7dff; border-radius:4px; padding:1px 5px; vertical-align:2px; }
.meta { color:#7d8088; font-size:12px; white-space:nowrap; }
.meta code { color:#9a9ca4; }
.specimen { margin:0 16px; padding:18px; position:relative; min-height:132px;
  display:flex; flex-direction:column; justify-content:center; gap:2px; overflow:hidden; }
.sp-display { font-size:44px; line-height:1; letter-spacing:-.03em; }
.sp-line { font-size:15px; opacity:.85; }
.sp-small { font-size:11px; opacity:.6; letter-spacing:.04em; margin-top:4px; }
.sp-dot { position:absolute; right:16px; top:16px; width:26px; height:26px; border-radius:999px; }
.swatches { padding:12px 16px 4px; display:grid; gap:4px; }
.sw { display:flex; align-items:center; gap:8px; font-size:11px; color:#9a9ca4; min-width:0; }
.sw b { width:52px; color:#c8cad0; font-weight:500; flex:none; }
.sw code { color:#7d8088; overflow:hidden; text-overflow:ellipsis; white-space:nowrap; }
.chip { width:16px; height:16px; border-radius:4px; border:1px solid #ffffff22; flex:none;
  background-size:cover; }
.badges { padding:8px 16px; display:flex; gap:5px; flex-wrap:wrap; }
.b { font-size:10.5px; color:#9a9ca4; border:1px solid #2b2e34; border-radius:999px; padding:2px 8px; }
.b-new { color:#4a7dff; border-color:#4a7dff66; }
.b-core { color:#ffb86b; border-color:#ffb86b55; }
.look { margin:4px 16px 0; font-size:12.5px; color:#9a9ca4; }
.forr { margin:8px 16px 16px; font-size:12.5px; color:#c8cad0; }
.forr b { color:#7d8088; font-weight:500; }
footer { max-width:1600px; margin:0 auto; padding:0 32px 60px; color:#7d8088; font-size:12.5px; }
@media (max-width:600px) { header.top, .controls, main, footer { padding-left:16px; padding-right:16px; } }
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


def render(packs: list[dict]) -> str:
    dark = sum(1 for p in packs if p["dark"])
    flagged = sum(1 for p in packs if p["flag"])
    core = sum(1 for p in packs if p["contract"].startswith("core"))
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>SHELEG style packs &mdash; {len(packs)} measured designs</title>
<style>{CSS}</style></head><body>
<header class="top">
  <h1>SHELEG style packs &mdash; {len(packs)} measured designs</h1>
  <p class="sub">Every card renders in <b>its own token layer</b>, read out of
  <code>styles/tokens/&lt;pack&gt;.css</code>: the swatches, the radius, the accent and the type
  stack are the pack's real values rather than a description of them, so a card that looks wrong
  is a pack that <i>is</i> wrong. Each pack was extracted from a named production site and every
  colour carries a measured contrast ratio.</p>
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
{chr(10).join(card(p) for p in packs)}
</main>
<footer>Generated by <code>tools/gallery.py</code> from <code>{esc(git("rev-parse", "--short", "HEAD"))}</code>
 &middot; each pack names its source in its own <code>Origin:</code> line.</footer>
<script>{JS}</script>
</body></html>"""


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(ROOT / "gallery.html"))
    args = ap.parse_args()
    packs = collect()
    stray = [p["name"] for p in packs if p["unresolved"]]
    if stray:
        print(f"unresolved var() in: {', '.join(stray)}", file=sys.stderr)
        return 1
    out = pathlib.Path(args.out)
    out.write_text(render(packs))
    print(f"{out} — {len(packs)} packs, {out.stat().st_size:,} bytes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
