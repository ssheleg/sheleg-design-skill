# Security

## What this skill does on your machine

`sheleg-design` is documentation — a design methodology, style packs and their
token CSS — plus two small installers. There is no runtime, no service and no
build step.

| Component | Runtime behavior |
|---|---|
| `SKILL.md`, `SHELEG_DESIGN.md`, `styles/*.md` | Text. Read by the agent; executes nothing. |
| `styles/tokens/*.css` | Plain CSS custom properties, copied into your project when you choose a pack. No `@import`, no external font or asset URLs. |
| `cursor/rules/*.mdc` | Text read by the host agent. |
| `bin/cli.js` (npx installer) | Runs only when you invoke it. Copies the bundle into `~/.claude/` and/or `.cursor/`. Zero dependencies, no post-install script. |
| `install.sh` | POSIX fallback for the same copy. |

There is no telemetry, no analytics and no phone-home.

## Network behavior

`bin/cli.js` makes no network requests — it copies from the package you already
downloaded.

`install.sh` **does** reach the network, but only in one case: when you run it
without a local checkout, it fetches each bundle file over HTTPS from
`raw.githubusercontent.com/ssheleg/sheleg-design-skill/main/`. With a checkout
present it copies locally and makes no requests. The file list is fixed in the
script — it never fetches a path derived from your input.

This means the documented one-liner —

```bash
curl -fsSL https://raw.githubusercontent.com/ssheleg/sheleg-design-skill/main/install.sh | sh
```

— pipes a remote script into a shell. That is convenient and it is also a real
trust decision. If you would rather not, clone the repo and run `./install.sh`
from the checkout, or use `npx sheleg-design-skill`, which copies from the signed
npm tarball.

## What it writes

Only the skill bundle, into `~/.claude/skills/sheleg-design/` and/or
`.cursor/skills/sheleg-design/`, plus the slash command when the Claude channel
is used. Existing files are overwritten only with `--force`. Nothing outside
those directories is touched, and nothing is deleted.

## Reporting a vulnerability

Do **not** open a public issue. Report privately through
[GitHub Security Advisories](https://github.com/ssheleg/sheleg-design-skill/security/advisories/new),
or via the contacts on [sshlg.me](https://sshlg.me).

Include the version, your OS and agent, what you observed, and a reproduction if
you have one. Expect a first response within a few days. Fixes ship as a normal
tagged release with the issue described in `CHANGELOG.md`.

## Supported versions

The latest release on `main` is the supported one. There are no long-term support
branches — fixes go into the next tag.

## Verifying for yourself

```bash
git clone https://github.com/ssheleg/sheleg-design-skill && cd sheleg-design-skill
```

```bash
python3 test/validate.py && node --check bin/cli.js
```

```bash
grep -rn "child_process\|spawnSync\|execSync\|fetch(\|https\?://" bin/cli.js
```

The last command returns nothing — the Node installer neither spawns processes
nor talks to the network.
