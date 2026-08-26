#!/usr/bin/env python3
"""Build the public site: the pack gallery, the collection audit, and an index.

Two things make this different from running the generators by hand.

**Sources are stripped, and that is enforced rather than promised.** Every address a
pack was measured from is private: the packs record it, this site does not. The build
computes the set of source hosts from the packs themselves and then greps its own output
for every one of them — if a single host, or a bare brand stem, reaches a page, the
build FAILS. A promise in a docstring is not a guard.

**Nothing generated is committed.** The site is built in CI from the repository, so it
cannot drift from the tokens it claims to show.

    python3 tools/site.py --out _site
"""
from __future__ import annotations

import argparse
import html
import importlib.util
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
# The published base. `ssheleg.github.io/sshlg-skills` 301s to the family's own
# domain, so the back-link below names the destination rather than the redirect.
SITE = "https://ssheleg.github.io/sheleg-design-skill"
FAMILY = "https://skills.sshlg.me/skills/sheleg-design/"


def load(name: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / "tools" / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def esc(s) -> str:
    return html.escape(str(s or ""), quote=True)


def git(*a: str) -> str:
    return subprocess.run(["git", *a], cwd=ROOT, capture_output=True, text=True).stdout.strip()



def page_meta(title: str, desc: str, canon: str) -> str:
    """The machine half of a page: what a crawler and a link preview read."""
    return (f'<meta name="description" content="{esc(desc)}">\n'
            f'<link rel="canonical" href="{esc(canon)}">\n'
            f'<meta property="og:type" content="website">\n'
            f'<meta property="og:title" content="{esc(title)}">\n'
            f'<meta property="og:description" content="{esc(desc)}">\n'
            f'<meta property="og:url" content="{esc(canon)}">\n'
            f'<meta property="og:image" content="{SITE}/og.png">\n'
            f'<meta property="og:image:width" content="1200">\n'
            f'<meta property="og:image:height" content="630">\n'
            f'<meta name="twitter:card" content="summary_large_image">\n'
            f'<meta name="twitter:title" content="{esc(title)}">\n'
            f'<meta name="twitter:description" content="{esc(desc)}">\n'
            f'<meta name="twitter:image" content="{SITE}/og.png">')


# ---------------------------------------------------------------- the leak guard
STOP = {"a", "the", "and", "of", "one", "its", "com", "www", "site", "page", "production"}


def source_terms(packs: list[dict], audit: list[dict]) -> set[str]:
    """Every host and brand stem that must never reach a published page."""
    terms: set[str] = set()
    for p in packs:
        h = (p.get("host") or "").strip().lower()
        if h and h != "—":
            h = re.sub(r"^\W+|\W+$", "", h)
            if "." in h:
                terms.add(h)
                terms.add(h.replace("www.", ""))
                stem = h.replace("www.", "").split(".")[0]
                if len(stem) > 3 and stem not in STOP:
                    terms.add(stem)
    for a in audit:
        u = (a.get("origin_url") or "").lower()
        m = re.search(r"https?://([^/]+)", u)
        if m:
            host = m.group(1)
            terms.add(host)
            terms.add(host.replace("www.", ""))
            stem = host.replace("www.", "").split(".")[0]
            if len(stem) > 3 and stem not in STOP:
                terms.add(stem)
    return {t for t in terms if len(t) > 3}


def leaks(text: str, terms: set[str], allow: set[str]) -> list[str]:
    """`allow` holds the terms a page may legitimately contain: a PACK NAME. Three packs
    carry their source brand as their own name — recorded in ADR-0001, and deliberately
    not renamed, because a pack name is a public API across four channels. Their names
    therefore cannot be stripped from a page that lists the packs, and this guard found
    all three by refusing to publish until it was told so explicitly."""
    low = text.lower()
    return sorted(t for t in terms if t in low and t not in allow)


# ---------------------------------------------------------------- the audit page
def audit_page(rows: list[dict], stamp: str) -> str:
    def mark(b: bool) -> str:
        return '<span class="y">yes</span>' if b else '<span class="n">&mdash;</span>'

    def origin_cell(r: dict) -> str:
        if r["addressable"]:
            live = r.get("live") or ""
            lab = "reachable" if live.startswith(("200", "30")) else (f"HTTP {live}" if live else "recorded")
            return f'<span class="y">address</span> <small>{esc(lab)}</small>'
        if r["anonymised"]:
            return '<span class="o">anonymised</span> <small>at the owner&rsquo;s request</small>'
        if r["recorded_exception"]:
            return '<span class="o">recorded exception</span>'
        return '<span class="n">missing</span>'

    body = "\n".join(
        f'<tr><td><b>{esc(r["name"])}</b></td><td>{esc(r["added"])}</td>'
        f'<td>{esc(r["contract"])}</td><td>{mark(r["read_render"])}</td>'
        f'<td>{mark(r["narrow_measured"])}</td><td>{mark(r["names_which_css"])}</td>'
        f'<td>{mark(r["kit_render_on_record"])}</td><td>{origin_cell(r)}</td></tr>'
        for r in rows)
    n = len(rows)
    reach = sum(1 for r in rows if str(r.get("live", "")).startswith(("200", "30")))
    addr = sum(r["addressable"] for r in rows)
    return f"""{HEAD.format(title="Collection audit &mdash; SHELEG style packs", site=SITE, canon=f"{SITE}/audit.html", desc="How each of the style packs was measured, and what the automated gates cannot see: whether values were read off a rendered page, whether a narrow width was measured, whether the kit was ever rendered.")}
<header class="top">
  <p class="crumb"><a href="./">&larr; index</a></p>
  <h1>Collection audit</h1>
  <p class="sub">What the automated gates cannot see: <b>how</b> each pack was measured.
  The three gates check that a pack is structurally whole, correctly routed and that every
  contrast ratio it states recomputes; none of them can tell you whether the values were
  read off a rendered page or off a stylesheet, whether a narrow width was ever measured,
  or whether the pack&rsquo;s reference kit was ever put in a browser.</p>
  <p class="sub">A dash is not a defect &mdash; several are recorded exceptions carried in the
  packs themselves, and two rules postdate most of the library. It is a queue.</p>
  <p class="sub"><b>{addr} of {n}</b> packs cite an address a reader could open, and
  <b>{reach}</b> of those answered when last probed. The rest carry a written exception
  saying so. <b>The addresses are not published here</b> &mdash; each pack records its own.</p>
</header>
<main class="wide">
<table>
  <thead><tr>
    <th>pack</th><th>added</th><th>contract</th><th>read off the render</th>
    <th>narrow width</th><th>names which CSS</th><th>kit rendered</th><th>origin</th>
  </tr></thead>
  <tbody>{body}</tbody>
</table>
<section class="notes">
  <h2>What each column means</h2>
  <dl>
    <dt>read off the render</dt><dd>Values taken from computed styles on the live page
      rather than from its stylesheet. A declared token can be one nothing paints; only the
      render settles it. This became a written rule late, so most of the library predates it.</dd>
    <dt>narrow width</dt><dd>A measurement at a phone width on record, which is what a
      pack&rsquo;s <code>Responsive</code> section is answerable against.</dd>
    <dt>names which CSS</dt><dd>The pack says which stylesheets it counted. It matters only
      where the reference also loads vendor CSS &mdash; counting that yields the framework&rsquo;s
      defaults as the brand&rsquo;s decisions.</dd>
    <dt>kit rendered</dt><dd>The pack&rsquo;s React kit was put in a browser and its computed
      values checked against what the pack claims. Three consecutive releases found a defect
      this way that every gate had passed &mdash; a gate reads structure, not layout.</dd>
    <dt>contract</dt><dd><code>widened</code> answers all thirteen headings.
      <code>core</code> deliberately leaves components, hero, responsive and the signature
      element undecided, and says so.</dd>
  </dl>
</section>
</main>
{foot(stamp)}"""


HEAD = """<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canon}">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{site}/og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{site}/og.png">
<style>
*{{box-sizing:border-box}}
body{{margin:0;background:#0e0f11;color:#e8e9ec;
 font:400 15px/1.55 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif}}
a{{color:#8ab0ff}} a:hover{{color:#b9cdff}}
.top{{max-width:1100px;margin:0 auto;padding:44px 32px 20px}}
.crumb{{margin:0 0 18px;font-size:13px}}
h1{{margin:0 0 12px;font-size:32px;font-weight:600;letter-spacing:-.02em}}
h2{{font-size:19px;font-weight:600;margin:34px 0 12px;letter-spacing:-.01em}}
.sub{{color:#9a9ca4;max-width:80ch;margin:0 0 10px}}
.sub b{{color:#e8e9ec;font-weight:600}} .sub code{{color:#c8cad0}}
main{{max-width:1100px;margin:0 auto;padding:12px 32px 70px}}
main.wide{{max-width:1320px}}
table{{width:100%;border-collapse:collapse;font-size:13px}}
th,td{{text-align:left;padding:8px 10px;border-bottom:1px solid #212328;white-space:nowrap}}
th{{color:#7d8088;font-weight:500;font-size:11.5px;text-transform:uppercase;letter-spacing:.06em;
 position:sticky;top:0;background:#0e0f11}}
td small{{color:#6e7178}}
.y{{color:#5ec98a}} .n{{color:#5a5d64}} .o{{color:#e0a458}}
.notes dl{{display:grid;grid-template-columns:auto 1fr;gap:8px 18px;max-width:96ch;font-size:13.5px}}
.notes dt{{color:#c8cad0;font-weight:500;white-space:nowrap}}
.notes dd{{margin:0;color:#9a9ca4}}
.cards{{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:16px;margin:24px 0}}
.tile{{border:1px solid #24262b;border-radius:14px;padding:20px;background:#141519;
 text-decoration:none;color:inherit;display:block}}
.tile:hover{{border-color:#3a3d45}}
.tile h3{{margin:0 0 6px;font-size:17px;font-weight:600}}
.tile p{{margin:0;color:#9a9ca4;font-size:13px}}
.n-big{{font-size:30px;font-weight:600;letter-spacing:-.02em;display:block;margin-bottom:2px}}
footer{{max-width:1320px;margin:0 auto;padding:0 32px 60px;color:#6e7178;font-size:12.5px}}
@media (max-width:640px){{.top,main,footer{{padding-left:16px;padding-right:16px}}
 table{{display:block;overflow-x:auto}}}}
</style></head><body>"""


def foot(stamp: str) -> str:
    return (f'<footer>Built from <code>{esc(stamp)}</code> by <code>tools/site.py</code>. '
            f'The site each pack was measured from is recorded in the pack and is '
            f'deliberately not published here.</footer>\n</body></html>')



def robots_txt() -> str:
    return (f"User-agent: *\nAllow: /\n\n"
            f"Sitemap: {SITE}/sitemap.xml\n"
            f"LLMs-Txt: {SITE}/llms.txt\n")


def sitemap_xml(stamp_date: str) -> str:
    urls = "".join(
        f"  <url><loc>{SITE}/{p}</loc><lastmod>{stamp_date}</lastmod></url>\n"
        for p in ("", "packs.html", "audit.html"))
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
            f"{urls}</urlset>\n")


