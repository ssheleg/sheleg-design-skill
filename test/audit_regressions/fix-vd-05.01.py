#!/usr/bin/env python3
"""FIX-VD-05.01 — the Button spine is a passthrough, not a wall (sherlock, VD-05).

The finding (statically determined, per the parent): the workbench `Button`
hardcoded `type="button"` with no override, took `onClick: () => void` (no
event), forwarded no `ref`, and dropped every native/ARIA prop the caller
passed — destructuring discarded them. A form submit could not be built, an
icon-only button could carry no `aria-label`, a trigger no `aria-controls`,
and `ref.focus()` was impossible.

The fix under test:
* `ButtonProps` extends the host element's own attribute type (native + ARIA
  passthrough), the component is a `forwardRef`, `...rest` is spread onto the
  node, and `type` defaults to `button` but an explicit caller `type` wins —
  a design default fills a hole, it never overwrites an explicit prop.
* The bridge doctrine states the spine-is-a-passthrough contract and that the
  six are reference primitives, not a product component system.

The Button.tsx contract is asserted from source (the behaviour is static), and
the override semantics are run as a pure model. Standard library only.
"""
import os
import re
import sys

sys.dont_write_bytecode = True

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
BUTTON = os.path.join(ROOT, "kits", "workbench", "src", "Button.tsx")
BRIDGE = os.path.join(ROOT, "plugins", "sheleg-design", "skills", "sheleg-design",
                      "DESIGN_SYNC_BRIDGE.md")

failures = []


def case(name, fn):
    try:
        fn()
        print(f"  ok  {name}")
    except AssertionError as e:
        failures.append(f"{name}: {e}")
        print(f"FAIL  {name}: {e}")


def src():
    with open(BUTTON, encoding="utf-8") as fh:
        return fh.read()


# ---------------- Button.tsx source contract (behaviour is static)


def t_props_extend_host_attributes():
    s = src()
    assert re.search(r"extends\s+Omit<\s*ButtonHTMLAttributes<HTMLButtonElement>",
                     s), "ButtonProps no longer extends the host element's attribute type"


def t_forwards_ref():
    s = src()
    assert "forwardRef<HTMLButtonElement, ButtonProps>" in s, \
        "Button is not a forwardRef — ref.focus() cannot land on the DOM node"
    assert re.search(r"<button\b[^>]*\bref=\{ref\}", s, re.S), \
        "the forwarded ref is not attached to the <button>"


def t_spreads_rest_onto_node():
    s = src()
    assert "...rest" in s and re.search(r"<button\b[^>]*\{\.\.\.rest\}", s, re.S), \
        "native/ARIA props are not spread onto the <button> (they would be dropped)"


def t_type_default_is_overridable():
    s = src()
    assert re.search(r"type=\{\s*type\s*\?\?\s*'button'\s*\}", s), \
        "type is not `type ?? 'button'` — the default is not overridable"
    # the destructure must pull `type` out so it is not also in ...rest (double-set)
    assert re.search(r"\{[^}]*\btype\b[^}]*\.\.\.rest\s*\}", s, re.S), \
        "type is not destructured out before the rest spread"
    # and the old un-overridable literal must be gone
    assert 'type="button"' not in s, "the hardcoded, un-overridable type=\"button\" survived"


# ---------------- the override semantics, run as a pure model


def resolve(defaults, caller):
    """The component's rule: a default fills a hole; an explicit caller prop
    always wins. Mirrors `type={type ?? 'button'}` plus `{...rest}`."""
    out = dict(defaults)
    for k, v in caller.items():
        if v is not None:
            out[k] = v            # explicit caller value overrides the default
    return out


def t_submit_overrides_default_type():
    r = resolve({"type": "button"}, {"type": "submit"})
    assert r["type"] == "submit", "an explicit type=submit was erased by the default"


def t_default_fills_the_hole():
    r = resolve({"type": "button"}, {"aria-label": "Close"})
    assert r["type"] == "button", "the default type did not apply when caller omitted it"
    assert r["aria-label"] == "Close", "aria-label did not pass through"


def t_trigger_and_state_pass_through():
    r = resolve({"type": "button"},
                {"aria-controls": "menu-1", "aria-expanded": True, "disabled": True})
    assert r["aria-controls"] == "menu-1" and r["aria-expanded"] is True, \
        "trigger controls did not pass through"
    assert r["disabled"] is True, "state prop did not pass through"


# ---------------- bridge doctrine


def t_bridge_states_passthrough_contract():
    flat = " ".join(open(BRIDGE, encoding="utf-8").read().split())
    for needle in ("The spine is a passthrough, not a wall",
                   "extends the host element's own\nattribute type".replace("\n", " "),
                   'defaults `type="button"` but an explicit `type="submit"` wins',
                   "`ref.focus()` lands on the real DOM node",
                   "A\n  design default may never silently erase a prop the caller set".replace("\n  ", " "),
                   "These are reference primitives, not a product component system"):
        assert needle in flat, f"the bridge no longer states {needle!r}"


def main():
    case("ButtonProps extends the host element's attribute type", t_props_extend_host_attributes)
    case("Button forwards a ref onto the node", t_forwards_ref)
    case("native/ARIA props are spread onto the node", t_spreads_rest_onto_node)
    case("the type default is overridable", t_type_default_is_overridable)
    case("an explicit type=submit overrides the default", t_submit_overrides_default_type)
    case("the default fills the hole when the caller omits type", t_default_fills_the_hole)
    case("trigger controls and state pass through", t_trigger_and_state_pass_through)
    case("the bridge states the passthrough / reference-primitive contract",
         t_bridge_states_passthrough_contract)
    if failures:
        print(f"\n{len(failures)} failure(s)")
        return 1
    print("\nall green")
    return 0


if __name__ == "__main__":
    sys.exit(main())
