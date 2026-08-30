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

chrome = None  # loaded in main(), like the other tool modules

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
            '<meta name="robots" content="index,follow,max-image-preview:large">\n'
            # The colour-scheme pair is DERIVED from the shell pack's own --bg and is
            # emitted by `chrome.meta()`; a second hand-typed copy here is how the URL
            # bar ends up a different colour from the page behind it.
            f'{chrome.meta()}\n'
            '<meta property="og:site_name" content="SHELEG style packs">\n<meta property="og:locale" content="en_US">\n'
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



# ---------------------------------------------------------------- the tab strip
#
# Since 1.52.0 the front door IS the designs. Before it, `/` was three tiles and a
# reader had to click once before seeing a single pack — a menu in front of the
# thing the site is for.
#
# The tabs are LINKS to three real pages, not panels toggled in one document, and
# that is a deliberate SEO decision: one URL per screen, every screen fully in the
# HTML, nothing behind a click a crawler has to execute. `rel="prefetch"` makes the
# switch feel like a tab without costing the indexability that a client-side tab
# panel costs. `aria-current="page"` is what marks the selected one for a reader on
# a screen reader; `.on` is what marks it for everyone else.
TABS = (("", "Designs", "Every pack rendered in its own token layer"),
        ("audit.html", "Audit", "How each pack was measured"),
        ("method.html", "Method", "What a pack is, and why the ratios are computed"))


def tabstrip(current: str) -> str:
    out = ['<nav class="tabs" aria-label="Sections">', '<div class="tabs-inner">']
    for href, label, hint in TABS:
        sel = href == current
        cls = ' class="tab on"' if sel else ' class="tab"'
        cur = ' aria-current="page"' if sel else ''
        target = href or "./"
        out.append(f'<a{cls}{cur} href="{target}" title="{esc(hint)}">{esc(label)}</a>')
    out.append('</div></nav>')
    return "\n".join(out)


def prefetch(current: str) -> str:
    return "\n".join(f'<link rel="prefetch" href="{h or "./"}">'
                      for h, _, _ in TABS if h != current)


# The tab strip's LOOK moved into `tools/chrome.py` with the rest of the shell, so it
# is dressed in the same pack as everything else. What stays here is the only thing
# that is about this site's layout rather than its palette: two sticky offsets.
TABS_CSS = """<style>
/* The gallery's own filter bar is sticky at 0 too. Two sticky strips at the same
   offset overlap; the filter bar belongs under the tabs, so it starts where they end
   (44px of tab plus its 1px rule). The selector carries `body` because the gallery's
   stylesheet is emitted after this one. */
body .controls{top:45px}
/* Same rule, same reason: the audit table's sticky header would slide under the tab
   strip. Both offsets are the strip's own height plus its rule, and there are exactly
   two sticky things on this site besides the strip. */
body table th{top:45px}
</style>"""


# ---------------------------------------------------------------- structured data
#
# One publisher node, referenced by `@id` from every page's primary entity. The
# family site shipped the opposite of this for two releases — a `Person` sitting in
# the graph that nothing pointed at — so the entity was published and anonymous at
# the same time. Each page names its own type: the front door is a CollectionPage
# carrying an ItemList of the packs (an answer engine can lift the list without
# running the filter JS), the audit is a Dataset-shaped WebPage, the method page is
# the software itself.
PUBLISHER = f'{SITE}/#publisher'
WEBSITE = f'{SITE}/#website'


def ld(*nodes: dict) -> str:
    import json as _json
    graph = {"@context": "https://schema.org", "@graph": list(nodes)}
    return ('<script type="application/ld+json">'
            + _json.dumps(graph, ensure_ascii=False, separators=(",", ":"))
            + "</script>")


def base_nodes() -> list[dict]:
    return [
        {"@type": "Organization", "@id": PUBLISHER, "name": "ssheleg",
         "url": "https://skills.sshlg.me/",
         "sameAs": ["https://github.com/ssheleg", "https://www.npmjs.com/package/sheleg-design-skill"]},
        {"@type": "WebSite", "@id": WEBSITE, "url": f"{SITE}/",
         "name": "SHELEG style packs",
         "inLanguage": "en",
         "publisher": {"@id": PUBLISHER},
         "license": "https://github.com/ssheleg/sheleg-design-skill/blob/main/LICENSE"},
    ]


def crumbs(*trail: tuple[str, str]) -> dict:
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": name, "item": url}
        for i, (name, url) in enumerate(trail)]}

