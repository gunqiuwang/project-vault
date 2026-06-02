#!/bin/bash
# Project Vault — Sync Script
# Scans recent git changes and suggests which vault files to update
#
# Usage: bash sync-vault.sh [project-path]

set -e
PROJECT_PATH="${1:-.}"
cd "$PROJECT_PATH"

if [ ! -d "docs/vault" ]; then
  echo "❌ No vault found. Run init-vault.sh first."
  exit 1
fi

echo "=========================================="
echo "  Project Vault Sync"
echo "=========================================="
echo ""

# Check what changed since last vault update
LAST_VAULT_COMMIT=$(git log --oneline --all -- docs/vault/ | head -1 | awk '{print $1}')
if [ -z "$LAST_VAULT_COMMIT" ]; then
  echo "⚠️  No vault commits found. Running full scan."
  CHANGED_FILES=$(git diff --name-only HEAD~10 HEAD 2>/dev/null || git diff --name-only HEAD 2>/dev/null)
else
  echo "Last vault update: $LAST_VAULT_COMMIT"
  CHANGED_FILES=$(git diff --name-only "$LAST_VAULT_COMMIT" HEAD 2>/dev/null)
fi

if [ -z "$CHANGED_FILES" ]; then
  echo "✅ No changes since last vault update. Vault is current."
  exit 0
fi

echo ""
echo "📝 Changes detected since last vault update:"
echo "$CHANGED_FILES" | head -20
TOTAL=$(echo "$CHANGED_FILES" | wc -l)
[ "$TOTAL" -gt 20 ] && echo "  ... and $((TOTAL - 20)) more"
echo ""

# Analyze which vault files need updating
NEEDS_UPDATE=""

# Check for architecture changes
if echo "$CHANGED_FILES" | grep -qE "(package\.json|requirements\.txt|Cargo\.toml|go\.mod|Dockerfile|docker-compose)"; then
  NEEDS_UPDATE="$NEEDS_UPDATE 04_ARCHITECTURE.md\n"
  echo "🟡 Tech stack changed → update 04_ARCHITECTURE.md"
fi

# Check for new commands
if echo "$CHANGED_FILES" | grep -qE "(package\.json|Makefile|scripts/)"; then
  NEEDS_UPDATE="$NEEDS_UPDATE 05_COMMANDS_AND_FILES.md\n"
  echo "🟡 Commands changed → update 05_COMMANDS_AND_FILES.md"
fi

# Check for deploy changes
if echo "$CHANGED_FILES" | grep -qE "(Dockerfile|docker-compose|\.github/workflows|vercel\.json|wrangler)"; then
  NEEDS_UPDATE="$NEEDS_UPDATE 06_DEPLOYMENT.md\n"
  echo "🟡 Deploy config changed → update 06_DEPLOYMENT.md"
fi

# Check for new test files
if echo "$CHANGED_FILES" | grep -qE "(\.test\.|\.spec\.|__tests__)"; then
  NEEDS_UPDATE="$NEEDS_UPDATE 07_TESTING_AND_VERIFICATION.md\n"
  echo "🟡 Tests changed → update 07_TESTING_AND_VERIFICATION.md"
fi

# Check for incident fixes
if echo "$CHANGED_FILES" | grep -qE "(fix|hotfix|patch)"; then
  echo "🟠 Fix detected → consider adding to 08_INCIDENTS_AND_FIXES.md"
fi

# Check for new dependencies
if echo "$CHANGED_FILES" | grep -qE "(package-lock|yarn\.lock|pnpm-lock|Pipfile\.lock)"; then
  echo "🟡 Dependencies changed → update 04_ARCHITECTURE.md"
fi

# Always update baseline
NEEDS_UPDATE="$NEEDS_UPDATE 01_CURRENT_BASELINE.md\n"
echo "🟡 Baseline always needs update → 01_CURRENT_BASELINE.md"

# Always update changelog
echo "🟡 Always append → VAULT_CHANGELOG.md"

echo ""
echo "=========================================="
echo "  Recommended Actions"
echo "=========================================="
echo ""
echo -e "$NEEDS_UPDATE" | sort -u | while read -r f; do
  [ -n "$f" ] && echo "  → Update docs/vault/$f"
done
echo ""
echo "  → Append entry to docs/vault/VAULT_CHANGELOG.md"
echo "  → git add docs/vault/ && git commit -m 'docs: sync vault'"
echo ""

# Offer to auto-update baseline
CURRENT_BRANCH=$(git branch --show-current 2>/dev/null || echo "unknown")
CURRENT_HEAD=$(git rev-parse --short HEAD 2>/dev/null || echo "unknown")
CURRENT_MSG=$(git log --oneline -1 2>/dev/null || echo "unknown")
TODAY=$(date +%Y-%m-%d)

echo "Auto-update 01_CURRENT_BASELINE.md? (updates branch/commit/date)"
echo "  Branch: $CURRENT_BRANCH"
echo "  HEAD: $CURRENT_HEAD"
echo "  Date: $TODAY"
echo ""
echo "Run: bash sync-vault.sh --auto $PROJECT_PATH  to auto-update"
