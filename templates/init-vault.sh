#!/bin/bash
# Project Vault — Automated Initialization Script v2
# Usage: bash init-vault.sh [project-path] [project-name] [phase]
# Example: bash init-vault.sh . "My App" mvp
#
# Phases: idea | prototype | mvp | growth | maintenance | sunset
# If phase is omitted, auto-detects based on project files.

set -e

PROJECT_PATH="${1:-.}"
PROJECT_NAME="${2:-$(basename "$(cd "$PROJECT_PATH" && pwd)")}"
PHASE="${3:-auto}"

cd "$PROJECT_PATH"
PROJECT_ROOT="$(pwd)"

# ============================================
# 0. PATH CHECK — WSL must be on Windows volume
# ============================================
ON_WINDOWS_VOLUME=false
if echo "$PROJECT_ROOT" | grep -qE "^/mnt/[cd]/"; then
  ON_WINDOWS_VOLUME=true
fi

if grep -qiE "(microsoft|wsl)" /proc/version 2>/dev/null; then
  IS_WSL=true
  if [ "$ON_WINDOWS_VOLUME" = false ]; then
    echo "⚠️  WARNING: Project is on WSL filesystem ($PROJECT_ROOT)"
    echo "   Obsidian on Windows cannot access WSL-only paths."
    echo "   Move project to /mnt/c/ or /mnt/d/ first:"
    echo ""
    echo "   cp -r $PROJECT_ROOT /mnt/d/C1/$(basename "$PROJECT_ROOT")"
    echo ""
    read -p "   Continue anyway? (y/N) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
      echo "Aborted. Move the project first."
      exit 1
    fi
  fi
else
  IS_WSL=false
fi

# ============================================
# 1. AUTO-DETECT PHASE
# ============================================
if [ "$PHASE" = "auto" ]; then
  if [ -f "package.json" ] || [ -f "requirements.txt" ] || [ -f "pyproject.toml" ] || [ -f "Cargo.toml" ] || [ -f "go.mod" ]; then
    if [ -d "src" ] || [ -d "app" ] || [ -d "lib" ] || [ -d "pages" ]; then
      PHASE="mvp"
    else
      PHASE="prototype"
    fi
  elif [ -f "index.html" ]; then
    PHASE="prototype"
  elif [ -d "assets" ] || [ -f "README.md" ] || [ -f "项目构想.md" ]; then
    PHASE="idea"
  else
    PHASE="idea"
  fi
  echo "🔍 Auto-detected phase: $PHASE"
fi

TODAY=$(date +%Y-%m-%d)

echo ""
echo "=========================================="
echo "  Project Vault Init v2"
echo "=========================================="
echo "  Project:  $PROJECT_NAME"
echo "  Path:     $PROJECT_ROOT"
echo "  Phase:    $PHASE"
echo "  Date:     $TODAY"
echo "  WSL:      $IS_WSL"
echo "  Windows:  $ON_WINDOWS_VOLUME"
echo "=========================================="
echo ""

# ============================================
# 2. CREATE DIRECTORIES
# ============================================
mkdir -p docs/vault/templates
mkdir -p assets/intake/reports
echo "✅ Directories created"

# ============================================
# 3. .GITIGNORE HANDLING
# ============================================
if [ ! -f ".gitignore" ]; then
  cat > .gitignore << 'GITIGNORE'
# Dependencies
node_modules/
venv/
.venv/
__pycache__/

# Environment
.env
.env.local

# IDE
.idea/
.vscode/

# OS
.DS_Store
Thumbs.db

# Build
dist/
build/
.next/

# Logs
*.log
GITIGNORE
  echo "✅ .gitignore created (was missing)"
else
  if ! grep -q "^\.env" .gitignore 2>/dev/null; then
    echo "" >> .gitignore
    echo "# Environment" >> .gitignore
    echo ".env" >> .gitignore
    echo ".env.local" >> .gitignore
    echo "✅ .gitignore updated (added .env)"
  else
    echo "✅ .gitignore exists"
  fi
fi

# ============================================
# 4. SCAN PROJECT — Read the "soul"
# ============================================
echo "🔍 Scanning project..."

