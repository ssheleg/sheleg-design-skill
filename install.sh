#!/bin/sh
# POSIX fallback installer for the SHELEG Design skill (no Node required).
# Usage: ./install.sh [target-dir] [--force]   (default: .cursor/skills/sheleg-design)
# From the web:
#   curl -fsSL https://raw.githubusercontent.com/ssheleg/sheleg-design-skill/main/install.sh | sh
# Exit codes: 0 installed, 1 missing transport, 2 usage,
#             3 refused — the target home's plugin channel owns this skill (--force overrides).
set -eu

RAW="https://raw.githubusercontent.com/ssheleg/sheleg-design-skill/main/plugins/sheleg-design/skills/sheleg-design"
SRC_DIR="$(CDPATH= cd -- "$(dirname -- "$0")" 2>/dev/null && pwd)/plugins/sheleg-design/skills/sheleg-design"

TARGET=""
FORCE=0
for arg in "$@"; do
  case "$arg" in
    --force) FORCE=1 ;;
    -*) echo "usage: $0 [target-dir] [--force]" >&2; exit 2 ;;
    *) TARGET="$arg" ;;
  esac
done
[ -n "$TARGET" ] || TARGET=".cursor/skills/sheleg-design"

# One channel per agent: a plain <home>/.claude/skills/sheleg-design beside an
# installed plugin is two listings of the same skill, and the stale copy wins.
# Refuse rather than create that shadow, and refuse loudly — a refusal that
# exits 0 reads as success to every script above it. installed_plugins.json is
# the record of what is installed (keys are <name>@<marketplace>, and the two
# names differ: this plugin ships from the sheleg-design-skill marketplace);
# the marketplaces/ dir is kept only as the fallback signal, because it
# under-reports. A missing or unparsable JSON reads as "no plugin" — fail open,
# never crash. Only the Claude Code channel is gated: .cursor/ and other
# agents' installs are untouched.
case "$TARGET" in
  /*) ABS_TARGET="$TARGET" ;;
  *) ABS_TARGET="$(pwd)/$TARGET" ;;
esac
ABS_TARGET="${ABS_TARGET%/}"
case "$ABS_TARGET" in
  */.claude/skills/sheleg-design)
    CLAUDE_HOME="${ABS_TARGET%/.claude/skills/sheleg-design}"
    INSTALLED_JSON="$CLAUDE_HOME/.claude/plugins/installed_plugins.json"
    SPEC=""
    if [ -f "$INSTALLED_JSON" ]; then
      SPEC="$(sed -n 's/.*"\(sheleg-design@[^"]*\)".*/\1/p' "$INSTALLED_JSON" 2>/dev/null | head -n 1)" || true
    fi
    MKT_DIR=""
    for m in sheleg-design sheleg-design-skill; do
      if [ -e "$CLAUDE_HOME/.claude/plugins/marketplaces/$m" ]; then
        MKT_DIR="$CLAUDE_HOME/.claude/plugins/marketplaces/$m"
        break
      fi
    done
    if { [ -n "$SPEC" ] || [ -n "$MKT_DIR" ]; } && [ "$FORCE" -eq 0 ]; then
      REMEDY_SPEC="${SPEC:-sheleg-design@sheleg-design-skill}"
      REMEDY_MKT="${REMEDY_SPEC#*@}"
      {
        if [ -n "$SPEC" ]; then
          echo "refused: sheleg-design is already installed as the Claude Code plugin $SPEC"
          echo "         (declared in $INSTALLED_JSON)."
        else
          echo "refused: sheleg-design is already registered as a Claude Code marketplace"
          echo "         ($MKT_DIR)."
        fi
        echo "         A plain copy in $ABS_TARGET would shadow"
        echo "         the plugin and serve this frozen version forever. Update the plugin"
        echo "         channel instead:"
        echo "           claude plugin marketplace update $REMEDY_MKT"
        echo "           claude plugin update $REMEDY_SPEC"
        echo "         Family launcher: npx --yes sshlg-skills@latest update"
        echo "         Pass --force to write the plain copy anyway."
      } >&2
      exit 3
    fi
    ;;
esac

mkdir -p "$TARGET" "$TARGET/styles" "$TARGET/styles/tokens"

for f in SKILL.md STYLE_PACK_INDEX.md DESIGN_SYNC_BRIDGE.md SHELEG_DESIGN.md FIGMA_BRIDGE.md AI_PRODUCT_PATTERNS.md MOTION_DOCTRINE.md SURFACE_COMPOSITION.md MOBILE_SURFACES.md styles/STYLE_PACK_TEMPLATE.md styles/instrument-console.md styles/editorial-luxury.md styles/workbench.md styles/briefing-room.md styles/atrium.md styles/orchard.md styles/field-notes.md styles/cyclorama.md styles/showroom.md styles/blueprint.md styles/prism.md styles/maquette.md styles/scoreboard.md styles/tokens/instrument-console.css styles/tokens/editorial-luxury.css styles/tokens/workbench.css styles/tokens/briefing-room.css styles/tokens/atrium.css styles/tokens/orchard.css styles/tokens/field-notes.css styles/tokens/cyclorama.css styles/tokens/showroom.css styles/tokens/blueprint.css styles/tokens/prism.css styles/tokens/maquette.css styles/tokens/scoreboard.css styles/datasheet.md styles/tokens/datasheet.css styles/manpage.md styles/tokens/manpage.css styles/pigeonhole.md styles/tokens/pigeonhole.css styles/roster.md styles/tokens/roster.css styles/ora.md styles/outrank.md styles/babylove.md styles/tokens/ora.css styles/tokens/outrank.css styles/tokens/babylove.css styles/tenor.md styles/tokens/tenor.css styles/paperclip.md styles/tokens/paperclip.css styles/ledger.md styles/tokens/ledger.css styles/awning.md styles/tokens/awning.css styles/router.md styles/tokens/router.css styles/daylight.md styles/tokens/daylight.css styles/notation.md styles/tokens/notation.css styles/almanac.md styles/tokens/almanac.css styles/vitrine.md styles/tokens/vitrine.css styles/proscenium.md styles/tokens/proscenium.css styles/bulletin.md styles/tokens/bulletin.css styles/patchbay.md styles/tokens/patchbay.css styles/nameplate.md styles/tokens/nameplate.css styles/rimlight.md styles/tokens/rimlight.css styles/onionskin.md styles/tokens/onionskin.css styles/deskmate.md styles/tokens/deskmate.css styles/test-drive.md styles/tokens/test-drive.css styles/surveyor.md styles/tokens/surveyor.css styles/chorus.md styles/tokens/chorus.css; do
  if [ -f "$SRC_DIR/$f" ]; then
    cp "$SRC_DIR/$f" "$TARGET/$f"
  elif command -v curl >/dev/null 2>&1; then
    curl -fsSL "$RAW/$f" -o "$TARGET/$f"
  elif command -v wget >/dev/null 2>&1; then
    wget -q "$RAW/$f" -O "$TARGET/$f"
  else
    echo "Need a local checkout, curl, or wget to install $f" >&2
    exit 1
  fi
done

echo "SHELEG Design installed to $TARGET/"
# The last line says how the next version arrives.
echo "Updates: re-run this installer from the new version (curl | sh, or git pull && ./install.sh --force), or npx --yes sshlg-skills@latest update"
