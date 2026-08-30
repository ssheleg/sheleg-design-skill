#!/usr/bin/env python3
"""The catalogue's own shell, dressed in a pack from this library rather than in nothing.

A library that ships thirty-nine measured token layers and paints its own catalogue in
an undocumented palette is arguing against itself. Before this file existed, the two
generators carried sixty-seven colour literals between them — a dark-only scheme that
appears in no pack, answers no `prefers-color-scheme`, and had never been through the
contrast gate every pack must pass.

So the shell below consumes **only** `var(--…)`. The values come from
`styles/tokens/workbench.css`, read at build time and inlined verbatim — the same
copy-never-transcribe rule the kits already live under, applied to the one surface
nobody had applied it to. `no_literals()` refuses a shell that reaches for a hex, and
it runs on every build rather than on a promise.

**Why `workbench`.** Two reasons a reader can check rather than take. It is the
library's own stated default for product UI, which is what a catalogue is; and it is
one of the two packs shipping a full `[data-theme="dark"]` twin, which a public page
needs and thirty-seven of the packs cannot give. Its own header names the switch used
here — *"have the app set data-theme='dark' from a prefers-color-scheme listener —
keep one switch, never two sources of truth for the theme"* — so following it is
obedience to the pack rather than a workaround around it.

What the shell does NOT dress: the cards. Every card on the front door paints itself
in the pack it advertises, and that is the page's entire argument. The shell is the
room; the cards are what is in it.
"""
from __future__ import annotations

import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
TOKENS_DIR = ROOT / "plugins/sheleg-design/skills/sheleg-design/styles/tokens"
SHELL_PACK = "workbench"

# A colour literal in the shell. The same expression the kit gate uses, so the two
# surfaces are held to one rule rather than to two that drift.
LITERAL = re.compile(r"#[0-9a-fA-F]{3,8}\b|rgba?\(|hsla?\(|oklch\(")


def tokens() -> str:
    """The pack's token layer, verbatim. Never parsed, never re-emitted — copied."""
    return (TOKENS_DIR / f"{SHELL_PACK}.css").read_text(encoding="utf-8")


def _bg(theme: str) -> str:
    """`--bg` for one theme, read out of the layer.

    `theme-color` has to be a literal — the spec takes no `var()` — so it is DERIVED
    here instead of typed. A second hand-written copy of the page background is the
    exact drift this module exists to stop, and it would show as a flash of the wrong
    colour behind a mobile URL bar rather than as anything a test would catch.
    """
    text = tokens()
    block = text if theme == "light" else text.split('[data-theme="dark"]', 1)[-1]
    m = re.search(r"--bg:\s*([^;]+);", block)
    if not m:  # a layer without a --bg cannot dress a page; say so at build time
        raise SystemExit(f"chrome: {SHELL_PACK}.css declares no --bg for the {theme} theme")
    return m.group(1).strip()


def meta() -> str:
    """The two colour-scheme meta tags, both derived."""
    return (
        '<meta name="color-scheme" content="light dark">\n'
        f'<meta name="theme-color" content="{_bg("light")}" '
        'media="(prefers-color-scheme: light)">\n'
        f'<meta name="theme-color" content="{_bg("dark")}" '
        'media="(prefers-color-scheme: dark)">'
    )


# The pack's one switch, and nothing else. It runs before first paint, so a dark
# reader never sees the light default flash past. `matchMedia` is the whole of it:
# no preference is stored, because the site has no setting to store — the OS is the
# single source of truth the pack's header asks for.
THEME_SWITCH = """<script>
(function(){var m=window.matchMedia('(prefers-color-scheme: dark)');
function s(d){document.documentElement.setAttribute('data-theme',d?'dark':'light');}
s(m.matches);m.addEventListener('change',function(e){s(e.matches);});})();
</script>"""