# Git info
BRANCH=$(git branch --show-current 2>/dev/null || echo "unknown")
COMMIT_SHORT=$(git rev-parse --short HEAD 2>/dev/null || echo "no commits")
COMMIT_MSG=$(git log --oneline -1 2>/dev/null || echo "no commits")
RECENT_COMMITS=$(git log --oneline -5 2>/dev/null || echo "no commits")

# --- Tech stack detection (multi-stack aware) ---
FRONTEND_STACK="Unknown"
BACKEND_STACK=""
IS_FULLSTACK=false

# Frontend detection
if [ -f "miniprogram/app.json" ] || [ -f "project.config.json" ]; then
  FRONTEND_STACK="WeChat Mini Program"
elif [ -f "package.json" ]; then
  if grep -q "react" package.json 2>/dev/null; then FRONTEND_STACK="React"
  elif grep -q "vue" package.json 2>/dev/null; then FRONTEND_STACK="Vue"
  elif grep -q "next" package.json 2>/dev/null; then FRONTEND_STACK="Next.js"
  elif grep -q "express" package.json 2>/dev/null; then FRONTEND_STACK="Express"
  else FRONTEND_STACK="Node.js"
  fi
elif [ -f "index.html" ]; then FRONTEND_STACK="HTML/CSS/JS"
fi

# Backend detection
if [ -d "backend" ] && [ -f "backend/requirements.txt" ]; then
  IS_FULLSTACK=true
  if grep -q "fastapi" backend/requirements.txt 2>/dev/null; then BACKEND_STACK="FastAPI"
  elif grep -q "django" backend/requirements.txt 2>/dev/null; then BACKEND_STACK="Django"
  elif grep -q "flask" backend/requirements.txt 2>/dev/null; then BACKEND_STACK="Flask"
  else BACKEND_STACK="Python"
  fi
elif [ -d "backend" ] && [ -f "backend/package.json" ]; then
  IS_FULLSTACK=true
  BACKEND_STACK="Node.js"
elif [ -f "requirements.txt" ] || [ -f "pyproject.toml" ]; then
  if grep -q "fastapi" requirements.txt pyproject.toml 2>/dev/null; then BACKEND_STACK="FastAPI"
  elif grep -q "django" requirements.txt pyproject.toml 2>/dev/null; then BACKEND_STACK="Django"
  elif grep -q "flask" requirements.txt pyproject.toml 2>/dev/null; then BACKEND_STACK="Flask"
  else BACKEND_STACK="Python"
  fi
elif [ -f "Cargo.toml" ]; then BACKEND_STACK="Rust"
elif [ -f "go.mod" ]; then BACKEND_STACK="Go"
fi

if [ "$IS_FULLSTACK" = true ]; then
  TECH_STACK="$FRONTEND_STACK + $BACKEND_STACK"
else
  TECH_STACK="$FRONTEND_STACK"
fi
[ "$BACKEND_STACK" != "" ] && TECH_STACK="${FRONTEND_STACK} + ${BACKEND_STACK}"
echo "  Tech stack: $TECH_STACK"
echo "  Full-stack: $IS_FULLSTACK"

# --- Scan ALL asset directories (not just assets/) ---
ASSET_COUNT=0
AUDIO_COUNT=0
IMAGE_COUNT=0
STORY_COUNT=0
TAROT_COUNT=0

for asset_dir in assets miniprogram/images miniprogram/assets public/images static/images; do
  if [ -d "$asset_dir" ]; then
    count=$(find "$asset_dir" -type f 2>/dev/null | wc -l)
    ASSET_COUNT=$((ASSET_COUNT + count))
    AUDIO_COUNT=$((AUDIO_COUNT + $(find "$asset_dir" -name "*.wav" -o -name "*.mp3" -o -name "*.ogg" 2>/dev/null | wc -l)))
    IMAGE_COUNT=$((IMAGE_COUNT + $(find "$asset_dir" -name "*.png" -o -name "*.jpg" -o -name "*.webp" -o -name "*.svg" -o -name "*.jpeg" 2>/dev/null | wc -l)))
    STORY_COUNT=$((STORY_COUNT + $(find "$asset_dir" -name "*.meta.json" 2>/dev/null | wc -l)))
  fi
done

# Tarot-specific detection
if [ -d "miniprogram/images/tarot" ]; then
  TAROT_COUNT=$(find miniprogram/images/tarot -type f 2>/dev/null | wc -l)
  echo "  Tarot cards: $TAROT_COUNT"
fi

