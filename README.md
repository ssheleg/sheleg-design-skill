# SHELEG Design — agent skill

[![npm version](https://img.shields.io/npm/v/sheleg-design-skill)](https://www.npmjs.com/package/sheleg-design-skill)
[![CI](https://github.com/ssheleg/sheleg-design-skill/actions/workflows/validate.yml/badge.svg)](https://github.com/ssheleg/sheleg-design-skill/actions/workflows/validate.yml)
[![license: MIT](https://img.shields.io/badge/license-MIT-blue)](./LICENSE)

> A motion + particle interface methodology for building cinematic,
> scroll-driven landing pages — packaged as an installable agent skill for
> Cursor and Claude.

Install it into any project with one command:

```bash
npx sheleg-design-skill
```

That drops a `SKILL.md` + `SHELEG_DESIGN.md` bundle into your project so your
coding agent can discover the skill and build sites on its principles.

## What is SHELEG Design?

A page feels *alive* not from many animations, but from a **single source of
truth** (scroll position) driving **many cheap, layered responses** that are
individually quiet and collectively cinematic. One scroll "clock" feeds a WebGL
particle field, a 2D fallback, attention dimming, parallax, scrubbed
instruments, and a progress rail — each an independent, degrade-to-calm layer.
Nothing crossfades; things *redeploy*. The result reads as one precision
instrument responding to your hand.

It was reverse-engineered from a production landing page (a 14-scene particle
narrative that morphs through formations and culminates in a brand "N" that
charges and bursts). The skill distills the architecture and the principles so
an agent can rebuild that level on a new site.

### The five principles

1. **One clock.** All motion derives from one measured scroll state.
2. **Read per frame, notify rarely.** Hot consumers read imperatively; only
   coarse changes hit the framework's render path.
3. **Hold, then redeploy.** Hold a formation ~80% of a section, then morph in a
   short, phase-staggered, arc-curved wave. No crossfades.
4. **Earned motion.** Scrub is for instruments that narrate state over time;
   entrance motion stays sub-500ms and never gates content.
5. **Degrade to calm.** Reduced-motion / coarse pointer / no-WebGL collapse to a
   static, fully-legible page.

## Usage

```bash
# Auto-detect (.cursor/ or .claude/), default to .cursor/skills/sheleg-design/
npx sheleg-design-skill

# Force a flavor
npx sheleg-design-skill --cursor
npx sheleg-design-skill --claude

# Custom location
npx sheleg-design-skill --dir docs/skills/sheleg-design

# Overwrite an existing install
npx sheleg-design-skill --force

# Help
npx sheleg-design-skill --help
```

### Other install paths

```bash
# Claude Code plugin (adds the /sheleg-design command too)
/plugin marketplace add ssheleg/sheleg-design-skill
/plugin install sheleg-design@sheleg-design-skill

# vercel-labs skills CLI (70+ agents)
npx skills add ssheleg/sheleg-design-skill

# POSIX fallback, no Node
curl -fsSL https://raw.githubusercontent.com/ssheleg/sheleg-design-skill/main/install.sh | sh
```

### What gets installed

| File | Purpose |
|---|---|
| `SKILL.md` | Agent-facing skill: discovery trigger, the principles, how to apply them, quick-reference rules, common mistakes |
| `SHELEG_DESIGN.md` | The full reference: architecture, layer-by-layer mechanics with code, the exact morph math, the DOM↔WebGL projection bridge, a build-from-scratch recipe, and the "why it works" |

After installing, a Cursor or Claude agent in that project can discover the
skill and use it when you ask it to build or upgrade a cinematic,
scroll-driven, particle-backed page.

## Stack-agnostic

The skill teaches **principles and architecture**, not a fixed dependency set.
The reference implementation happens to use Next.js + React + three /
react-three-fiber + GSAP ScrollTrigger + Lenis + Framer Motion, but the method
applies to any stack that can render to a canvas/WebGL surface and read scroll.

## Zero dependencies

The installer is a single zero-dependency Node script, so `npx` runs instantly
with no install step and no supply-chain surface.

## Development

`python3 test/validate.py` checks repo consistency (manifests, version sync,
skill/command/rule front-matter, relative links); CI runs it plus a CLI smoke
test on every push and PR. Versioning is semver; bump `marketplace.json` +
`plugin.json` + `package.json` + `CHANGELOG.md` together — the validator
enforces the sync.

## По-русски (коротко)

SHELEG Design — методология кинематографичных скролл-лендингов: один
scroll-«клок» питает много дешёвых независимых слоёв (WebGL-частицы,
2D-фоллбек, параллакс, scrub-инструменты, прогресс-рейл), каждый деградирует
до спокойной статики. Ничего не кроссфейдится — формации «передислоцируются».
Установка: `npx sheleg-design-skill` (авто-детект `.cursor`/`.claude`), либо
плагин Claude Code — `/plugin marketplace add ssheleg/sheleg-design-skill`,
затем `/plugin install sheleg-design@sheleg-design-skill` (даст команду
`/sheleg-design`). Агент получает SKILL.md (принципы и порядок работы) и
SHELEG_DESIGN.md (полный референс: архитектура, точная математика морфа,
DOM↔WebGL-мост, рецепт сборки с нуля).

## License

MIT © ssheleg
