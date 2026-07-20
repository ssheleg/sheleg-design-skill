#!/bin/sh
# POSIX fallback installer for the SHELEG Design skill (no Node required).
# Usage: ./install.sh [target-dir]   (default: .cursor/skills/sheleg-design)
# From the web:
#   curl -fsSL https://raw.githubusercontent.com/ssheleg/sheleg-design-skill/main/install.sh | sh
set -eu

RAW="https://raw.githubusercontent.com/ssheleg/sheleg-design-skill/main/plugins/sheleg-design/skills/sheleg-design"
TARGET="${1:-.cursor/skills/sheleg-design}"
SRC_DIR="$(CDPATH= cd -- "$(dirname -- "$0")" 2>/dev/null && pwd)/plugins/sheleg-design/skills/sheleg-design"

mkdir -p "$TARGET" "$TARGET/styles"

for f in SKILL.md SHELEG_DESIGN.md styles/instrument-console.md styles/editorial-luxury.md styles/workbench.md; do
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
