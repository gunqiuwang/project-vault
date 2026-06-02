#!/bin/bash
# Agent Vault — Cross-platform Obsidian symlink setup
# Detects OS and creates the correct link type
#
# Usage: bash setup-obsidian-link.sh [project-path] [display-name]
# Example: bash setup-obsidian-link.sh ~/projects/my-app "My App"
#
# If OBSIDIAN_VAULT env is set, uses that. Otherwise auto-detects.

set -e

PROJECT_VAULT="${1:?'Usage: setup-obsidian-link.sh <project-vault-path> [display-name]'}"
DISPLAY_NAME="${2:-$(basename "$PROJECT_VAULT")}"

# Resolve to absolute path
PROJECT_VAULT="$(cd "$PROJECT_VAULT" && pwd)"

# --- Detect Obsidian vault path ---
if [ -n "$OBSIDIAN_VAULT" ]; then
  OBSIDIAN_DIR="$OBSIDIAN_VAULT"
elif [ "$(uname)" = "Darwin" ]; then
  # macOS: common locations
  for candidate in "$HOME/Documents/Obsidian Vault" "$HOME/Obsidian" "$HOME/Documents/Notes"; do
    if [ -d "$candidate/.obsidian" ]; then
      OBSIDIAN_DIR="$candidate"
      break
    fi
  done
elif [ -d "/mnt/c/Users/$USER/Documents/Obsidian Vault/.obsidian" ]; then
  # WSL: check Windows path
  OBSIDIAN_DIR="/mnt/c/Users/$USER/Documents/Obsidian Vault"
else
  # Linux: common locations
  for candidate in "$HOME/Documents/Obsidian Vault" "$HOME/Obsidian" "$HOME/Notes"; do
    if [ -d "$candidate/.obsidian" ]; then
      OBSIDIAN_DIR="$candidate"
      break
    fi
  done
fi

if [ -z "$OBSIDIAN_DIR" ]; then
  echo "❌ Could not find Obsidian vault. Set OBSIDIAN_VAULT env or create a vault first."
  echo "   Example: export OBSIDIAN_VAULT=~/Documents/MyVault"
  exit 1
fi

echo "📁 Obsidian vault: $OBSIDIAN_DIR"
echo "📁 Project vault:  $PROJECT_VAULT"
echo "📎 Display name:   $DISPLAY_NAME"

# Create Projects directory
mkdir -p "$OBSIDIAN_DIR/Projects"
LINK_PATH="$OBSIDIAN_DIR/Projects/$DISPLAY_NAME"

# --- Create link based on platform ---

# Check if running inside WSL
if grep -qiE "(microsoft|wsl)" /proc/version 2>/dev/null; then
  # WSL: use Windows junction via PowerShell
  echo "🔍 Detected: WSL + Windows"

  # Convert WSL paths to Windows paths
  WIN_OBSIDIAN=$(wslpath -w "$OBSIDIAN_DIR" 2>/dev/null || echo "$OBSIDIAN_DIR" | sed 's|/mnt/c/|C:\\|' | sed 's|/|\\|g')
  WIN_PROJECT=$(wslpath -w "$PROJECT_VAULT" 2>/dev/null || echo "$PROJECT_VAULT" | sed 's|/mnt/c/|C:\\|' | sed 's|/|\\|g')
  WIN_LINK="$WIN_OBSIDIAN\\Projects\\$DISPLAY_NAME"

  # Remove existing link if present
  if [ -e "$LINK_PATH" ]; then
    echo "🗑️  Removing existing link..."
    powershell.exe -Command "cmd /c rmdir '$WIN_LINK'" 2>/dev/null || rm -rf "$LINK_PATH"
  fi

  # Create junction (no admin required)
  powershell.exe -Command "cmd /c mklink /J '$WIN_LINK' '$WIN_PROJECT'" 2>&1

  if [ -d "$LINK_PATH" ]; then
    echo "✅ Junction created successfully!"
  else
    echo "❌ Junction creation failed. Try running from PowerShell as admin:"
    echo "   mklink /J \"$WIN_LINK\" \"$WIN_PROJECT\""
    exit 1
  fi

elif [ "$(uname)" = "Darwin" ]; then
  # macOS: regular symlink
  echo "🔍 Detected: macOS"

  if [ -e "$LINK_PATH" ]; then
    echo "🗑️  Removing existing link..."
    rm -rf "$LINK_PATH"
  fi

  ln -s "$PROJECT_VAULT" "$LINK_PATH"

  if [ -L "$LINK_PATH" ]; then
    echo "✅ Symlink created successfully!"
  else
    echo "❌ Symlink creation failed."
    exit 1
  fi

elif [ "$(uname)" = "Linux" ]; then
  # Native Linux: regular symlink
  echo "🔍 Detected: Linux"

  if [ -e "$LINK_PATH" ]; then
    echo "🗑️  Removing existing link..."
    rm -rf "$LINK_PATH"
  fi

  ln -s "$PROJECT_VAULT" "$LINK_PATH"

  if [ -L "$LINK_PATH" ]; then
    echo "✅ Symlink created successfully!"
  else
    echo "❌ Symlink creation failed."
    exit 1
  fi

else
  echo "❌ Unknown platform: $(uname)"
  echo "   Manual setup needed. Create a symlink/junction from:"
  echo "   $OBSIDIAN_DIR/Projects/$DISPLAY_NAME"
  echo "   → $PROJECT_VAULT"
  exit 1
fi

# --- Add color group to Obsidian graph config ---
echo ""
echo "🎨 Configuring Graph View color..."

GRAPH_CONFIG="$OBSIDIAN_DIR/.obsidian/graph.json"
if [ -f "$GRAPH_CONFIG" ]; then
  # Generate a random color (hue-based, distinct per project)
  # Use hash of display name for consistent color
  HASH=$(echo -n "$DISPLAY_NAME" | md5sum | head -c 6)
  R=$((16#${HASH:0:2}))
  G=$((16#${HASH:2:2}))
  B=$((16#${HASH:4:2}))
  # Ensure minimum brightness
  R=$((R < 100 ? R + 100 : R))
  G=$((G < 100 ? G + 100 : G))
  B=$((B < 100 ? B + 100 : B))
  DECIMAL_RGB=$((R * 65536 + G * 256 + B))

  # Check if this project already has a color group
  if ! grep -q "$DISPLAY_NAME" "$GRAPH_CONFIG" 2>/dev/null; then
    # Add color group using python (available on most systems)
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

# Verify
echo ""
echo "=== Verification ==="
FILE_COUNT=$(ls "$LINK_PATH" 2>/dev/null | wc -l)
echo "Files visible through link: $FILE_COUNT"

if [ "$FILE_COUNT" -gt 0 ]; then
  echo ""
  echo "✅ Setup complete! Open Obsidian and check:"
  echo "   Projects/$DISPLAY_NAME in the left sidebar"
  echo "   Graph View (Ctrl+G) to see the hub structure"
else
  echo "⚠️  Link exists but no files visible. Check permissions."
fi