# ---------------------------------------------------------------- the leak guard
STOP = {"a", "the", "and", "of", "one", "its", "com", "www", "site", "page", "production"}


TLDS = {"com", "org", "net", "dev", "app", "ing", "st", "so", "ai", "io", "global"}


def _stems(host: str) -> set[str]:
    """Every distinctive label of a host — not only the first. visible.seranking.com
    must forbid `seranking`, which a first-label-only read never saw; the guard that
    found this was its own false positive on `visible`."""
    return {lab for lab in host.replace("www.", "").split(".")
            if len(lab) > 3 and lab not in STOP and lab not in TLDS}


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
                terms |= _stems(h)
    for a in audit:
        u = (a.get("origin_url") or "").lower()
        m = re.search(r"https?://([^/]+)", u)
        if m:
            host = m.group(1)
            terms.add(host)
            terms.add(host.replace("www.", ""))
            terms |= _stems(host)
    return {t for t in terms if len(t) > 3}


_MACHINE = re.compile(r"<style\b[^>]*>.*?</style>|<script\b[^>]*>.*?</script>", re.S | re.I)


def leaks(text: str, terms: set[str], allow: set[str]) -> list[str]:
    """`allow` holds the terms a page may legitimately contain: a PACK NAME. Three packs
    carry their source brand as their own name — recorded in ADR-0001, and deliberately
    not renamed, because a pack name is a public API across four channels. Their names
    therefore cannot be stripped from a page that lists the packs, and this guard found
    all three by refusing to publish until it was told so explicitly.

    Two tiers, because the guard's subject is NAMING. A full host (it contains a dot)
    is searched raw over the whole file — a URL inside a stylesheet still makes a
    network request, so CSS is no refuge for it. A bare stem is searched only in the
    page with its <style> and <script> blocks removed, and only at word boundaries:
    `visible.seranking.com` put `visible` in this set, and the raw substring scan
    refused every page on the site for carrying `:focus-visible` in its own CSS —
    a pseudo-class, not a source name."""
    low = text.lower()
    prose = _MACHINE.sub(" ", low)
    hits = []
    for t in sorted(terms):
        if t in allow:
            continue
        if "." in t:
            if t in low:
                hits.append(t)
        elif re.search(r"(?<![a-z0-9-])" + re.escape(t) + r"(?![a-z0-9-])", prose):
            hits.append(t)
    return hits


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
    canon = f"{SITE}/audit.html"
    desc = ("How each style pack was measured, and what the automated gates cannot see: "
            "the render, a narrow width, and whether the kit was ever put in a browser.")
    machine = "\n".join([
        prefetch("audit.html"), TABS_CSS,
        ld(*base_nodes(),
           {"@type": "WebPage", "@id": f"{canon}#page", "url": canon,
            "name": "Collection audit", "description": desc,
            "isPartOf": {"@id": WEBSITE}, "publisher": {"@id": PUBLISHER},
            "inLanguage": "en"},
           crumbs(("Designs", f"{SITE}/"), ("Audit", canon)))])
    return f"""{head("Collection audit &mdash; SHELEG style packs", desc, canon)}
{machine}
{tabstrip("audit.html")}
<header class="top">
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


def head(title: str, desc: str, canon: str) -> str:
    """Every page's `<head>`, with the shell and the theme switch already in it.

    The three chrome pieces are filled here rather than at each call site, because a
    page that forgets one is a page that ships unstyled or dark-only, and nothing
    downstream would say so.
    """
    return HEAD.format(
        title=title, desc=desc, canon=canon, site=SITE,
        scheme=chrome.meta(), style=chrome.style_block(), switch=chrome.THEME_SWITCH)


HEAD = """<!doctype html><html lang="en" data-theme="light"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canon}">
<meta name="robots" content="index,follow,max-image-preview:large">
{scheme}
<meta property="og:site_name" content="SHELEG style packs">
<meta property="og:locale" content="en_US">
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
{style}{switch}</head><body>"""


def foot(stamp: str) -> str:
    return (f'<footer>Built from <code>{esc(stamp)}</code> by <code>tools/site.py</code>. '
            f'The site each pack was measured from is recorded in the pack and is '
            f'deliberately not published here.</footer>\n</body></html>')



def robots_txt() -> str:
    return (f"User-agent: *\nAllow: /\n\n"
            f"Sitemap: {SITE}/sitemap.xml\n"
            f"LLMs-Txt: {SITE}/llms.txt\n")


def sitemap_xml(stamp_date: str) -> str:
    # Only the three indexable screens. `packs.html` is a canonical alias and `404.html`
    # is noindex, so listing either would ask a crawler to index a page that tells it not
    # to — the commonest way a small sitemap starts disagreeing with its own pages.
    urls = "".join(
        f"  <url><loc>{SITE}/{p}</loc><lastmod>{stamp_date}</lastmod></url>\n"
        for p in ("", "audit.html", "method.html"))
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
              f"- [Designs]({SITE}/): the front door — every pack rendered in its own token "
              f"layer, filterable by field, motion ceiling and text. Each pack has an anchor: "
              f"{SITE}/#pack-<name>.",
              f"- [Audit]({SITE}/audit.html): how each pack was measured, and what the "
              f"automated gates cannot see.",
              f"- [Method]({SITE}/method.html): what a pack contains, why the ratios are "
              f"recomputed, and how to install it.", ""]
    return "\n".join(lines)


def index_intro(packs: list[dict], rows: list[dict]) -> str:
    """The opening two paragraphs. It states no count the gallery's own header states one
    paragraph later — the first draft said the dark and core figures twice, three lines
    apart, which is how a page starts disagreeing with itself the moment one moves."""
    return """  <p class="sub">Every card below renders in <b>its own token layer</b>, read out of the
  pack itself: the swatches, the radius, the accent and the type stack are the pack's real
  values rather than a description of them, so a card that looks wrong is a pack that
  <i>is</i> wrong. Each one was extracted from a real production interface, and every
  contrast ratio was recomputed by a gate rather than asserted.</p>
  <p class="sub"><b>The interface each pack was measured from is not published here.</b>
  Sources are recorded inside the packs; this page is about the systems. Install the set
  with <code>npx sheleg-design-skill</code>, read
  <a href="method.html">how a pack is measured</a>, or open
  <a href="audit.html">the collection audit</a>.</p>"""


def index_page(packs: list[dict], rows: list[dict], stamp: str) -> str:
    """The front door, and it IS the gallery: the designs are the first thing on it."""
    n = len(packs)
    desc = (f"{n} style packs for coding agents, each extracted from a real production "
            f"interface and rendered here in its own tokens.")
    items = {"@type": "ItemList", "name": "SHELEG style packs",
             "numberOfItems": n, "itemListOrder": "https://schema.org/ItemListUnordered",
             "itemListElement": [
                 {"@type": "ListItem", "position": i + 1, "name": p["name"],
                  "url": f"{SITE}/#pack-{p['name']}",
                  "description": p["for"].rstrip(".")}
                 for i, p in enumerate(packs)]}
    page = {"@type": "CollectionPage", "@id": f"{SITE}/#page", "url": f"{SITE}/",
            "name": "SHELEG style packs", "description": desc,
            "isPartOf": {"@id": WEBSITE}, "publisher": {"@id": PUBLISHER},
            "inLanguage": "en", "mainEntity": items}
    meta = "\n".join([
        page_meta(f"SHELEG style packs — {n} designs, in their own tokens", desc, f"{SITE}/"),
        prefetch(""), TABS_CSS, ld(*base_nodes(), page)])
    return gallery_mod.render(
        packs, public=True, meta=meta, nav=tabstrip(""),
        title=f"{n} style packs, rendered in their own tokens",
        intro=index_intro(packs, rows))


def method_page(packs: list[dict], rows: list[dict], stamp: str) -> str:
    """What a pack is. This is the prose the index carried until 1.52.0, moved off the
    front door so the designs could have it."""
    n = len(packs)
    core = sum(1 for r in rows if r["contract"] == "core")
    render = sum(1 for r in rows if r["read_render"])
    desc = ("What a SHELEG style pack contains, how it is measured off a live interface, "
            "and why every contrast ratio is recomputed rather than asserted.")
    canon = f"{SITE}/method.html"
    app = {"@type": "SoftwareApplication", "@id": f"{canon}#app",
           "name": "sheleg-design-skill", "applicationCategory": "DeveloperApplication",
           "operatingSystem": "Any", "url": canon,
           "downloadUrl": "https://www.npmjs.com/package/sheleg-design-skill",
           "codeRepository": "https://github.com/ssheleg/sheleg-design-skill",
           "license": "https://spdx.org/licenses/MIT.html",
           "description": desc, "publisher": {"@id": PUBLISHER},
           "isPartOf": {"@id": WEBSITE},
           "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"}}
    # No `page_meta` here: `HEAD` below already emits the description, the canonical and
    # the og/twitter pair for this page. Adding both shipped two canonicals and two
    # descriptions on one page, which is a crawler being asked to pick.
    meta = "\n".join([
        prefetch("method.html"), TABS_CSS,
        ld(*base_nodes(), app, crumbs(("Designs", f"{SITE}/"), ("Method", canon)))])
    return f"""{head("Method — how a SHELEG style pack is measured", desc, canon)}
{meta}
{tabstrip("method.html")}
<header class="top">
  <h1>How a pack is measured</h1>
  <p class="sub">A pack is a token layer, the rules for spending it, and a list of what it
  bans. It is extracted from a real production interface rather than composed: colours,
  type, spacing, radii and motion tokens are read off the running page, and every ratio is
  recomputed by a gate before the pack ships.</p>
