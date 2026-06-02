#!/bin/bash
# Project Vault — Cross-platform Obsidian link setup v2
# Auto-detects OS, creates correct link type, configures Graph View colors
#
# Usage: bash setup-obsidian-link.sh <project-vault-path> [display-name]
# Example: bash setup-obsidian-link.sh docs/vault "My App"

set -e

PROJECT_VAULT="${1:?'Usage: setup-obsidian-link.sh <project-vault-path> [display-name]'}"
DISPLAY_NAME="${2:-$(basename "$PROJECT_VAULT")}"

# Resolve to absolute path
PROJECT_VAULT="$(cd "$PROJECT_VAULT" && pwd)"

# ============================================
# 1. PATH CHECK
# ============================================
if grep -qiE "(microsoft|wsl)" /proc/version 2>/dev/null; then
  IS_WSL=true
  if ! echo "$PROJECT_VAULT" | grep -qE "^/mnt/[cd]/"; then
    echo "❌ Project must be on Windows volume (/mnt/c/ or /mnt/d/) for Obsidian."
    echo "   Current path: $PROJECT_VAULT"
    echo ""
    echo "   Fix: cp -r $PROJECT_VAULT /mnt/d/C1/$(basename "$PROJECT_VAULT")"
    exit 1
  fi
else
  IS_WSL=false
fi

# ============================================
# 2. DETECT OBSIDIAN VAULT
# ============================================
if [ -n "$OBSIDIAN_VAULT" ]; then
  OBSIDIAN_DIR="$OBSIDIAN_VAULT"
elif [ "$(uname)" = "Darwin" ]; then
  for candidate in "$HOME/Documents/Obsidian Vault" "$HOME/Obsidian" "$HOME/Documents/Notes"; do
    if [ -d "$candidate/.obsidian" ]; then OBSIDIAN_DIR="$candidate"; break; fi
  done
elif [ -d "/mnt/c/Users/$USER/Documents/Obsidian Vault/.obsidian" ]; then
  OBSIDIAN_DIR="/mnt/c/Users/$USER/Documents/Obsidian Vault"
elif [ -d "/mnt/c/Users/guoku/Documents/Obsidian Vault/.obsidian" ]; then
  OBSIDIAN_DIR="/mnt/c/Users/guoku/Documents/Obsidian Vault"
else
  for candidate in "$HOME/Documents/Obsidian Vault" "$HOME/Obsidian" "$HOME/Notes"; do
    if [ -d "$candidate/.obsidian" ]; then OBSIDIAN_DIR="$candidate"; break; fi
  done
fi

if [ -z "$OBSIDIAN_DIR" ]; then
  echo "❌ Could not find Obsidian vault. Set OBSIDIAN_VAULT env."
  exit 1
fi

echo "📁 Obsidian vault: $OBSIDIAN_DIR"
echo "📁 Project vault:  $PROJECT_VAULT"
echo "📎 Display name:   $DISPLAY_NAME"

# ============================================
# 3. CREATE PROJECTS DIRECTORY
# ============================================
mkdir -p "$OBSIDIAN_DIR/Projects"
LINK_PATH="$OBSIDIAN_DIR/Projects/$DISPLAY_NAME"

# ============================================
# 4. CREATE LINK
# ============================================
if [ "$IS_WSL" = true ]; then
  echo "🔍 Detected: WSL + Windows"
  WIN_OBSIDIAN=$(wslpath -w "$OBSIDIAN_DIR" 2>/dev/null || echo "$OBSIDIAN_DIR" | sed 's|/mnt/c/|C:\\|;s|/mnt/d/|D:\\|;s|/|\\|g')
  WIN_PROJECT=$(wslpath -w "$PROJECT_VAULT" 2>/dev/null || echo "$PROJECT_VAULT" | sed 's|/mnt/c/|C:\\|;s|/mnt/d/|D:\\|;s|/|\\|g')
  WIN_LINK="$WIN_OBSIDIAN\\Projects\\$DISPLAY_NAME"

  if [ -e "$LINK_PATH" ]; then
    powershell.exe -Command "cmd /c rmdir '$WIN_LINK'" 2>/dev/null || rm -rf "$LINK_PATH"
  fi
  powershell.exe -Command "cmd /c mklink /J '$WIN_LINK' '$WIN_PROJECT'" 2>&1

elif [ "$(uname)" = "Darwin" ] || [ "$(uname)" = "Linux" ]; then
  echo "🔍 Detected: $(uname)"
  if [ -e "$LINK_PATH" ]; then rm -rf "$LINK_PATH"; fi
  ln -s "$PROJECT_VAULT" "$LINK_PATH"
fi

if [ -d "$LINK_PATH" ]; then
  echo "✅ Link created!"
else
  echo "❌ Link creation failed."
  exit 1
fi

# ============================================
# 5. CLEAN UP OBSIDIAN DEFAULT FILES
# ============================================
for junk in "欢迎.md" "未命名.base"; do
  if [ -f "$OBSIDIAN_DIR/$junk" ]; then
    rm "$OBSIDIAN_DIR/$junk"
    echo "🗑️  Removed default: $junk"
  fi
done

# ============================================
# 6. CONFIGURE GRAPH VIEW COLOR
# ============================================
echo ""
echo "🎨 Configuring Graph View color..."

GRAPH_CONFIG="$OBSIDIAN_DIR/.obsidian/graph.json"
if [ -f "$GRAPH_CONFIG" ]; then
  # Check if this project already has a color
  if ! grep -q "$DISPLAY_NAME" "$GRAPH_CONFIG" 2>/dev/null; then
    # Generate consistent color from project name hash
    HASH=$(echo -n "$DISPLAY_NAME" | md5sum | head -c 6)
    R=$((16#${HASH:0:2}))
    G=$((16#${HASH:2:2}))
    B=$((16#${HASH:4:2}))
    # Ensure minimum brightness (visible on dark background)
    R=$(( (R * 3 + 255) / 4 ))
    G=$(( (G * 3 + 255) / 4 ))
    B=$(( (B * 3 + 255) / 4 ))
    DECIMAL_RGB=$((R * 65536 + G * 256 + B))

    python3 -c "
import json
with open('$GRAPH_CONFIG', 'r') as f:
    config = json.load(f)
if 'colorGroups' not in config:
    config['colorGroups'] = []
config['colorGroups'].append({
    'query': 'path:Projects/$DISPLAY_NAME',
    'color': {'a': 1, 'rgb': $DECIMAL_RGB}
})
config['collapse-color-groups'] = False
with open('$GRAPH_CONFIG', 'w') as f:
    json.dump(config, f, indent=2)
" 2>/dev/null && echo "  ✅ Color group added (RGB: $DECIMAL_RGB)" || echo "  ⚠️  Could not auto-configure color"
  else
    echo "  ✅ Color group already exists"
  fi
else
  echo "  ⚠️  graph.json not found — open Obsidian once, then re-run"
fi

# ============================================
# 7. VERIFY
# ============================================
echo ""
echo "=== Verification ==="
FILE_COUNT=$(ls "$LINK_PATH" 2>/dev/null | wc -l)
echo "Files visible: $FILE_COUNT"

if [ "$FILE_COUNT" -gt 0 ]; then
  echo ""
  echo "✅ Setup complete!"
  echo ""
  echo "  In Obsidian:"
  echo "  - Left sidebar: Projects/$DISPLAY_NAME"
  echo "  - Graph View (Ctrl+G): colored by project"
  echo "  - Each project has a unique color"
else
  echo "⚠️  Link exists but no files visible."
fi