def llms_txt(packs: list[dict], rows: list[dict]) -> str:
    """What a machine reading this site should be able to answer without running JS.

    It names no source address — the same guard that checks the pages checks this."""
    n = len(packs)
    dark = sum(1 for p in packs if p["dark"])
    core = sum(1 for r in rows if r["contract"] == "core")
    by_name = {r["name"]: r for r in rows}
    lines = [
        "# SHELEG style packs",
        "",
        f"> {n} style packs for coding agents. Each is a design system extracted from a real",
        "> production interface: colours, type, spacing, radii and motion tokens read off the",
        "> running page, with every contrast ratio recomputed by a gate rather than asserted.",
        "> A pack is a token layer, the rules for spending it, and a list of what it bans.",
        f"> {dark} stand on a dark field; {core} sit on the core contract and deliberately leave",
        "> components, hero, responsive and their signature element undecided.",
        "",
        "The interface each pack was measured from is recorded inside the pack and is",
        "deliberately not published here.",
        "",
        "Install: `npx sheleg-design-skill`",
        "Repository: https://github.com/ssheleg/sheleg-design-skill",
        f"Catalogue: {SITE}/",
        f"Audit: {SITE}/audit.html",
        "Family: https://skills.sshlg.me/",
        "",
        "## Packs",
        "",
    ]
    for p in packs:
        r = by_name.get(p["name"], {})
        field = "dark field" if p["dark"] else "light field"
        ceiling = f", motion ceiling {r['ceiling']}" if r.get("ceiling") else ""
        contract = r.get("contract", "")
        lines.append(f"- **{p['name']}** ({field}{ceiling}, {contract} contract): "
                     f"{p['for'].rstrip('.')}.")
    lines += ["", "## Pages", "",
              f"- [Catalogue]({SITE}/): every pack rendered in its own token layer.",
              f"- [Packs]({SITE}/packs.html): the same, filterable by field, motion ceiling and text.",
              f"- [Collection audit]({SITE}/audit.html): how each pack was measured, and what the "
              f"automated gates cannot see.", ""]
    return "\n".join(lines)