echo "  Assets: $ASSET_COUNT files ($AUDIO_COUNT audio, $IMAGE_COUNT images, $STORY_COUNT content items)"

# --- Scan source files (exclude venv/node_modules/.git) ---
SOURCE_COUNT=$(find . -type f \( -name "*.js" -o -name "*.ts" -o -name "*.py" -o -name "*.rs" -o -name "*.go" -o -name "*.wxml" -o -name "*.wxss" -o -name "*.html" -o -name "*.css" -o -name "*.vue" -o -name "*.jsx" -o -name "*.tsx" \) ! -path "*/.git/*" ! -path "*/node_modules/*" ! -path "*/venv/*" ! -path "*/__pycache__/*" ! -path "*/.venv/*" 2>/dev/null | wc -l)
echo "  Source files: $SOURCE_COUNT"

# --- Scan design files ---
DESIGN_COUNT=0
DESIGN_FILES=""
if [ -d "design" ]; then
  DESIGN_COUNT=$(find design -name "*.html" -o -name "*.fig" -o -name "*.sketch" 2>/dev/null | wc -l)
  DESIGN_FILES=$(find design -name "*.html" -type f 2>/dev/null | head -5 | xargs -I{} basename {} .html)
  echo "  Design files: $DESIGN_COUNT ($DESIGN_FILES)"
fi

# --- Scan documentation files ---
DOC_FILES=""
for doc in README.md "项目构想.md" PRD.md "设计文档.md" PROJECT-REVIEW.md "brand-spec.md" "animation-spec.md" "database-api.md"; do
  if [ -f "$doc" ]; then
    DOC_FILES="$DOC_FILES $doc"
  fi
  # Also check in subdirectories
  find . -maxdepth 3 -name "$doc" ! -path "./.git/*" 2>/dev/null | while read -r f; do
    DOC_FILES="$DOC_FILES $f"
  done
done
echo "  Docs found:$DOC_FILES"