</header>
<main>
  <h2>Thirteen headings, and the same thirteen every time</h2>
  <p class="sub">Register, palette, type, texture and surface, components, hero, responsive,
  motion tokens, signature motifs, the signature element, micro-interactions, bans, and the
  traps the reference carries. Alongside it ships a token CSS file to copy verbatim and a
  React reference kit that renders the states a token layer cannot describe — hover,
  focus-visible, disabled, selected. {core} of the {n} packs sit on the <b>core
  contract</b>: they deliberately leave components, hero, responsive rules and their
  signature element to you, and say so in their own contract line.</p>
  <h2>Why the ratios are computed</h2>
  <p class="sub">A production site is a real source and an imperfect one. Across this
  library, references were found putting white text on a fill at 2.9:1, secondary copy at
  2.5:1, and a focus ring composited to 1.3:1 against a 3:1 floor. Each pack keeps the
  measured hue and moves only lightness until the pairing clears, then states the correction
  with its number at the declaration — so a derived value can never later be read as a
  measured one.</p>
  <h2>What the gates cannot see</h2>
  <p class="sub">Structure is checkable and layout is not. {render} of the {n} packs were
  read off the render rather than off the stylesheet, and each kit is mounted in a browser at
  three widths and read back through <code>getComputedStyle</code> before its pack ships —
  which is how a control that promised 50px and drew 78px, and a card that painted white on
  white inside an inverted section, were both caught. The <a href="audit.html">collection
  audit</a> is the standing record of that.</p>
  <h2>Installing it</h2>
  <p class="sub"><code>npx sheleg-design-skill</code> installs the skill for Claude Code,
  Cursor and any agent that reads a <code>SKILL.md</code>; <code>npx sheleg-design-skill
  --kit &lt;pack&gt;</code> materialises one pack's React kit.
  <a href="https://github.com/ssheleg/sheleg-design-skill">The repository</a> holds the
  gates. This is the visual layer of <a href="{FAMILY}">a family of skills</a> that split
  the work around the code — what the interface must do, how it sounds, how a change reaches
  the repository.</p>