def index_page(packs: list[dict], rows: list[dict], stamp: str) -> str:
    n = len(packs)
    dark = sum(1 for p in packs if p["dark"])
    core = sum(1 for r in rows if r["contract"] == "core")
    render = sum(1 for r in rows if r["read_render"])
    return f"""{HEAD.format(title="SHELEG style packs", site=SITE, canon=f"{SITE}/", desc="Style packs for coding agents, each extracted from a real production interface and every contrast ratio recomputed by a gate rather than asserted. Browse them rendered in their own tokens.")}
<header class="top">
  <h1>SHELEG style packs</h1>
  <p class="sub">{n} style packs for coding agents. Each one was extracted from a real
  production interface: colours, type, spacing, radii and motion tokens read off the running
  page, with every contrast ratio recomputed by a gate rather than asserted. A pack is a
  token layer plus the rules for spending it &mdash; and a list of what it bans.</p>
  <p class="sub"><b>The site each pack was measured from is not published here.</b> Sources
  are recorded inside the packs; this page is about the systems, not about whose they were.</p>
  <div class="cards">
    <a class="tile" href="packs.html"><span class="n-big">{n}</span>
      <h3>Browse the packs</h3>
      <p>Every card rendered in its own token layer &mdash; swatches, radius, accent and type
      stack read out of the pack, not described. Filter by field, by motion ceiling, by text.</p></a>
    <a class="tile" href="audit.html"><span class="n-big">{render}/{n}</span>
      <h3>Collection audit</h3>
      <p>How each pack was measured, and what the automated gates cannot see. {core} sit on
      the core contract by design; the rest answer all thirteen headings.</p></a>
    <a class="tile" href="{FAMILY}">
      <span class="n-big">&harr;</span>
      <h3>The rest of the family</h3>
      <p>This is the visual layer of a set of skills that split the work around the
      code &mdash; what the interface must do, how it sounds, how a change reaches the
      repository. No count here: this repository cannot derive one, and a number it
      cannot check is a number that goes stale.</p></a>
  </div>
  <p class="sub" style="margin-top:6px">Source, and installing just this one:
  <a href="https://github.com/ssheleg/sheleg-design-skill">the repository</a> ·
  <code>npx sheleg-design-skill</code> · {dark} of {n} packs stand on a dark field.</p>
</header>
<main>
  <h2>What a pack contains</h2>
  <p class="sub">Thirteen headings, and the same thirteen every time: register, palette,
  type, texture and surface, components, hero, responsive, motion tokens, signature motifs,
  the signature element, micro-interactions, bans, and the traps the reference carries.
  Alongside it ships a token CSS file to copy verbatim and a React reference kit that
  renders the states a token layer cannot describe &mdash; hover, focus-visible, disabled,
  selected.</p>
  <h2>Why the ratios are computed</h2>
  <p class="sub">A production site is a real source and an imperfect one. Across this
  library, references were found putting white text on a fill at 2.9:1, secondary copy at
  2.5:1, and a focus ring composited to 1.3:1 against a 3:1 floor. Each pack keeps the
  measured hue and moves only lightness until the pairing clears, and states the correction
  with its number at the declaration &mdash; so a derived value can never later be read as a
  measured one.</p>
</main>
{foot(stamp)}"""


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(ROOT / "_site"))
    args = ap.parse_args()

    gallery, auditor = load("gallery"), load("audit_packs")
    packs = gallery.collect()
    stray = [p["name"] for p in packs if p["unresolved"]]
    if stray:
        print(f"unresolved var() in: {', '.join(stray)}", file=sys.stderr)
        return 1
    rows = auditor.collect(check_live=False)

    stamp = git("rev-parse", "--short", "HEAD") or "working tree"
    out = pathlib.Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    stamp_date = git("log", "-1", "--format=%ad", "--date=short") or "1970-01-01"
    pages = {
        "index.html": index_page(packs, rows, stamp),
        "packs.html": gallery.render(packs, public=True, meta=page_meta(
            "SHELEG style packs — every pack in its own tokens",
            "All the style packs, each card rendered in its own token layer: swatches, radius, "
            "accent and type stack read out of the pack rather than described.",
            f"{SITE}/packs.html")),
        "audit.html": audit_page(rows, stamp),
        ".nojekyll": "",
        "robots.txt": robots_txt(),
        "sitemap.xml": sitemap_xml(stamp_date),
        "llms.txt": llms_txt(packs, rows),
    }
    terms = source_terms(packs, rows)
    # A pack name is public by necessity. Where it equals its own source's brand — see
    # ADR-0001, three recorded cases — the name stays and the guard is told which.
    allow = {p["name"].lower() for p in packs}
    collisions = sorted(terms & allow)
    if collisions:
        print(f"note: {len(collisions)} pack name(s) equal their own source brand "
              f"({', '.join(collisions)}) — allowed by ADR-0001, not renamed", file=sys.stderr)
    failed = False
    for name, text in pages.items():
        (out / name).write_text(text)
        if not name.endswith((".html", ".txt", ".xml")):
            continue
        bad = leaks(text, terms, allow)
        if bad:
            failed = True
            print(f"FAIL {name}: leaks {len(bad)} source term(s): {', '.join(bad[:8])}", file=sys.stderr)
    if failed:
        print("the published site must name no source — build refused", file=sys.stderr)
        return 1
    card = load("ogcard").card(packs)
    (out / "og.png").write_bytes(card)
    html_pages = sum(1 for n in pages if n.endswith(".html"))
    print(f"{out} — {html_pages} pages + robots/sitemap/llms + a {len(card):,}-byte card, "
          f"{len(packs)} packs, 0 of {len(terms)} source terms present")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
