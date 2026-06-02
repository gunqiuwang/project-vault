#!/bin/bash
# Project Vault — Audit Script
# 10-point health check on your vault
#
# Usage: bash audit-vault.sh [project-path]

set -e
PROJECT_PATH="${1:-.}"
cd "$PROJECT_PATH"

if [ ! -d "docs/vault" ]; then
  echo "❌ No vault found. Run init-vault.sh first."
  exit 1
fi

TODAY=$(date +%Y-%m-%d)
PASS=0
WARN=0
FAIL=0

echo "=========================================="
echo "  Project Vault Audit"
echo "=========================================="
echo "  Path: $(pwd)"
echo "  Date: $TODAY"
echo "=========================================="
echo ""

# --- Check 1: Existence ---
echo "1. Existence Check"
REQUIRED_FILES="00_HOME 01_CURRENT_BASELINE 02_DECISION_LOG 03_DO_NOT_TOUCH 04_ARCHITECTURE 05_COMMANDS_AND_FILES 06_DEPLOYMENT 07_TESTING_AND_VERIFICATION 08_INCIDENTS_AND_FIXES 09_AGENT_PROMPTS 10_REPORT_INDEX VAULT_SCHEMA VAULT_CHANGELOG"
for f in $REQUIRED_FILES; do
  if [ -f "docs/vault/${f}.md" ]; then
    echo "  ✅ ${f}.md"
  else
    echo "  ❌ ${f}.md MISSING"
    FAIL=$((FAIL + 1))
  fi
done
PASS=$((PASS + 1))
echo ""

# --- Check 2: Baseline freshness ---
echo "2. Baseline Freshness"
BASELINE_HEAD=$(grep -oP '(?<=`)[a-f0-9]{7}' docs/vault/01_CURRENT_BASELINE.md 2>/dev/null | head -1)
ACTUAL_HEAD=$(git rev-parse --short HEAD 2>/dev/null || echo "unknown")
if [ "$BASELINE_HEAD" = "$ACTUAL_HEAD" ]; then
  echo "  ✅ Baseline HEAD matches: $ACTUAL_HEAD"
  PASS=$((PASS + 1))
else
  echo "  ❌ Baseline HEAD ($BASELINE_HEAD) ≠ actual ($ACTUAL_HEAD)"
  FAIL=$((FAIL + 1))
fi
echo ""

