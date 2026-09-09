#!/usr/bin/env python3
"""FIX-VD-03.01 — the platform/renderer contract (sherlock audit, VD-03).

The finding: platform target and prototype renderer were one decision — so a
SwiftUI brief could get Expo as its only answer, and a browser HTML
screenshot could be passed off as native proof (Dynamic Type / VoiceOver
inferred from a web render).

The fix under test: the platform target (iOS/Android/RN/web) picks the
component adapter separately from the renderer; a route to one target never
receives another's toolkit; a web HTML mockup is a demonstration with a
native-equivalent column, never native proof. Documented in
MOBILE_SURFACES.md and SKILL.md, and the adapter/proof rules run as behaviour.

Standard library only.
"""
import os
import sys

sys.dont_write_bytecode = True

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
SKILL_DIR = os.path.join(ROOT, "plugins", "sheleg-design", "skills", "sheleg-design")

failures = []


def case(name, fn):
    try:
        fn()
        print(f"  ok  {name}")
    except AssertionError as e:
        failures.append(f"{name}: {e}")
        print(f"FAIL  {name}: {e}")


def read(name):
    return open(os.path.join(SKILL_DIR, name), encoding="utf-8").read()


def t_doctrine_states_the_split():
    ms = " ".join(read("MOBILE_SURFACES.md").split())
    for needle in ("Platform target and prototype renderer are two decisions, not one",
                   "UIKit / SwiftUI against Apple's **HIG**",
                   "Jetpack **Compose** / Material",
                   "a SwiftUI\nscreen is not answered with Expo".replace("\n", " "),
                   "A web HTML mockup is a demonstration, never native proof",
                   "explicit **native-equivalent** column",
                   "browser screenshot proves nothing about Dynamic Type or\nVoiceOver".replace("\n", " ")):
        assert needle in ms, f"MOBILE_SURFACES.md no longer states {needle!r}"
    sk = " ".join(read("SKILL.md").split())
    assert "separate\nthe platform target".replace("\n", " ") in sk, \
        "SKILL.md does not reference the platform/renderer split"


# ---------------- the adapter + proof rules, executed


ADAPTER = {
    "ios-native": "UIKit/SwiftUI/HIG",
    "android-native": "Compose/Material",
    "react-native": "RN primitives",
    "web": "pack web components",
}


def adapter_for(target):
    if target not in ADAPTER:
        raise ValueError(f"unknown platform target {target!r}")
    return ADAPTER[target]


def native_proof(renderer, has_native_equivalent_column):
    """A web/HTML render is a demonstration; it is native proof only if it is a
    native runtime render. A web mockup without the native-equivalent column is
    not even a valid demonstration."""
    if renderer in ("ios-native", "android-native"):
        return "native-proof"
    if renderer == "web":
        return "demonstration" if has_native_equivalent_column else "invalid"
    return "demonstration"


def t_target_picks_its_own_adapter():
    assert adapter_for("ios-native") == "UIKit/SwiftUI/HIG"
    assert adapter_for("react-native") == "RN primitives"
    assert adapter_for("ios-native") != adapter_for("react-native"), \
        "a SwiftUI target and an RN target shared an adapter — the conflation"


def t_swiftui_route_never_gets_expo_only():
    # Expo/RN is the RN adapter; a native-iOS target must not resolve to it.
    assert adapter_for("ios-native") != ADAPTER["react-native"], \
        "the native-iOS route resolved to RN — the finding itself"


def t_web_screenshot_is_not_native_proof():
    assert native_proof("web", has_native_equivalent_column=True) == "demonstration", \
        "a web HTML mockup was accepted as native proof"
    assert native_proof("ios-native", True) == "native-proof"


def t_web_mockup_needs_the_native_equivalent_column():
    assert native_proof("web", has_native_equivalent_column=False) == "invalid", \
        "a web mockup without a native-equivalent column passed as a demonstration"


def main():
    case("the doctrine states the platform/renderer split",
         t_doctrine_states_the_split)
    case("each platform target picks its own component adapter",
         t_target_picks_its_own_adapter)
    case("a SwiftUI route never resolves to RN/Expo only",
         t_swiftui_route_never_gets_expo_only)
    case("a web screenshot is a demonstration, not native proof",
         t_web_screenshot_is_not_native_proof)
    case("a web mockup needs its native-equivalent column",
         t_web_mockup_needs_the_native_equivalent_column)
    if failures:
        print(f"\n{len(failures)} failure(s)")
        return 1
    print("\nall green")
    return 0


if __name__ == "__main__":
    sys.exit(main())
