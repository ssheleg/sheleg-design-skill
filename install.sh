#!/bin/sh
# POSIX fallback installer for the SHELEG Design skill (no Node required).
# Usage: ./install.sh [target-dir]   (default: .cursor/skills/sheleg-design)
# From the web:
#   curl -fsSL https://raw.githubusercontent.com/ssheleg/sheleg-design-skill/main/install.sh | sh
set -eu

RAW="https://raw.githubusercontent.com/ssheleg/sheleg-design-skill/main/plugins/sheleg-design/skills/sheleg-design"
TARGET="${1:-.cursor/skills/sheleg-design}"
SRC_DIR="$(CDPATH= cd -- "$(dirname -- "$0")" 2>/dev/null && pwd)/plugins/sheleg-design/skills/sheleg-design"

mkdir -p "$TARGET" "$TARGET/styles" "$TARGET/styles/tokens"

for f in SKILL.md DESIGN_SYNC_BRIDGE.md SHELEG_DESIGN.md FIGMA_BRIDGE.md AI_PRODUCT_PATTERNS.md MOTION_DOCTRINE.md SURFACE_COMPOSITION.md MOBILE_SURFACES.md styles/STYLE_PACK_TEMPLATE.md styles/instrument-console.md styles/editorial-luxury.md styles/workbench.md styles/briefing-room.md styles/atrium.md styles/orchard.md styles/field-notes.md styles/cyclorama.md styles/showroom.md styles/blueprint.md styles/prism.md styles/maquette.md styles/scoreboard.md styles/tokens/instrument-console.css styles/tokens/editorial-luxury.css styles/tokens/workbench.css styles/tokens/briefing-room.css styles/tokens/atrium.css styles/tokens/orchard.css styles/tokens/field-notes.css styles/tokens/cyclorama.css styles/tokens/showroom.css styles/tokens/blueprint.css styles/tokens/prism.css styles/tokens/maquette.css styles/tokens/scoreboard.css styles/datasheet.md styles/tokens/datasheet.css styles/manpage.md styles/tokens/manpage.css styles/pigeonhole.md styles/tokens/pigeonhole.css styles/roster.md styles/tokens/roster.css styles/ora.md styles/tokens/ora.css styles/tenor.md styles/tokens/tenor.css; do
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