# --- Extract pages from WeChat app.json ---
PAGES=""
PAGE_COUNT=0
if [ -f "miniprogram/app.json" ]; then
  PAGES=$(python3 -c "
import json
with open('miniprogram/app.json') as f:
    d = json.load(f)
for p in d.get('pages',[]):
    print(p)
" 2>/dev/null || echo "")
  PAGE_COUNT=$(echo "$PAGES" | grep -c "/" 2>/dev/null || echo "0")
  echo "  Pages: $PAGE_COUNT detected"
elif [ -f "app.json" ]; then
  PAGES=$(python3 -c "
import json
with open('app.json') as f:
    d = json.load(f)
for p in d.get('pages',[]):
    print(p)
" 2>/dev/null || echo "")
  PAGE_COUNT=$(echo "$PAGES" | grep -c "/" 2>/dev/null || echo "0")
  echo "  Pages: $PAGE_COUNT detected"
fi

# --- Extract backend dependencies ---
BACKEND_DEPS=""
if [ -f "backend/requirements.txt" ]; then
  BACKEND_DEPS=$(cat backend/requirements.txt 2>/dev/null | grep -v "^#" | grep -v "^$" | sed 's/>=.*$//' | tr '\n' ', ' | sed 's/,$//')
  echo "  Backend deps: $BACKEND_DEPS"
elif [ -f "requirements.txt" ]; then
  BACKEND_DEPS=$(cat requirements.txt 2>/dev/null | grep -v "^#" | grep -v "^$" | sed 's/>=.*$//' | tr '\n' ', ' | sed 's/,$//')
  echo "  Backend deps: $BACKEND_DEPS"
fi

# --- Detect commands from package.json ---
COMMANDS_SAFE=""
if [ -f "package.json" ]; then
  COMMANDS_SAFE=$(python3 -c "
import json
with open('package.json') as f:
    d = json.load(f)
for k,v in d.get('scripts',{}).items():
    print(f'| \`npm run {k}\` | {v} | 🟢 Safe |')
" 2>/dev/null || echo "")
fi

# --- Detect sensitive patterns ---
SENSITIVE_PATTERNS=""
if [ -f ".env.example" ]; then
  SENSITIVE_PATTERNS=$(grep -oP '^[A-Z_]+=' .env.example 2>/dev/null | sed 's/=$//' | head -10 || true)
fi
if [ -f ".env" ]; then
  echo "  ⚠️  .env file exists — verify it's in .gitignore!"
fi

# --- Detect naming patterns ---
NAMING_PATTERN=""
if [ -d "assets" ]; then
  SAMPLE=$(find assets -name "*.meta.json" -type f 2>/dev/null | head -3 | xargs -I{} basename {} .meta.json)
  if [ -n "$SAMPLE" ]; then
    NAMING_PATTERN=$(echo "$SAMPLE" | head -1 | sed 's/[0-9]/X/g')
    echo "  Naming pattern: $NAMING_PATTERN"
  fi
fi

echo ""

# ============================================
# 5. GENERATE VAULT FILES
# ============================================
echo "📝 Generating vault files..."

# --- 00_HOME.md ---
cat > docs/vault/00_HOME.md << EOF
---
type: home
status: active
confidence: high
last_updated: $TODAY
owner: both
reviewed_by: unreviewed
aliases: ["$PROJECT_NAME", "$PROJECT_NAME Home"]
---

# $PROJECT_NAME — Project Vault

## Quick Facts

| Key | Value |
|-----|-------|
| **Project** | $PROJECT_NAME |
| **Phase** | $PHASE |
| **Tech Stack** | $TECH_STACK |
| **Full-stack** | $IS_FULLSTACK |
| **Branch** | $BRANCH |
| **Last Commit** | \`$COMMIT_SHORT\` |
| **Source Files** | $SOURCE_COUNT |
| **Assets** | $ASSET_COUNT files |
| **Last Updated** | $TODAY |
EOF

# Add content inventory if assets exist
if [ "$ASSET_COUNT" -gt 0 ]; then
cat >> docs/vault/00_HOME.md << EOF

## Content Inventory

| Category | Count |
|----------|-------|
| Total assets | $ASSET_COUNT |
| Images | $IMAGE_COUNT |
| Audio | $AUDIO_COUNT |
| Content items | $STORY_COUNT |
EOF
[ "$TAROT_COUNT" -gt 0 ] && echo "| Tarot cards | $TAROT_COUNT |" >> docs/vault/00_HOME.md
[ "$PAGE_COUNT" -gt 0 ] && echo "| Pages | $PAGE_COUNT |" >> docs/vault/00_HOME.md
[ "$DESIGN_COUNT" -gt 0 ] && echo "| Design files | $DESIGN_COUNT |" >> docs/vault/00_HOME.md
fi

# Add recent activity if available
if [ -n "$RECENT_COMMITS" ] && [ "$RECENT_COMMITS" != "no commits" ]; then
cat >> docs/vault/00_HOME.md << EOF

## Recent Activity

\`\`\`
$RECENT_COMMITS
\`\`\`
EOF
fi

cat >> docs/vault/00_HOME.md << EOF

## Agent Entry Page

> **Every new Agent MUST read this page first.**

1. [[00_HOME]] — You are here
2. [[01_CURRENT_BASELINE]] — Source of truth
3. [[03_DO_NOT_TOUCH]] — Danger zones
4. [[05_COMMANDS_AND_FILES]] — What you can run
5. [[VAULT_SCHEMA]] — Vault rules

**After completing any task, you MUST:**
- Update [[01_CURRENT_BASELINE]] if status changed
- Append to [[VAULT_CHANGELOG]]

## Source Documentation

EOF

# Auto-link discovered docs
if [ -n "$DOC_FILES" ]; then
  for doc in $DOC_FILES; do
    echo "- [[$doc]]" >> docs/vault/00_HOME.md
  done
else
  echo "- [ ] Link your planning docs here" >> docs/vault/00_HOME.md
fi

cat >> docs/vault/00_HOME.md << EOF

## Vault Navigation

- [[01_CURRENT_BASELINE]] — Current state
- [[02_DECISION_LOG]] — Key decisions
- [[03_DO_NOT_TOUCH]] — Danger zones
- [[04_ARCHITECTURE]] — Tech stack & data flow
- [[05_COMMANDS_AND_FILES]] — Commands & files
- [[06_DEPLOYMENT]] — Deploy process
- [[07_TESTING_AND_VERIFICATION]] — Testing
- [[08_INCIDENTS_AND_FIXES]] — Incidents
- [[09_AGENT_PROMPTS]] — Agent prompts
- [[10_REPORT_INDEX]] — Reports
- [[VAULT_SCHEMA]] — Vault rules
- [[VAULT_CHANGELOG]] — Vault log
EOF
echo "  ✅ 00_HOME.md"

# --- 01_CURRENT_BASELINE.md ---
cat > docs/vault/01_CURRENT_BASELINE.md << EOF
---
type: baseline
status: active
confidence: high
last_updated: $TODAY
owner: agent
reviewed_by: unreviewed
---

# Current Baseline

| Key | Value | Confidence |
|-----|-------|------------|
| **Branch** | $BRANCH | high |
| **HEAD** | \`$COMMIT_SHORT\` — $COMMIT_MSG | high |
| **Phase** | $PHASE | high |
| **Tech** | $TECH_STACK | high |
| **Source Files** | $SOURCE_COUNT | high |
| **Assets** | $ASSET_COUNT files | high |
| **Production** | Not deployed | medium |

## Capabilities

> Customize with what the project can do right now.

## Recently Completed

\`\`\`
$RECENT_COMMITS
\`\`\`

## Must NOT Regress

> List critical features that must never break.
EOF
echo "  ✅ 01_CURRENT_BASELINE.md"

# --- 02_DECISION_LOG.md ---
cat > docs/vault/02_DECISION_LOG.md << EOF
---
type: decision-log
status: active
confidence: high
last_updated: $TODAY
owner: both
reviewed_by: unreviewed
---

# Decision Log

> Record important decisions here. Newest first.

## Decision: {TITLE}

**Date:** $TODAY | **Status:** Proposed
**Decision:** {What was decided}
**Why:** {Why}
**Do not reverse unless:** {Conditions}
EOF
echo "  ✅ 02_DECISION_LOG.md"

# --- 03_DO_NOT_TOUCH.md ---
cat > docs/vault/03_DO_NOT_TOUCH.md << EOF
---
type: danger-zones
status: active
confidence: high
last_updated: $TODAY
owner: human
reviewed_by: human
---

# DO NOT TOUCH

## Files That Must NOT Be Changed Casually

| File | Why | Who Can Change |
|------|-----|---------------|
| {FILE} | {REASON} | {APPROVER} |

## Security Rules

**Never include in any vault file:**
- API keys, tokens, passwords
- Database connection strings
- Internal URLs
- Personal data (emails, phone numbers)
EOF

if [ -n "$SENSITIVE_PATTERNS" ]; then
  echo "" >> docs/vault/03_DO_NOT_TOUCH.md
  echo "### Detected Sensitive Patterns" >> docs/vault/03_DO_NOT_TOUCH.md
  echo "" >> docs/vault/03_DO_NOT_TOUCH.md
  echo "| Pattern | Source |" >> docs/vault/03_DO_NOT_TOUCH.md
  echo "|---------|--------|" >> docs/vault/03_DO_NOT_TOUCH.md
  echo "$SENSITIVE_PATTERNS" | while read -r pattern; do
    echo "| \`$pattern\` | .env.example |" >> docs/vault/03_DO_NOT_TOUCH.md
  done
fi
echo "  ✅ 03_DO_NOT_TOUCH.md"

# --- 04_ARCHITECTURE.md ---
cat > docs/vault/04_ARCHITECTURE.md << EOF
---
type: architecture
status: active
confidence: medium
last_updated: $TODAY
owner: agent
reviewed_by: unreviewed
---

# Architecture

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | $FRONTEND_STACK |
EOF

if [ -n "$BACKEND_STACK" ]; then
echo "| Backend | $BACKEND_STACK |" >> docs/vault/04_ARCHITECTURE.md
fi

cat >> docs/vault/04_ARCHITECTURE.md << EOF
| Source files | $SOURCE_COUNT |
| Assets | $ASSET_COUNT |

## Main Structure

> Customize with your project's directory structure.

EOF

# Add page list if detected
if [ -n "$PAGES" ] && [ "$PAGE_COUNT" -gt 0 ]; then
echo "### Pages ($PAGE_COUNT)" >> docs/vault/04_ARCHITECTURE.md
echo "" >> docs/vault/04_ARCHITECTURE.md
echo "\`\`\`" >> docs/vault/04_ARCHITECTURE.md
echo "$PAGES" >> docs/vault/04_ARCHITECTURE.md
echo "\`\`\`" >> docs/vault/04_ARCHITECTURE.md
echo "" >> docs/vault/04_ARCHITECTURE.md
fi

# Add backend deps if detected
if [ -n "$BACKEND_DEPS" ]; then
echo "### Backend Dependencies" >> docs/vault/04_ARCHITECTURE.md
echo "" >> docs/vault/04_ARCHITECTURE.md
echo "\`$BACKEND_DEPS\`" >> docs/vault/04_ARCHITECTURE.md
echo "" >> docs/vault/04_ARCHITECTURE.md
fi

# Add design files if detected
if [ "$DESIGN_COUNT" -gt 0 ]; then
echo "### Design Files ($DESIGN_COUNT)" >> docs/vault/04_ARCHITECTURE.md
echo "" >> docs/vault/04_ARCHITECTURE.md
echo "\`\`\`" >> docs/vault/04_ARCHITECTURE.md
ls design/*.html 2>/dev/null | head -10 >> docs/vault/04_ARCHITECTURE.md
echo "\`\`\`" >> docs/vault/04_ARCHITECTURE.md
echo "" >> docs/vault/04_ARCHITECTURE.md
fi

cat >> docs/vault/04_ARCHITECTURE.md << EOF

## Source Documentation

> Link to original planning docs, design docs, or discussions.
> This preserves the "why" behind decisions.
EOF

if [ -n "$DOC_FILES" ]; then
  echo "" >> docs/vault/04_ARCHITECTURE.md
  for doc in $DOC_FILES; do
    echo "- [[$doc]]" >> docs/vault/04_ARCHITECTURE.md
  done
fi
echo "  ✅ 04_ARCHITECTURE.md"

# --- 05_COMMANDS_AND_FILES.md ---
cat > docs/vault/05_COMMANDS_AND_FILES.md << EOF
---
type: commands-files
status: active
confidence: medium
last_updated: $TODAY
owner: agent
reviewed_by: unreviewed
---

# Commands and Files

## Commands

### Safe Local

| Command | Purpose | Risk |
|---------|---------|------|
EOF

if [ -n "$COMMANDS_SAFE" ]; then
  echo "$COMMANDS_SAFE" >> docs/vault/05_COMMANDS_AND_FILES.md
fi

cat >> docs/vault/05_COMMANDS_AND_FILES.md << EOF
| \`git status\` | Check changes | 🟢 Safe |
| \`git log --oneline -10\` | Recent commits | 🟢 Safe |

### Deploy

| Command | Purpose | Risk |
|---------|---------|------|
| {DEPLOY_CMD} | Deploy to production | 🔴 Critical |

## File Inventory

> List the most important files and their purposes.
EOF
echo "  ✅ 05_COMMANDS_AND_FILES.md"

# --- 06-10 minimal ---
for file_info in \
  "06_DEPLOYMENT.md|deployment|Deployment|> Describe build and deploy process here." \
  "07_TESTING_AND_VERIFICATION.md|testing|Testing|> Describe how to test this project." \
  "08_INCIDENTS_AND_FIXES.md|incidents|Incidents|No incidents yet." \
  "09_AGENT_PROMPTS.md|agent-prompts|Agent Prompts|## New Task Startup\n\nRead docs/vault/00_HOME.md before making changes.\nSummarize your plan before editing." \
  "10_REPORT_INDEX.md|report-index|Report Index|Full reports in assets/intake/reports/. Summaries here."
do
  IFS='|' read -r fname ftype ftitle fdesc <<< "$file_info"
  cat > "docs/vault/$fname" << EOF
---
type: $ftype
status: active
confidence: low
last_updated: $TODAY
owner: agent
reviewed_by: unreviewed
---

# $ftitle

$fdesc
EOF
  echo "  ✅ $fname"
done

# --- VAULT_SCHEMA.md ---
cat > docs/vault/VAULT_SCHEMA.md << EOF
---
type: schema
status: active
confidence: high
last_updated: $TODAY
owner: human
reviewed_by: human
---

# Vault Schema

## Project Identity

**Project:** $PROJECT_NAME
**Phase:** $PHASE
**Tech:** $TECH_STACK

## Vault Version

\`\`\`yaml
vault_version: 5.1.0
vault_created: $TODAY
\`\`\`

## Staleness Thresholds

\`\`\`yaml
staleness_threshold_days: 30
review_threshold_days: 14
audit_interval_days: 30
\`\`\`

## Link Discipline

- 00_HOME is the hub
- Reports only go to 10_REPORT_INDEX
- No circular links
EOF
echo "  ✅ VAULT_SCHEMA.md"

# --- VAULT_CHANGELOG.md ---
cat > docs/vault/VAULT_CHANGELOG.md << EOF
---
type: changelog
status: active
confidence: high
last_updated: $TODAY
owner: both
reviewed_by: unreviewed
---

# Vault Changelog

## [$TODAY] init | Vault created by init-vault.sh v2

- Phase: $PHASE
- Tech: $TECH_STACK
- Assets: $ASSET_COUNT files scanned
- Docs linked: $DOC_FILES
- Naming pattern: ${NAMING_PATTERN:-N/A}
EOF
echo "  ✅ VAULT_CHANGELOG.md"

# Templates
for tpl in DECISION_TEMPLATE INCIDENT_TEMPLATE DEPLOY_REPORT_TEMPLATE AGENT_TASK_TEMPLATE; do
  touch "docs/vault/templates/$tpl.md"
done
echo "  ✅ Templates"

# ============================================
# 6. VAULT SCORE
# ============================================
echo ""
echo "📊 Vault Score:"
TOTAL=13
HIGH_CONF=$(grep -l "confidence: high" docs/vault/*.md 2>/dev/null | wc -l)
HUMAN_REV=$(grep -l "reviewed_by: human" docs/vault/*.md 2>/dev/null | wc -l)

CONF=$((HIGH_CONF * 100 / TOTAL))
FRESH=100
COMP=$((TOTAL * 100 / TOTAL))
REV=$((HUMAN_REV * 100 / TOTAL))
SCORE=$((CONF * 35 / 100 + FRESH * 30 / 100 + COMP * 20 / 100 + REV * 15 / 100))

echo "  Confidence:  $CONF% ($HIGH_CONF/$TOTAL high)"
echo "  Freshness:   100%"
echo "  Completeness: 100%"
echo "  Review:      $REV% ($HUMAN_REV/$TOTAL human)"
echo ""
echo "  VAULT SCORE: $SCORE / 100"

if [ "$SCORE" -ge 90 ]; then echo "  Grade: 🟢 Excellent"
elif [ "$SCORE" -ge 70 ]; then echo "  Grade: 🟡 Good"
elif [ "$SCORE" -ge 50 ]; then echo "  Grade: 🟠 Needs work"
else echo "  Grade: 🔴 Critical"
fi

# ============================================
# 7. GIT COMMIT
# ============================================
echo ""
if git rev-parse --git-dir > /dev/null 2>&1; then
  git add docs/vault/ assets/intake/reports/ .gitignore 2>/dev/null
  git commit -m "docs: create project vault (phase: $PHASE, score: $SCORE)" 2>&1
  echo "✅ Committed to Git"
else
  echo "⚠️  No git repo found. Run 'git init' first."
fi

# ============================================
# 8. SUMMARY
# ============================================
echo ""
echo "=========================================="
echo "  ✅ Project Vault initialized!"
echo "=========================================="
echo ""
echo "  Files:     13 vault files + 4 templates"
echo "  Score:     $SCORE / 100"
echo "  Phase:     $PHASE"
echo "  Assets:    $ASSET_COUNT scanned"
echo "  Docs:     ${DOC_FILES:-none found}"
echo ""
echo "  Next steps:"
echo "  1. Open Obsidian → check Graph View"
echo "  2. Customize docs/vault/00_HOME.md"
echo "  3. Tell your AI: 'Read docs/vault/00_HOME.md first'"
echo ""

if [ "$IS_WSL" = true ] && [ "$ON_WINDOWS_VOLUME" = true ]; then
  echo "  Connect Obsidian (WSL detected):"
  echo "  bash templates/setup-obsidian-link.sh docs/vault \"$PROJECT_NAME\""
elif [ "$IS_WSL" = true ] && [ "$ON_WINDOWS_VOLUME" = false ]; then
  echo "  ⚠️  Move project to /mnt/c/ or /mnt/d/ before connecting Obsidian"
else
  echo "  Connect Obsidian:"
  echo "  bash templates/setup-obsidian-link.sh docs/vault \"$PROJECT_NAME\""
fi
echo ""
