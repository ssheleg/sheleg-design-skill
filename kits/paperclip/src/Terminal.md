---
category: Surfaces
---

**The only warm surface in the pack.** `--terminal` is `#1f1d1a` against a neutral
`#0a0a0a` field — the block has a hue because it is quoting a real shell, and nothing else
on the page is allowed one. Its header sits a step darker again at `--terminal-head`, with
three inert 10px `--terminal-dot` circles left and the tab group right. **The
inactive tab label is `--terminal-mid` (5.64:1), not the reference's
`--terminal-dim` (2.92:1)** — that is below every floor this pack enforces, on a
label a reader has to click. `--terminal-dim` survives for the prompt glyph
alone, which is `aria-hidden` punctuation.

The tab group is the pack's worked example of concentric radii: `--r-sm` inside a bar
carrying the block's `--r-md`, with 2px of padding — `8 − 2 ≈ 4.8`, which is `--r-sm`
exactly. That is why it looks machined into the bar rather than dropped on it.

The copy affordance **reports in place**: the glyph swaps to a check in `--good` with a
0.3s overshoot pop, the button does not move, and the label does not change width. No
toast, no tooltip, no layout shift.

The command is a `<code>`, the prompt is `aria-hidden` — a screen reader should read the
command, not the shell's punctuation. Long commands scroll inside the block; the page
never scrolls sideways for one.

```tsx
<Terminal
  tabs={[
    { id: 'npm', label: 'npm', command: 'npx paperclipai onboard --yes' },
    { id: 'claude', label: 'claude', command: '/plugin install paperclip' },
  ]}
  activeId="npm"
/>
```
