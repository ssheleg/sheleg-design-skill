---
category: Signature
---

The only surface that leaves the page plane, and it goes **down**: `--terminal` is
darker than `--bg` in dark and darker than the page in light too. Raw machine output is
cut into the field, not raised off it, and that inversion is what stops a page of
instruments from reading as a card deck.

It never carries a shadow. Body text is `white-space: pre` at the caption step in
`--terminal-ink`; horizontal overflow scrolls **inside the block**, so the page never
scrolls sideways for it.

```tsx
<Terminal label="terminal" action={<Button variant="ghost">copy</Button>}>
  {`$ curl -A "ClaudeBot" https://your-site.com\nHTTP/2 403 text/html`}
</Terminal>
```