</main>
{foot(stamp)}"""


def packs_alias() -> str:
    """`packs.html` was the gallery until 1.52.0, when the gallery became the front door.
    The URL is kept because it is in the wild — and kept as a REDIRECT rather than a
    second copy, because two URLs serving one gallery is duplicate content that splits
    whatever authority the page has."""
    canon = f"{SITE}/"
    return f"""<!doctype html><html lang="en" data-theme="light"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>SHELEG style packs</title>
<link rel="canonical" href="{canon}">
<meta name="robots" content="noindex,follow">
<meta http-equiv="refresh" content="0;url=./">
{chrome.style_block()}{chrome.THEME_SWITCH}
</head><body>
<main class="narrow"><p>The pack gallery is now the front page.
<a href="./">Continue to the packs</a>.</p></main>
</body></html>"""


def not_found() -> str:
    return f"""<!doctype html><html lang="en" data-theme="light"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Not found — SHELEG style packs</title>
<meta name="robots" content="noindex,follow">
{chrome.style_block()}{TABS_CSS}{chrome.THEME_SWITCH}
</head><body>
{tabstrip("")}
<main class="narrow">
<h1>Not found</h1>
<p class="sub">That address is not part of this site. The three that are:
<a href="./">the packs</a>, <a href="audit.html">the audit</a> and
<a href="method.html">the method</a>.</p>
</main></body></html>"""


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(ROOT / "_site"))
    args = ap.parse_args()

    global gallery_mod, chrome
    gallery, auditor = load("gallery"), load("audit_packs")
    chrome = load("chrome")
    gallery_mod = gallery
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
        "method.html": method_page(packs, rows, stamp),
        "audit.html": audit_page(rows, stamp),
        "packs.html": packs_alias(),
        "404.html": not_found(),
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