# --- Check 3: Metadata compliance ---
echo "3. Metadata Compliance"
MISSING_META=0
for f in docs/vault/*.md; do
  fname=$(basename "$f")
  has_type=$(head -10 "$f" | grep -c "type:" || true)
  has_conf=$(head -10 "$f" | grep -c "confidence:" || true)
  has_updated=$(head -10 "$f" | grep -c "last_updated:" || true)
  has_reviewed=$(head -10 "$f" | grep -c "reviewed_by:" || true)
  if [ "$has_type" -ge 1 ] && [ "$has_conf" -ge 1 ] && [ "$has_updated" -ge 1 ] && [ "$has_reviewed" -ge 1 ]; then
    :
  else
    echo "  ⚠️  $fname — missing metadata fields"
    MISSING_META=$((MISSING_META + 1))
  fi
done
if [ "$MISSING_META" -eq 0 ]; then
  echo "  ✅ All files have full metadata"
  PASS=$((PASS + 1))
else
  echo "  ⚠️  $MISSING_META files missing metadata"
  WARN=$((WARN + 1))
fi
echo ""

# --- Check 4: Confidence audit ---
echo "4. Confidence Audit"
LOW_CONF=$(grep -l "confidence: low" docs/vault/*.md 2>/dev/null | wc -l)
HIGH_CONF=$(grep -l "confidence: high" docs/vault/*.md 2>/dev/null | wc -l)
TOTAL_FILES=$(ls docs/vault/*.md 2>/dev/null | wc -l)
echo "  High: $HIGH_CONF / $TOTAL_FILES"
echo "  Low:  $LOW_CONF / $TOTAL_FILES"
if [ "$LOW_CONF" -gt 0 ]; then
  echo "  ⚠️  Files with low confidence:"
  grep -l "confidence: low" docs/vault/*.md 2>/dev/null | while read -r f; do
    echo "    - $(basename "$f")"
  done
  WARN=$((WARN + 1))
else
  echo "  ✅ No low-confidence files"
  PASS=$((PASS + 1))
fi
echo ""

# --- Check 5: Review audit ---
echo "5. Review Audit"
UNREVIEWED=$(grep -l "reviewed_by: unreviewed" docs/vault/*.md 2>/dev/null | wc -l)
HUMAN_REVIEWED=$(grep -l "reviewed_by: human" docs/vault/*.md 2>/dev/null | wc -l)
echo "  Human reviewed: $HUMAN_REVIEWED / $TOTAL_FILES"
echo "  Unreviewed: $UNREVIEWED / $TOTAL_FILES"
if [ "$UNREVIEWED" -gt 0 ]; then
  echo "  ⚠️  Unreviewed files:"
  grep -l "reviewed_by: unreviewed" docs/vault/*.md 2>/dev/null | while read -r f; do
    echo "    - $(basename "$f")"
  done
  WARN=$((WARN + 1))
else
  echo "  ✅ All files reviewed"
  PASS=$((PASS + 1))
fi
echo ""

# --- Check 6: Aliases ---
echo "6. Aliases (Graph View)"
if grep -q "aliases:" docs/vault/00_HOME.md 2>/dev/null; then
  ALIAS=$(grep "aliases:" docs/vault/00_HOME.md | head -1)
  echo "  ✅ $ALIAS"
  PASS=$((PASS + 1))
else
  echo "  ❌ No aliases in 00_HOME.md — Graph View will show generic '00_HOME'"
  FAIL=$((FAIL + 1))
fi
echo ""

# --- Check 7: .gitignore ---
echo "7. .gitignore"
if [ -f ".gitignore" ]; then
  if grep -q "^\.env" .gitignore 2>/dev/null; then
    echo "  ✅ .gitignore exists with .env rule"
    PASS=$((PASS + 1))
  else
    echo "  ⚠️  .gitignore exists but missing .env rule"
    WARN=$((WARN + 1))
  fi
else
  echo "  ❌ No .gitignore"
  FAIL=$((FAIL + 1))
fi
echo ""

# --- Check 8: Reports directory ---
echo "8. Reports Directory"
if [ -d "assets/intake/reports" ]; then
  REPORT_COUNT=$(ls assets/intake/reports/*.md 2>/dev/null | wc -l)
  echo "  ✅ assets/intake/reports/ exists ($REPORT_COUNT reports)"
  PASS=$((PASS + 1))
else
  echo "  ⚠️  assets/intake/reports/ missing"
  WARN=$((WARN + 1))
fi
echo ""

# --- Check 9: Vault score ---
echo "9. Vault Score"
CONF=$((HIGH_CONF * 100 / TOTAL_FILES))
FRESH=100
COMP=$((TOTAL_FILES * 100 / 13))
REV=$((HUMAN_REVIEWED * 100 / TOTAL_FILES))
SCORE=$((CONF * 35 / 100 + FRESH * 30 / 100 + COMP * 20 / 100 + REV * 15 / 100))
echo "  Confidence:  $CONF%"
echo "  Freshness:   $FRESH%"
echo "  Completeness: $COMP%"
echo "  Review:      $REV%"
echo ""
if [ "$SCORE" -ge 90 ]; then echo "  🟢 SCORE: $SCORE / 100 — Excellent"
elif [ "$SCORE" -ge 70 ]; then echo "  🟡 SCORE: $SCORE / 100 — Good"
elif [ "$SCORE" -ge 50 ]; then echo "  🟠 SCORE: $SCORE / 100 — Needs work"
else echo "  🔴 SCORE: $SCORE / 100 — Critical"
fi
echo ""

# --- Check 10: Obsidian connection ---
echo "10. Obsidian Connection"
if [ -L "/mnt/c/Users/guoku/Documents/Obsidian Vault/Projects/"* ] 2>/dev/null; then
  echo "  ✅ Obsidian junction exists"
  PASS=$((PASS + 1))
else
  echo "  ⚠️  No Obsidian connection detected"
  WARN=$((WARN + 1))
fi
echo ""

# --- Summary ---
echo "=========================================="
echo "  Audit Summary"
echo "=========================================="
echo "  ✅ Pass: $PASS"
echo "  ⚠️  Warn: $WARN"
echo "  ❌ Fail: $FAIL"
echo ""

if [ "$FAIL" -eq 0 ] && [ "$WARN" -eq 0 ]; then
  echo "  Overall: 🟢 HEALTHY"
elif [ "$FAIL" -eq 0 ]; then
  echo "  Overall: 🟡 GOOD (some warnings)"
else
  echo "  Overall: 🔴 NEEDS ATTENTION"
fi
echo ""
