# Knowledge provenance

Where the reviewed knowledge in this pack came from, and the rules that governed
taking it. This file exists because *"we learned it from an open repository"* is
not a licence, not a citation, and not a substitute for saying exactly which
bytes were read and what was done with them. Every adopted method carries its
receipt here: the commit, the source-relative path, the digest of the file
reviewed, a permalink, whether the result is **derived** (a method re-expressed
in our own words) or **adapted** (text carried over), and the date it was
verified.

**The controlling decision (XD-01).** No external assets are transferred into
this pack. Platform guidance (iOS, Android) is **paraphrased from the primary
platform documentation in our own words**, not copied from a third party, until
that third party's MIT notice has been verified and attached — so the rows below
are *evidence a method exists and works*, never instruction authority and never
a source whose text was vendored.

## Adopted sources

| # | Source (commit-pinned) | Path | SHA256 of reviewed file | Kind | Verified | Permalink |
|---|---|---|---|---|---|---|
| 1 | pbakaus/impeccable @ `4db7f6ba4b6ef661bc8a721261b691b40648c08a` | `plugin/skills/impeccable/SKILL.md` | `53cd1dec43ab49a9bfb31a1f47c1b231dbe1d3ed04e5fcfa3569be2579040291` | derived | 2026-09-07 | https://github.com/pbakaus/impeccable/blob/4db7f6ba4b6ef661bc8a721261b691b40648c08a/plugin/skills/impeccable/SKILL.md |
| 2 | pbakaus/impeccable @ `4db7f6ba4b6ef661bc8a721261b691b40648c08a` | `plugin/skills/impeccable/reference/ios.md` | `40c87038b5f75147a5952a96237acf312a327bf70c1bcd8e0a5f064625ae9668` | derived | 2026-09-07 | https://github.com/pbakaus/impeccable/blob/4db7f6ba4b6ef661bc8a721261b691b40648c08a/plugin/skills/impeccable/reference/ios.md |
| 3 | pbakaus/impeccable @ `4db7f6ba4b6ef661bc8a721261b691b40648c08a` | `plugin/skills/impeccable/reference/android.md` | `058f81f256134841875fd3183e06b37a023de0c877fd2b9eecd97011640791fe` | derived | 2026-09-07 | https://github.com/pbakaus/impeccable/blob/4db7f6ba4b6ef661bc8a721261b691b40648c08a/plugin/skills/impeccable/reference/android.md |
| 4 | pbakaus/impeccable @ `4db7f6ba4b6ef661bc8a721261b691b40648c08a` | `plugin/skills/impeccable/reference/adapt.native.md` | `17c583cf8ad41266ea1e787b666b9d91fe13469d3d0f6af57c08e0146f9b17ac` | derived | 2026-09-07 | https://github.com/pbakaus/impeccable/blob/4db7f6ba4b6ef661bc8a721261b691b40648c08a/plugin/skills/impeccable/reference/adapt.native.md |
| 5 | pbakaus/impeccable @ `4db7f6ba4b6ef661bc8a721261b691b40648c08a` | `plugin/skills/impeccable/reference/audit.native.md` | `fe91fcf28638f95577af481a50edaf339d6c9a3ad3b9fa477bc81c116b8bc392` | derived | 2026-09-07 | https://github.com/pbakaus/impeccable/blob/4db7f6ba4b6ef661bc8a721261b691b40648c08a/plugin/skills/impeccable/reference/audit.native.md |
| 6 | julianoczkowski/designer-skills @ `c259656c76d9758d7ead46b0d2f125cbe84f8665` | `frontend-design/SKILL.md` | `6a078fa3e5a5cef2656d621a90c8dff8191bd9d8a3724df1b98760262c88ef60` | derived | 2026-09-07 | https://github.com/julianoczkowski/designer-skills/blob/c259656c76d9758d7ead46b0d2f125cbe84f8665/frontend-design/SKILL.md |

**Kind.** *derived* — the method was read and re-expressed in this pack's own
words; no source text was carried over, so no source licence rides on it beyond
attribution. *adapted* — source text was carried over; a row of that kind
additionally requires the transfer rules below, and none of the rows above is of
that kind today.

## Transfer rules (apply the moment a row becomes `adapted`)

1. **Carry the licence with the text.** Transferred text keeps its upstream
   notice — an Apache-2.0 source keeps its `LICENSE` and `NOTICE`, and each
   modified file is marked as modified per §4 of that licence. Text is not
   "ours" because it sits in our tree.
2. **Platform-derived material is verified before it is attached.** For anything
   traceable to a platform vendor, the original **MIT notice is checked and
   attached** before the text is used; until then the knowledge is paraphrased
   from the primary platform docs, not taken from the intermediary.
3. **A source path, a SHA and a permalink, or it is not adopted.** A method with
   no row here has no provenance and does not ship.

## What is NOT in the knowledge package

The knowledge package is doctrine and method only. It deliberately excludes:

- **the launcher** — installation machinery is not knowledge;
- **any foreign router or hook** — another pack's control flow is not adopted,
  only observed;
- **any API or font SERVICE** — a runtime dependency is not vendored knowledge;
- **images and fonts** — **no binary asset is vendored.** Cloning a repository
  under its licence does NOT automatically clear the third-party assets inside
  it, and this pack makes no such promise: an asset's own licence is a separate
  question, so assets are referenced by their upstream, never copied in.
