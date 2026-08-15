# Awning — the rules this design system is built on

A pure white forecourt for a product other businesses will run their own
business on. **The accent is black.** No hue reaches the chrome at all, which is
what leaves every colour on the page belonging to the thing being sold.
Extracted from a production reference (shopify.com, 2026-08-15) whose delivered
CSS carries a real three-tier token system; the full pack, with every
measurement and every trap, is `styles/awning.md` in the sheleg-design skill.

**This is the static half of a pack.** Motion does not cross this boundary:
build screens from these components, never a scroll narrative around them.

## Bans — what this system never does

- **No accent hue.** Not on a button, a link, a tab, a badge or a focus ring.
  The primary action is black; the moment chrome takes a colour, the screenshot
  inside it stops being the only colourful thing on the page.
- **No weight of 700.** Body is **420** and bold is **550**, both off the
  standard axis and both reachable only because the face is variable. Setting a
  heading in 700 is the one number this system was built to avoid.
- **No second shadow.** One three-layer token — ambient, contact, and a hairline
  edge that keeps a card legible on pure white. Dropping the third layer is why
  a copied card floats without sitting.
- **No `clamp()` in the type layer.** Size and leading ship as a paired `rem`
  value so they cannot drift; a fluid step breaks the pair.
- **Status is never by colour alone.** The derived red and green collapse toward
  each other under deuteranopia at a measured 5.2 against a floor of 8.0, so
  every state carries its word.

## The two shapes

Surfaces take the radius scale — `0.375 / 0.5 / 0.75 / 1rem`. **Buttons take
`--radius-full`,** and they take it through `--radius-button`, which is the only
place the system says why a button is a pill. Keep the indirection.