# The shell. Every colour is a token; every radius, gap and duration is a token.
# Sizes that the pack does not carry a token for are stated as literals on purpose —
# a px is not a colour, and inventing `--t-nav` to hold 13px would be adding to a
# pack from outside it, which is the thing this repository forbids most loudly.
SHELL = """
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--ink);
 font:400 var(--t-body)/1.55 var(--font-ui)}
/* The pack declares `--accent` @role non-text at 4.30:1, so a link may not BE the
   accent — it wears it. Text stays `--ink`; the accent is the underline, which is a
   mark and clears the 3:1 mark floor. Hover thickens the rule instead of recolouring
   the word, which is the only move available that does not break the role. */
a{color:var(--ink);text-decoration-color:var(--accent);text-underline-offset:2px;
 text-decoration-thickness:1px;
 transition:text-decoration-thickness var(--dur-hover) var(--motion-ease)}
a:hover{text-decoration-thickness:2px}
code,kbd{font-family:var(--font-data);font-size:.92em}
::selection{background:var(--accent-weak);color:var(--ink)}
:where(a,button,input,summary):focus-visible{outline:2px solid var(--accent);
 outline-offset:2px;border-radius:var(--r-control)}

/* --- the strip ------------------------------------------------------------ */
.tabs{position:sticky;top:0;z-index:9;background:var(--panel);
 border-bottom:1px solid var(--border);backdrop-filter:saturate(1.4) blur(8px)}
.tabs .inner{max-width:1600px;margin:0 auto;padding:0 32px;display:flex;gap:2px}
.tab{display:inline-block;padding:13px 14px 11px;border-bottom:2px solid transparent;
 color:var(--muted);text-decoration:none;font-size:var(--t-label);font-weight:500;
 transition:color var(--dur-hover) var(--motion-ease),
  border-color var(--dur-hover) var(--motion-ease)}
.tab:hover{color:var(--ink);background:var(--panel-2)}
.tab.on{color:var(--ink);border-bottom-color:var(--accent)}

/* --- page furniture ------------------------------------------------------- */
header.top,.top{max-width:1600px;margin:0 auto;padding:44px 32px 22px}
main{max-width:1600px;margin:0 auto;padding:14px 32px 80px}
main.narrow{max-width:1100px}
footer{max-width:1600px;margin:0 auto;padding:0 32px 64px;color:var(--muted);
 font-size:var(--t-chip)}
.crumb{margin:0 0 18px;font-size:var(--t-chip);color:var(--muted)}
h1{margin:0 0 10px;font-size:var(--t-page);font-weight:600;letter-spacing:-.02em}
h2{margin:36px 0 12px;font-size:var(--t-section);font-weight:600;letter-spacing:-.01em}
.sub{color:var(--muted);max-width:80ch;margin:0 0 10px}
.sub b{color:var(--ink);font-weight:600}
.sub code{color:var(--ink)}

/* --- tables --------------------------------------------------------------- */
table{width:100%;border-collapse:collapse;font-size:var(--t-label)}
th,td{text-align:left;padding:9px 10px;border-bottom:1px solid var(--border);
 white-space:nowrap}
th{color:var(--muted);font-weight:500;font-size:var(--t-chip);text-transform:uppercase;
 letter-spacing:.06em;position:sticky;top:0;background:var(--bg)}
td small{color:var(--muted)}
tbody tr:hover{background:var(--panel-2)}
.y{color:var(--ok)}
.n{color:var(--muted)}
.o{color:var(--warn)}

/* --- blocks --------------------------------------------------------------- */
.notes dl{display:grid;grid-template-columns:auto 1fr;gap:8px 18px;max-width:96ch;
 font-size:var(--t-label)}
.notes dt{color:var(--ink);font-weight:500;white-space:nowrap}
.notes dd{margin:0;color:var(--muted)}
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));
 gap:var(--space-4);margin:24px 0}
.tile{border:1px solid var(--border);border-radius:var(--r-card);padding:20px;
 background:var(--panel);text-decoration:none;color:inherit;display:block;
 transition:border-color var(--dur-hover) var(--motion-ease)}
.tile:hover{border-color:var(--border-strong)}
.tile h3{margin:0 0 6px;font-size:var(--t-card);font-weight:600}
.tile p{margin:0;color:var(--muted);font-size:var(--t-label)}
.n-big{font-size:var(--t-page);font-weight:600;letter-spacing:-.02em;display:block;
 margin-bottom:2px;font-family:var(--font-data)}

/* --- controls ------------------------------------------------------------- */
.controls{position:sticky;top:0;z-index:5;background:var(--panel);
 backdrop-filter:saturate(1.4) blur(8px);border-bottom:1px solid var(--border);
 padding:13px 32px}
.controls .inner{max-width:1600px;margin:0 auto;display:flex;gap:var(--space-2);
 flex-wrap:wrap;align-items:center}
input[type=search]{background:var(--bg);border:1px solid var(--border-strong);
 color:var(--ink);border-radius:var(--r-control);padding:8px 12px;min-width:260px;
 font-size:var(--t-body);font-family:inherit}
input[type=search]::placeholder{color:var(--muted)}
button{background:var(--panel-2);border:1px solid var(--border-strong);
 color:var(--muted);border-radius:var(--r-pill);padding:6px 14px;
 font-size:var(--t-label);font-family:inherit;cursor:pointer;
 transition:background-color var(--dur-state) var(--motion-ease),
  color var(--dur-state) var(--motion-ease)}
button:hover{color:var(--ink)}
button[aria-pressed=true]{background:var(--accent);color:var(--accent-ink);
 border-color:var(--accent)}
.count{color:var(--muted);font-size:var(--t-label);margin-left:auto;
 font-family:var(--font-data)}

@media (max-width:640px){
 header.top,.top,main,footer,.controls,.tabs .inner{padding-left:16px;padding-right:16px}
 table{display:block;overflow-x:auto;white-space:nowrap}
}
"""


def no_literals(*css: str) -> None:
    """Refuse a shell that reaches for a colour.

    Called by both generators on every build. The point is not tidiness: a literal
    here is a colour that never went through `validate_palette.py`, on the one page
    that exists to argue that colours should.
    """
    for block in css:
        for i, line in enumerate(block.splitlines(), 1):
            hit = LITERAL.search(line)
            if hit:
                raise SystemExit(
                    f"chrome: the shell carries the colour literal '{hit.group(0)}' on "
                    f"line {i} — the shell consumes var(--…) only, and its values come "
                    f"from styles/tokens/{SHELL_PACK}.css"
                )


def style_block() -> str:
    """The whole thing: the pack verbatim, then the shell that consumes it."""
    no_literals(SHELL)
    return f"<style>\n/* --- {SHELL_PACK} token layer, copied verbatim --- */\n" \
           f"{tokens()}\n/* --- the catalogue shell, var() only --- */{SHELL}</style>"


if __name__ == "__main__":
    no_literals(SHELL)
    print(f"chrome: {SHELL_PACK} + {len(SHELL.splitlines())} shell lines, 0 literals")
