---
name: project-vault
description: "Use when starting any new project, onboarding an existing codebase, or syncing project knowledge after changes. Creates and maintains a structured knowledge vault (docs/vault/) with quality signals, orphan detection, project phases, and lifecycle management. Human-visual + agent-executable project operating system."
version: 5.5.2
author: guoku
license: MIT
platforms: [linux, macos, windows, wsl]
metadata:
  hermes:
    tags: [project-init, knowledge-base, documentation, onboarding, vault, agent-safety, lifecycle, schema, quality, obsidian, phases]
    related_skills: [writing-plans, requesting-code-review, codebase-inspection, plan, llm-wiki, systematic-debugging, obsidian]
# References: design-rationale.md, audit-methodology.md, obsidian-integration.md, walkthrough-two-char-diary.md, walkthrough-worldcup.md, wsl-github-push.md, wsl-github-push-proxy.md, source-documentation-pattern.md, obsidian-aliases-pattern.md, iterative-development-pattern.md, readme-style-guide.md, karpathy-coding-principles.md, vault-sync-discipline.md, espn-sports-api.md, free-sports-apis.md, content-feed-pattern.md, data-integrity-audit.md, claude-code-integration.md, github-actions-debugging.md
---

# Project Vault — Project Operating System

## Overview

Project Vault is a **project operating system** — human-visual + agent-executable. It creates a structured knowledge base under `docs/vault/` that:

- **Onboards** — any agent can understand the project in 5 minutes
- **Protects** — documents what NOT to touch, preventing production incidents
- **Evolves** — tracks project changes with quality signals and append-only logs
- **Audits** — detects stale knowledge, orphan references, and quality degradation
- **Scales** — adapts to project phase (idea → prototype → MVP → maintenance → sunset)
- **Secures** — prevents secret leakage into vault files

## When to Use

| Trigger | Action |
|---------|--------|
| New project kickoff | **Init** — create the vault from scratch |
| Empty project (idea only) | **Init --greenfield** — minimal vault, grow as project grows |
| Onboarding existing codebase | **Init** — inspect and document everything |
| After significant code changes | **Sync** — update vault to match current state |
| Before handoff to another agent | **Audit** — verify vault is current |
| Monthly or before major release | **Audit** — catch stale knowledge |
| After incident/deploy | **Sync** — log incident, update baseline |
| Vault structure needs update | **Upgrade** — migrate to new vault version |
| Project phase changes | **Upgrade** — add/remove vault files for new phase |

**Don't use for:**
- Quick one-off scripts with no maintenance needs
- Projects you'll never revisit

## The 6 Lifecycle Commands

| Command | When | What It Does |
|---------|------|-------------|
| `vault init` | New project / onboarding | Create vault from scratch |
| `vault init --greenfield` | Empty project (idea only) | Create minimal vault, grow later |
| `vault sync` | After significant changes | Update affected vault files |
| `vault audit` | Monthly / before handoff | Health check, detect stale knowledge |
| `vault upgrade` | Skill version bump / phase change | Migrate vault to new structure |
| `vault score` | Anytime | Calculate vault health score |

**Mandatory first step for every agent task:**
```
Read docs/vault/00_HOME.md before making changes.
```

## Project Phases

Projects have lifecycles. The vault adapts to each phase:

| Phase | Vault Files Required | Files Optional | Description |
|-------|---------------------|----------------|-------------|
| **idea** | 00_HOME, 04_ARCHITECTURE, VAULT_SCHEMA | All others | Just the vision |
| **prototype** | + 01_BASELINE, 05_COMMANDS | 06_DEPLOY, 07_TESTING, 08_INCIDENTS | Working code, no deploys |
| **mvp** | + 03_DO_NOT_TOUCH, 06_DEPLOY, 07_TESTING | 08_INCIDENTS | First users |
| **growth** | All 13 files | None | Full vault |
| **maintenance** | All 13 files | None | Focus on 02_DECISIONS + 08_INCIDENTS |
| **sunset** | 00_HOME, 03_DO_NOT_TOUCH | Rest archived | Read-only project |

Set the phase in `VAULT_SCHEMA.md`:
```yaml
project_phase: growth  # idea | prototype | mvp | growth | maintenance | sunset
```

During `vault init`, the phase determines which files are created. During `vault upgrade`, changing the phase adds/removes files.

## Vault Structure

```
docs/vault/
├── 00_HOME.md                          # Agent entry page + project overview + VAULT STARTUP SYNC
├── 01_CURRENT_BASELINE.md              # Source of truth: branch, commit, status
├── 02_DECISION_LOG.md                  # Why we made key choices
├── 03_DO_NOT_TOUCH.md                  # 🚫 Danger zones + security rules
├── 04_ARCHITECTURE.md                  # Tech stack, data flow, modules
├── 05_COMMANDS_AND_FILES.md            # Command & file inventory
├── 06_DEPLOYMENT.md                    # Build, deploy, rollback
├── 07_TESTING_AND_VERIFICATION.md      # Tests, lint, QA checklist
├── 08_INCIDENTS_AND_FIXES.md           # What broke and how we fixed it
├── 09_AGENT_PROMPTS.md                 # Reusable prompts for common tasks
├── 10_REPORT_INDEX.md                  # Summary index only (full reports in assets/)
├── VAULT_SCHEMA.md                     # Vault rules, phase, thresholds, write protocol
├── VAULT_CHANGELOG.md                  # Append-only vault operation log
└── templates/
    ├── DECISION_TEMPLATE.md
    ├── INCIDENT_TEMPLATE.md
    ├── DEPLOY_REPORT_TEMPLATE.md
    └── AGENT_TASK_TEMPLATE.md

assets/intake/reports/                  # Full reports live here (NOT in vault)
├── 2026-06-01_setup-report.md
├── 2026-06-15_deploy-report.md
└── 2026-07-01_audit-report.md
```

**Key rule:** Full reports go in `assets/intake/reports/`. The vault only contains summaries in `10_REPORT_INDEX.md`. This keeps Obsidian Graph View clean.

## Standardized Metadata

Every vault file MUST have this frontmatter:

```yaml
---
type: home | baseline | decision-log | danger-zones | architecture | commands-files | deployment | testing | incidents | agent-prompts | report-index | schema | changelog
status: active | stale | archived
confidence: high | medium | low
last_updated: YYYY-MM-DD
owner: agent | human | both
reviewed_by: agent | human | unreviewed
---
```

| Field | Purpose | Dataview Query |
|-------|---------|----------------|
| `type` | What kind of vault file | `WHERE type = "incidents"` |
| `status` | Is this file current? | `WHERE status = "stale"` |
| `confidence` | How trustworthy? | `WHERE confidence = "low"` |
| `last_updated` | When last changed? | `SORT last_updated DESC` |
| `owner` | Who maintains this? | `WHERE owner = "human"` |
| `reviewed_by` | Who confirmed accuracy? | `WHERE reviewed_by = "unreviewed"` |

### Quality Rules

| Rule | Detail |
|------|--------|
| `03_DO_NOT_TOUCH` entries | MUST be `confidence: high` + `reviewed_by: human` |
| "Must not regress" items | MUST be `confidence: high` |
| Agent-written content | Default `reviewed_by: agent` until human confirms |
| Human edits in Obsidian | Set `reviewed_by: human` after confirming |

### Dataview Queries

```dataview
TABLE type, confidence, last_updated, reviewed_by
FROM "docs/vault"
WHERE type
SORT last_updated DESC
```

```dataview
LIST
FROM "docs/vault"
WHERE reviewed_by = "unreviewed" AND confidence != "low"
```

```dataview
LIST
FROM "docs/vault"
WHERE status = "stale"
```

## 00_HOME.md — Universal Agent Entry Page

Every project's vault MUST have `00_HOME.md` as the central hub. Non-negotiable.

**Critical: Add `aliases` to distinguish projects in Obsidian search and linking.**

```yaml
---
type: home
aliases: ["项目中文名", "Project English Name", "project-slug"]
---
```

Without aliases, search and backlinks can't distinguish between projects.
For Graph View display, use **color groups** (see Obsidian Integration section below).

```markdown
## 🔴 Agent Entry Page

> **Every new Agent MUST read this page first.**

**Mandatory reading order:**
1. [[00_HOME]] — You are here
2. [[01_CURRENT_BASELINE]] — Source of truth
3. [[03_DO_NOT_TOUCH]] — Danger zones + security rules
4. [[05_COMMANDS_AND_FILES]] — What you can run
5. [[VAULT_SCHEMA]] — Vault rules + write protocol
6. Task-specific vault note

**After completing any task, you MUST:**
- Update [[01_CURRENT_BASELINE]] if branch/commit/status changed
- Append to [[10_REPORT_INDEX]] if a report was generated (full report → assets/intake/reports/)
- Append to [[VAULT_CHANGELOG]]
```

## Multi-Agent Write Protocol

When multiple agents work on the same project, vault writes can conflict. Rules:

### File Ownership

| File | Primary Writer | Backup Writer |
|------|---------------|---------------|
| `00_HOME.md` | Human | Agent |
| `01_CURRENT_BASELINE.md` | Last agent to commit | — |
| `02_DECISION_LOG.md` | Human (decisions) | Agent (recording) |
| `03_DO_NOT_TOUCH.md` | Human | Agent (suggestions only) |
| `04_ARCHITECTURE.md` | Agent | Human |
| `05_COMMANDS_AND_FILES.md` | Agent | — |
| `06_DEPLOYMENT.md` | Agent | Human |
| `07_TESTING_AND_VERIFICATION.md` | Agent | — |
| `08_INCIDENTS_AND_FIXES.md` | Agent | — |
| `VAULT_SCHEMA.md` | Human | — |
| `VAULT_CHANGELOG.md` | Any agent (append-only) | — |

### Conflict Resolution

1. **Append-only files** (VAULT_CHANGELOG, 08_INCIDENTS, 02_DECISIONS): No conflicts — always append at the end
2. **State files** (01_BASELINE, 05_COMMANDS): Last writer wins — agent must read current state before writing
3. **Rule files** (03_DO_NOT_TOUCH, VAULT_SCHEMA): Human has veto — agent can suggest but not override
4. **If conflict detected** (git merge conflict in vault): Agent MUST stop and ask human to resolve

### Write Lock Convention

Before modifying a state file, agent should:
1. Read the file
2. Check `last_updated` timestamp
3. If updated within last 5 minutes by another agent → wait and retry
4. Make changes
5. Update `last_updated` to now
6. Commit immediately

## Report Separation

Full reports do NOT go in `docs/vault/`. They go in `assets/intake/reports/`.

```
assets/intake/reports/
├── 2026-06-01_setup-report.md
├── 2026-06-15_deploy-report.md
├── 2026-07-01_audit-report.md
└── 2026-07-15_incident-report.md
```

`docs/vault/10_REPORT_INDEX.md` contains only summaries with relative links to full reports.

**During `vault init`:** `mkdir -p assets/intake/reports` is created automatically.

## Security Rules

The vault MUST NOT contain:
- API keys, tokens, passwords, or secrets
- Internal URLs that are not public
- Database connection strings
- Private IP addresses or ports
- Personal data (emails, phone numbers) unless explicitly approved

These are documented in `03_DO_NOT_TOUCH.md` under a "Security" section.

**During `vault init`:** Agent scans `.env.example` and `.gitignore` to identify sensitive patterns, then adds them to `03_DO_NOT_TOUCH.md` automatically.

## 🔴 Continuous Sync Rule (边做边更新)

**The vault must be updated DURING work, NOT batched at the end.**

Agents naturally focus on code and forget the vault. By the time they remember, context has been lost — commits, decisions, and incidents from earlier in the session are summarized inaccurately or omitted entirely. This defeats the vault's purpose.

### Per-Action Sync Table

| Agent Action | Vault Update Required | When |
|-------------|----------------------|------|
| Commit code | Update `01_CURRENT_BASELINE.md` (HEAD, status) | Immediately after commit |
| Fix a bug | Append `08_INCIDENTS_AND_FIXES.md` | Immediately after fix |
| Make architecture decision | Append `02_DECISION_LOG.md` | Before implementing |
| Add/delete/rename files | Update `05_COMMANDS_AND_FILES.md` | Same commit |
| Change deploy process | Update `06_DEPLOYMENT.md` | Same commit |
| Add/remove dependencies | Update `04_ARCHITECTURE.md` | Same commit |
| New dangerous area discovered | Update `03_DO_NOT_TOUCH.md` | Immediately |

### Anti-Patterns (Forbidden)

- ❌ **End-of-session batch update** — "I'll update the vault when I'm done." Context is lost by then.
- ❌ **User reminds you** — if the user has to say "update the vault", you already failed.
- ❌ **Code-only commits** — a commit that changes code but not the vault is incomplete.

### Correct Pattern

```
1. Read vault (startup)
2. Make code change
3. Commit code
4. IMMEDIATELY update affected vault file(s)
5. Repeat 2-4 for each change
6. Final commit: "docs: vault sync" with any remaining updates + VAULT_CHANGELOG
```

The vault commit can be a single "docs:" commit at the end that bundles all vault changes made during the session — but the FILE CONTENT must be written incrementally as work progresses, not reconstructed from memory at the end.

## Agent Task-End Rule

**Every Agent task MUST end with a FINAL vault check:**

1. Read through ALL vault files — did every code change get reflected?
2. Update `01_CURRENT_BASELINE.md` with final HEAD commit and status
3. Append to `VAULT_CHANGELOG.md` with session summary
4. If any vault file was missed during live sync, update it now
5. Commit vault changes with prefix `docs:`

This is the SAFETY NET. Live sync (above) should catch most updates, but the task-end rule catches anything missed.

## How Init Works

### Mode 1: Standard Init (existing codebase)

**Option A: Automated script (recommended)**

```bash
bash templates/init-vault.sh /path/to/project "Project Name" mvp
```

The script auto-detects:
- **Phase**: idea/prototype/mvp/growth based on project files
- **Tech stack**: multi-stack aware (e.g. "WeChat Mini Program + FastAPI")
- **Full-stack**: detects `backend/` directory with its own deps
- **Assets**: scans `assets/`, `miniprogram/images/`, `design/`, `public/images/`, `static/images/`
- **Design files**: scans `design/*.html` and counts them
- **Pages**: extracts from `miniprogram/app.json` or `app.json`
- **Backend deps**: reads `backend/requirements.txt` or `requirements.txt`
- **Recent commits**: fills `git log --oneline -5` into 01_BASELINE
- **Naming patterns**: detects `wasr_bs_sXX_XXX` style patterns
- **Sensitive patterns**: scans `.env.example` for API key names
- **WSL path check**: warns if project is on WSL filesystem (Obsidian can't access)

Then runs vault score and git commit automatically.

**Option B: Manual (for AI agent)**

Paste `templates/INIT_PROMPT.md` to your AI agent.

**Phase 1: Inspect (read-only)**
```bash
git status
git log --oneline -10
```

Inspect files if they exist (skip if missing):
```
README.md  CLAUDE.md  AGENTS.md  package.json  pnpm-lock.yaml
yarn.lock  requirements.txt  pyproject.toml  Cargo.toml  go.mod
Dockerfile  docker-compose.yml  .env.example  .gitignore
docs/  scripts/  src/  app/  lib/
```

**Phase 2: Create structure**
```bash
mkdir -p docs/vault/templates
mkdir -p assets/intake/reports
```

Create vault files based on `project_phase` (see Project Phases table above).

**Phase 3: Fill with quality signals**
- Add standardized metadata frontmatter to every file
- Set `confidence` based on verification level
- Set `reviewed_by: agent` (human confirms later)
- Set `last_updated` to today
- Scan `.env.example` + `.gitignore` → add security rules to `03_DO_NOT_TOUCH.md`
- If unknown: write "Unknown — not verified in this pass", set `confidence: low`

**Phase 4: Record in log**
```markdown
## [YYYY-MM-DD] init | Vault created
- Phase: {PROJECT_PHASE}
- Files created: {COUNT}
- Commands inventoried: {COUNT}
- Dangerous commands found: {COUNT}
- Security rules added: {COUNT}
- Confidence: medium (initial pass)
```

**Phase 5: Validate & commit**
```bash
git add docs/vault/ assets/intake/reports/
git commit -m "docs: create agent vault"
```

### Mode 2: Greenfield Init (empty project)

```markdown
Run project-vault with action: init --greenfield
```

For projects that are just an idea — no code yet.

```bash
mkdir -p docs/vault/templates
mkdir -p assets/intake/reports
```

Create only phase-appropriate files (typically `idea` phase: 00_HOME, 04_ARCHITECTURE, VAULT_SCHEMA, VAULT_CHANGELOG).

All sections use placeholder text with `confidence: low` and `reviewed_by: unreviewed`.

As the project grows, run `vault upgrade` to add files for the new phase.

## How Sync Works

### Change → File Mapping

| What Changed | Update These Files | Urgency |
|-------------|-------------------|---------|
| New branch/tag/commit | `01_CURRENT_BASELINE.md` | 🟡 Medium |
| Architecture change | `04_ARCHITECTURE.md` | 🔴 High |
| New commands/scripts | `05_COMMANDS_AND_FILES.md` | 🟡 Medium |
| New dependencies | `04_ARCHITECTURE.md`, `05_COMMANDS_AND_FILES.md` | 🟡 Medium |
| Deploy process change | `06_DEPLOYMENT.md` | 🔴 High |
| New test suite | `07_TESTING_AND_VERIFICATION.md` | 🟡 Medium |
| Incident occurred | `08_INCIDENTS_AND_FIXES.md` | 🔴 High |
| Decision made | `02_DECISION_LOG.md` | 🟡 Medium |
| New dangerous area | `03_DO_NOT_TOUCH.md` | 🔴 High |
| Any significant change | `01_CURRENT_BASELINE.md`, `VAULT_CHANGELOG.md` | 🟡 Medium |
| Phase change | Run `vault upgrade` | 🔴 High |

### Sync Procedure

```bash
# 1. Check what changed
git log --oneline -20
git diff --stat HEAD~10

# 2. Read current vault

# 3. Update affected files using mapping above

# 4. Update metadata: last_updated = today, confidence = re-verified

# 5. Append to VAULT_CHANGELOG.md

# 6. Commit
git add docs/vault/
git commit -m "docs: sync vault — {WHAT_CHANGED}"
```

## How Audit Works

### 10-Point Checklist

| # | Check | How | Severity |
|---|-------|-----|----------|
| 1 | **Existence** | All phase-required vault files exist? | 🔴 Critical |
| 2 | **Baseline freshness** | `01_CURRENT_BASELINE.md` HEAD matches `git log -1`? | 🔴 Critical |
| 3 | **Orphan wikilinks** | Any `[[wikilinks]]` pointing to missing files? | 🟡 Warning |
| 4 | **Orphan content** | Any vault file not referenced by any other? | 🟡 Warning |
| 5 | **Confidence audit** | Any `confidence: low` that should be `high`? | 🟡 Warning |
| 6 | **Review audit** | Any `reviewed_by: unreviewed` older than threshold? | 🟠 High |
| 7 | **Staleness** | Any files with `last_updated` older than threshold? | 🟠 High |
| 8 | **Command sync** | `05_COMMANDS_AND_FILES.md` matches `package.json`? | 🟠 High |
| 9 | **DO_NOT_TOUCH validity** | Referenced files still exist? Security rules current? | 🔴 Critical |
| 10 | **Cross-reference** | Every vault file has ≥1 inbound `[[wikilink]]`? | 🟡 Warning |

### Staleness Thresholds

Defined in `VAULT_SCHEMA.md`, NOT hardcoded:

```yaml
staleness_threshold_days: 30    # active development
review_threshold_days: 14       # how long before unreviewed becomes stale
```

### Audit Report

Write full report to `assets/intake/reports/YYYY-MM-DD_audit-report.md`.
Add summary to `10_REPORT_INDEX.md`.

## How Upgrade Works

```markdown
Run project-vault with action: upgrade
```

Triggers when:
- Skill version changes (v4.0 → v4.1)
- Project phase changes (prototype → mvp)
- Vault structure needs migration

### Upgrade Procedure

1. Read current `VAULT_SCHEMA.md` — note `vault_version` and `project_phase`
2. Compare with new skill version
3. Add missing files (new phase requires more files)
4. Remove/archive files (phase regression, e.g., mvp → sunset)
5. Update metadata format if schema changed
6. Bump `vault_version` in `VAULT_SCHEMA.md`
7. Append to `VAULT_CHANGELOG.md`
8. Commit

### Version Tracking

In `VAULT_SCHEMA.md`:
```yaml
vault_version: 4.1.0    # matches skill version
vault_created: 2026-06-01
last_upgraded: 2026-07-15
```

## How Score Works

```markdown
Run project-vault with action: score
```

Calculates vault health:

```
vault_score = confidence_score * 0.35
            + freshness_score * 0.30
            + completeness_score * 0.20
            + review_score * 0.15

confidence_score  = high_confidence_files / total_files * 100
freshness_score   = files_within_threshold / total_files * 100
completeness_score = existing_files / phase_required_files * 100
review_score      = human_reviewed_files / total_files * 100
```

| Score | Grade | Action |
|-------|-------|--------|
| 90-100 | 🟢 Excellent | Maintain |
| 70-89 | 🟡 Good | Review low-confidence items |
| 50-69 | 🟠 Needs work | Run vault sync |
| 0-49 | 🔴 Critical | Run vault audit, fix issues |

## Vault Split & Merge

### Split (monorepo)

When a project splits into multiple repos:

```bash
# For each new repo:
# 1. Copy vault to new repo
cp -r docs/vault/ /path/to/new-repo/docs/vault/

# 2. Remove files that don't apply to the sub-project
# 3. Update 00_HOME.md with new project identity
# 4. Update VAULT_SCHEMA.md with new phase
# 5. Commit in new repo
```

### Merge (consolidation)

When projects merge:

```bash
# 1. Create new vault in merged repo
# 2. Merge decisions from both into 02_DECISION_LOG.md
# 3. Merge danger zones into 03_DO_NOT_TOUCH.md
# 4. Combine command inventories into 05_COMMANDS_AND_FILES.md
# 5. Update 00_HOME.md with merged project identity
# 6. Archive old vaults
```

## Git Hook Integration

```bash
cp templates/git-hook-post-commit .git/hooks/post-commit
chmod +x .git/hooks/post-commit
```

## CI Integration

```bash
cp templates/ci-vault-check.yml .github/workflows/vault-check.yml
```

## Obsidian Integration — Pitfalls from Real-World Use

### WSL Symlink Does NOT Work with Windows Obsidian

`ln -sf` from WSL creates Linux symlinks. Windows Obsidian sees `EACCES: permission denied`.
**Fix:** Use Windows junction via PowerShell — no admin required:

```powershell
powershell.exe -Command "cmd /c mklink /J 'C:\Users\YOU\Documents\Obsidian Vault\Projects\项目名' 'C:\Users\YOU\Desktop\project\docs\vault'"
```

The cross-platform script `templates/setup-obsidian-link.sh` handles this automatically.

### Graph View Node Disambiguation (aliases)

When multiple projects connect to one Obsidian vault, all `00_HOME.md` nodes look identical in Graph View. **Fix:** Add `aliases` to frontmatter:

```yaml
aliases: ["二字日记", "二字日记 Home", "two-char-diary"]
```

Graph View then shows the alias instead of the filename. The vault template already includes this.

### Obsidian Default Files

New vaults auto-create `未命名.base` and `欢迎.md`. Safe to delete — not part of project vault.

### Multi-Project Cross-Index

When multiple projects share one Obsidian vault, create `Projects/INDEX.md` with a table linking to each project's `[[alias]]`. Template: `templates/PROJECTS_INDEX.md`.

---

Agent Vault uses Obsidian-native `[[wikilinks]]` syntax.

### Approach A: Open Project as Obsidian Vault

1. Open Obsidian → "Open folder as vault" → select project root
2. All `[[wikilinks]]` work natively

### Approach B: Multi-Project via Link (Recommended)

All projects in one unified Obsidian vault. **Project files are real; Obsidian only holds references.**

**Cross-platform setup script (auto-detects OS):**

```bash
# Copy the script to your project (or run from skill templates)
bash templates/setup-obsidian-link.sh /path/to/project/docs/vault "项目名"
```

The script handles:
| Platform | Method | Admin Required |
|----------|--------|---------------|
| macOS | `ln -s` | No |
| Linux | `ln -s` | No |
| Windows (no WSL) | `mklink /J` | No (junction) |
| WSL + Windows | `mklink /J` via PowerShell | No (junction) |

**Manual setup if script doesn't work:**

```bash
# macOS / Linux
ln -s ~/project/docs/vault "$OBSIDIAN_VAULT/Projects/项目名"

# WSL + Windows (⚠️ do NOT use ln -sf — Windows can't read WSL symlinks)
powershell.exe -Command "cmd /c mklink /J 'C:\Users\YOU\Documents\Obsidian Vault\Projects\项目名' 'C:\Users\YOU\Desktop\project\docs\vault'"

# Windows PowerShell (no WSL)
New-Item -ItemType Junction -Path "C:\Users\YOU\Documents\Obsidian Vault\Projects\项目名" -Target "C:\Users\YOU\Desktop\project\docs\vault"
```

Convention: Each project's `docs/vault/` is the real file (committed to Git). Obsidian only holds junction/symlink references.

**Pros:** Unified graph view, cross-project linking, one search index, Git-safe
**Best for:** Multi-project overview

### Graph View Color Groups (Critical for Multi-Project)

All projects use the same filenames (`00_HOME.md`, `01_CURRENT_BASELINE.md`...). Without color coding, Graph View shows identical-looking nodes for every project.

**Fix: Obsidian Graph Color Groups** — assign a unique color per project:

```json
// .obsidian/graph.json — add to colorGroups array
{
  "colorGroups": [
    {"query": "path:Projects/二字日记", "color": {"a": 1, "rgb": 12101770}},
    {"query": "path:Projects/世界杯", "color": {"a": 1, "rgb": 3900150}},
    {"query": "path:Projects/晚安小书房", "color": {"a": 1, "rgb": 10190276}}
  ]
}
```

Color reference (decimal RGB):
| Color | Hex | Decimal | Suggested for |
|-------|-----|---------|--------------|
| Copper/Gold | #B8A88A | 12101770 | Warm projects |
| Blue | #3B82F6 | 3900150 | Tech projects |
| Purple | #9B7DC4 | 10190276 | Creative projects |
| Green | #10B981 | 1088512 | Growth projects |
| Red | #EF4444 | 15680068 | Alert/urgent |

After configuring, each project's nodes appear in a different color. You can instantly tell which `00_HOME` belongs to which project.

### Pitfall: Obsidian Default Files

New vaults in Obsidian auto-create `未命名.base` and `欢迎.md`. These are Obsidian defaults, not vault content. Safe to delete. The `setup-obsidian-link.sh` script deletes them automatically.

### Obsidian Config

```json
// .obsidian/app.json
{
  "showUnsupportedFiles": true,
  "newLinkFormat": "shortest",
  "useMarkdownLinks": false,
  "alwaysUpdateLinks": true
}
```

### Agent + Obsidian Loop

```
Agent writes vault → Git commit → Obsidian auto-refreshes
    → Human reviews in Obsidian (graph, backlinks, Dataview)
    → Human confirms (reviewed_by: human)
    → Agent reads updated vault on next task
```

## Source Documentation

Every project has planning docs, design discussions, or decision records that aren't in the vault. **Link them in `04_ARCHITECTURE.md` under "Source Documentation".**

Examples:
- `[[项目构想.md]]` — original planning doc
- `[[PRD]]` — product requirements
- `[[design-spec]]` — design specifications
- Chat logs, meeting notes, email threads

**Why:** Six months from now, "why did we choose X?" should be one click away.

## Multi-Project Obsidian Setup

When you have multiple projects connected to one Obsidian vault, add a `Projects/INDEX.md`:

```markdown
# Projects Index

| Project | Phase | Score | Entry |
|---------|-------|-------|-------|
| [[二字日记]] | mvp | 81/100 | [[二字日记]] |
| [[世界杯]] | prototype | 75/100 | [[世界杯]] |
```

This gives you a bird's-eye view of all projects. The `[[aliases]]` link to each project's `00_HOME`.

## Graph View Link Discipline

To prevent Obsidian Graph View from becoming a spider web, follow these rules:

### Star Structure (00_HOME as Hub)

```
00_HOME ──→ 01_CURRENT_BASELINE
    ├──→ 03_DO_NOT_TOUCH
    ├──→ 05_COMMANDS_AND_FILES
    ├──→ 09_AGENT_PROMPTS (second entry point)
    ├──→ 10_REPORT_INDEX (report gateway)
    └──→ task-specific files (02, 04, 06, 07, 08)
```

### Link Rules

| Rule | Detail |
|------|--------|
| **Core docs can interlink** | 00↔01↔03↔05↔09 are allowed |
| **Reports only go to INDEX** | Reports link ONLY to 10_REPORT_INDEX, never to core docs |
| **Templates don't link core** | Templates are standalone, no wikilinks to vault files |
| **09 is second entry** | Only 00_HOME links to 09, 09 doesn't link back to 00 |
| **One-way preferred** | 00_HOME → other files. Other files don't backlink to 00 |
| **No circular chains** | A→B→C→A is forbidden. Keep it tree-shaped |

### Why This Matters

Without discipline, Graph View becomes unreadable after 6 months. The star structure keeps `00_HOME` as the clear center, with clean spokes to each file.

## Agent Prompt Templates

### New Task Startup (ALWAYS first)

```
Read docs/vault/00_HOME.md, docs/vault/01_CURRENT_BASELINE.md,
docs/vault/03_DO_NOT_TOUCH.md, and docs/vault/05_COMMANDS_AND_FILES.md
before making changes. Then read VAULT_SCHEMA.md for project rules
and write protocol. Do not change unrelated systems.
Do not deploy unless explicitly asked. Summarize your plan before editing.
```

### Bugfix

```
Read vault. Identify the bug. Propose a fix with affected files.
Do not refactor. Run tests after fix.
【边做边更新】Immediately after fix:
  - Append to 08_INCIDENTS_AND_FIXES.md
  - Update 01_CURRENT_BASELINE.md
Write incident report to assets/intake/reports/YYYY-MM-DD_incident-{slug}.md
Add summary to 10_REPORT_INDEX.md. Set reviewed_by: agent.
```

### Feature

```
Read vault. Identify affected modules. Propose implementation plan.
Do not touch files in 03_DO_NOT_TOUCH.md without approval.
【边做边更新】After each commit:
  - Update 01_CURRENT_BASELINE.md
  - Update 05_COMMANDS_AND_FILES.md if files added/removed
  - Update 04_ARCHITECTURE.md if structure changed
  - Append 02_DECISION_LOG.md if decision made
Run tests. Commit vault changes with prefix "docs:".
```

### Task Completion (ALWAYS last)

```
Task complete. Final vault check:
1. Verify all vault files were updated DURING work (not batching!)
2. Append entry to VAULT_CHANGELOG.md with session summary
3. Commit vault changes with prefix "docs:"
4. git push
```

### Sync

```
Read vault. Check git log for recent changes.
Update affected files using change→file mapping.
Update metadata (last_updated, confidence). Append to VAULT_CHANGELOG.md.
Commit with prefix "docs:".
```

### Audit

```
Read all vault files. Run 10-point checklist from VAULT_SCHEMA.md.
Check orphans, confidence, staleness, cross-references, security rules.
Write full report to assets/intake/reports/YYYY-MM-DD_audit-report.md.
Add summary to 10_REPORT_INDEX.md.
```

## Design Principles (User Preferences)

- **Simple over professional.** README should be ~50 lines. One-line descriptions beat paragraphs. This is a "小帮手" (small helper), not enterprise software. Don't make it look intimidating.
- **Screenshots over text.** A Graph View screenshot explains more than 10 paragraphs of Obsidian docs. Include one in the README.
- **Separate language READMEs.** `README.md` (English) + `README.zh-CN.md` (Chinese), linked at top. GitHub auto-detects `zh-CN` and shows language switcher. Do NOT mix both in one file.
- **Image width: 500px** in README — `<img src="..." width="500">` not full-width.
- **"太丑就重画，不修补"** — if the output isn't good, redo it entirely rather than patch.
- **"不要造轮子"** — check existing skills/tools before building new ones.
9. **Don't forget to push screenshots.** Always verify `git add assets/` before push. User will call you out ("你简直是个小迷糊").
10. **Screenshots must be relevant.** Never add screenshots from unrelated projects to a README. If one language README has a screenshot, the other should have the SAME one — don't add different/irrelevant images. User explicitly corrected this.

## Agent Memory Discipline

When an agent works on multiple projects, memory gets polluted fast. The user's explicit preference: **only two things truly matter in memory**:

1. **⚠️ Work discipline** — "Before starting any project with a vault, read `00_HOME.md` + `01_CURRENT_BASELINE.md` first. Update vault DURING work, not after."
2. **Project locations** — A compact map of every project's path + vault status.

Everything else (deployment details, API quirks, hardware specs) belongs in the vault files, not in agent memory. If the agent reads `00_HOME.md` at the start of every session, it gets the full context without memory bloat.

**Memory template (one entry, all projects):**
```
⚠️ 开工纪律：有vault→先读 00_HOME.md + 01_BASELINE.md。边做边更新vault。
§
项目路径：项目A=path(status) | 项目B=path(status) | ...
```

This single entry replaces dozens of scattered per-project memory entries.

## Vault Sync via Git Log Diffing

When vault is stale (agent forgot to update), the fastest recovery:

```bash
# 1. Find vault's last_updated date
grep 'last_updated' docs/vault/01_CURRENT_BASELINE.md

# 2. Count missing commits
git log --oneline --since="<last_updated>" | wc -l

# 3. Categorize commits (exclude chore/docs noise)
git log --oneline --since="<last_updated>" | grep -v "chore: update" | grep -v "docs:"

# 4. Map commits to vault files
#    feat: → 04_ARCHITECTURE + 05_COMMANDS + 08_INCIDENTS
#    fix:  → 08_INCIDENTS
#    refactor: → 04_ARCHITECTURE
#    remove: → 04_ARCHITECTURE + 05_COMMANDS
#    style: → (usually skip unless major visual change)

# 5. Update each file, then commit
git add docs/vault/ && git commit -m "docs: vault sync — N commits补更新"
```

## TencentDB-Assisted Vault Maintenance

When TencentDB Agent Memory is installed, use it as a vault auditor:

1. **conversation_search** with project keywords → find recent discussions
2. Compare timestamps against vault `last_updated` fields
3. Extract decisions/incidents from conversations that weren't written to vault
4. Auto-update vault files with the extracted information

**Cron job pattern:** Run nightly, check each project's git log since vault's last_updated, auto-sync if stale. See `references/tencentdb-vault-sync.md`.

## Vault Sync via Git Log Diffing

## Common Pitfalls

1. **Agent skips vault read.** Enforce startup checklist from `00_HOME.md`.
2. **Vault becomes stale.** The #1 failure mode: agent does all work, never updates vault, user has to remind. **Fix: "边做边更新vault" — update vault files DURING work, not after.** Each code commit should have a corresponding vault update. See `09_AGENT_PROMPTS.md` CORE RULE.
   - **Real-world example:** worldcup2026 vault was 3 days behind — 37 commits unstaged. Manual sync required updating 9 files with categorized commit analysis.
   - **Cron auto-sync** is the sustainable fix — `staleness_threshold_days` in VAULT_SCHEMA.md determines when to trigger.
3. **03_DO_NOT_TOUCH is too vague.** Name exact files, exact commands, exact conditions.
4. **Inventing facts.** Write "Unknown — not verified in this pass." Set `confidence: low`.
5. **No metadata.** Every file MUST have full frontmatter.
6. **Orphan references.** After deleting a project file, check if vault references it.
7. **Reports in vault.** Full reports go in `assets/intake/reports/`, not `docs/vault/`.
8. **Secrets in vault.** Never put API keys, passwords, or internal URLs in vault files.
9. **Hardcoded thresholds.** Staleness/review thresholds belong in `VAULT_SCHEMA.md`.
10. **No phase awareness.** Don't create 08_INCIDENTS for an idea-phase project.
11. **Multi-agent conflicts.** Check write protocol in `VAULT_SCHEMA.md` before editing state files.
12. **WSL symlink doesn't work with Windows Obsidian.** `ln -sf` creates Linux symlinks that Windows can't read. Use `powershell.exe -Command "cmd /c mklink /J"` for directory junctions instead.
13. **Obsidian default files confuse users.** `未命名.base` and `欢迎.md` are auto-created by Obsidian, not by agent-vault. Safe to delete.
6. **Orphan references.** After deleting a project file, check if vault references it.
7. **Reports in vault.** Full reports go in `assets/intake/reports/`, not `docs/vault/`.
8. **Secrets in vault.** Never put API keys, passwords, or internal URLs in vault files.
9. **Hardcoded thresholds.** Staleness/review thresholds belong in `VAULT_SCHEMA.md`.
10. **No phase awareness.** Don't create 08_INCIDENTS for an idea-phase project.
11. **Multi-agent conflicts.** Check write protocol in `VAULT_SCHEMA.md` before editing state files.
12. **Never upgrading.** Run `vault upgrade` when skill version changes or phase changes.
13. **WSL symlink doesn't work with Windows Obsidian.** `ln -sf` creates Linux symlinks that Windows can't read. Use `powershell.exe -Command "cmd /c mklink /J"` for directory junctions instead.
14. **Obsidian default files confuse users.** `未命名.base` and `欢迎.md` are auto-created by Obsidian, not by agent-vault. Safe to delete.
15. **Agent skips vault read on session resume.** When the user says "继续做X项目" or resumes work on a known project, **read `docs/vault/00_HOME.md` FIRST** before asking questions or inspecting files. The vault exists to survive context compression. Not reading it forces the user to re-explain everything. If the vault is stale, sync it — don't ignore it.
16. **Batching vault updates at end.** Agents write code, commit, write more code, commit — then try to reconstruct what happened for the vault at the end. By then, details are lost. **Update vault files IMMEDIATELY after each code commit.** See "Continuous Sync Rule" section. If the user has to remind you to update the vault, the workflow has failed.
17. **Trusting MEMORY over vault for project status.** MEMORY stores cross-project facts (paths, ports, user prefs) but can go stale on project-specific status (deployment state, feature completeness, current bugs). When MEMORY says "Vercel已部署" but the vault says "待配置", **the vault wins**. Always read `01_CURRENT_BASELINE.md` for current status, not MEMORY. If MEMORY contradicts the vault, update MEMORY to match.
18. **User says X, vault says Y — trust the vault, verify user.** When the user answers a clarification question with info that contradicts what the vault documents, **stop and verify before acting**. Example: user says "GitHub Pages" but vault says "待配置: Vercel/Cloudflare". Don't blindly add `base: '/worldcup-2026/'` — check the vault's deployment section first. The user may be misremembering or describing intent, not current state. Always cross-reference with vault before making config changes based on user-provided context.
18. **Context compaction destroys vault-awareness.** When Hermes compresses context and summary generation fails, all session knowledge is lost. If `abort_on_summary_failure` is `false`, the agent drops to zero context and starts guessing from MEMORY. **Set `abort_on_summary_failure: true` in Hermes config.** The vault exists precisely to survive this — but only if the agent actually reads it at session start.
19. **CLAUDE.md / AGENTS.md not created for Claude Code/Codex.** When using project-vault with external agents (Claude Code, Codex), create `CLAUDE.md` at project root pointing to vault files. Without it, external agents skip vault entirely. See `references/claude-code-integration.md`.
20. **Vault goes stale despite "边做边更新" rule.** The #1 failure mode in practice. Agents simply forget mid-work. **Fix: VAULT STARTUP SYNC** — put a staleness check in `00_HOME.md` right after frontmatter so the agent catches drift at session start, not mid-task. See `references/vault-startup-sync-pattern.md`. Deployed to all 6 projects as of 2026-06-10.
21. **execute_code read_file embeds line numbers.** When batch-processing vault files with `execute_code`, `read_file()` returns `1|content` format. Writing back with `write_file()` permanently embeds line numbers. **Fix:** Use `terminal("cat '<path>'")` for raw content. See `references/vault-startup-sync-pattern.md`.

## Verification Checklist

### After Init
- [ ] Phase-appropriate vault files exist
- [ ] `assets/intake/reports/` directory created
- [ ] `VAULT_SCHEMA.md` has project_phase, vault_version, thresholds
- [ ] `00_HOME.md` has agent entry page
- [ ] Every file has full metadata (type, status, confidence, last_updated, owner, reviewed_by)
- [ ] Security rules added to `03_DO_NOT_TOUCH.md` from .env/.gitignore analysis
- [ ] No secrets in any vault file
- [ ] Vault committed to Git

### After Sync
- [ ] `01_CURRENT_BASELINE.md` reflects current HEAD
- [ ] Changed areas have updated vault files
- [ ] Metadata updated (last_updated, confidence)
- [ ] `VAULT_CHANGELOG.md` has sync entry
- [ ] Vault committed to Git

### After Audit
- [ ] 10-point checklist completed
- [ ] Staleness thresholds from VAULT_SCHEMA.md (not hardcoded)
- [ ] Full report in assets/intake/reports/
- [ ] Summary in 10_REPORT_INDEX.md
- [ ] Critical issues resolved or flagged

## Script Tooling

Four scripts handle the full lifecycle:

| Script | Purpose | Usage |
|--------|---------|-------|
| `init-vault.sh` | Create vault from scratch | `bash templates/init-vault.sh . "Project" mvp` |
| `sync-vault.sh` | Scan git changes, suggest updates | `bash templates/sync-vault.sh .` |
| `audit-vault.sh` | 10-point health check | `bash templates/audit-vault.sh .` |
| `setup-obsidian-link.sh` | Connect Obsidian + auto-color | `bash templates/setup-obsidian-link.sh docs/vault "Name"` |

All scripts are in `templates/` and work on macOS, Linux, Windows (WSL).

## QUICKSTART

For new users: see `QUICKSTART.md` in the GitHub repo — 3-step setup in under 30 seconds.
For a working demo: see `example-vault/` in the GitHub repo — complete Todo App vault.

## Content & Documentation Style

When creating READMEs, docs, or GitHub content for this skill:

- **Keep it simple.** This is a small helper tool, not an enterprise framework. Don't make it look "professional" or "complex."
- **Always include a screenshot.** One real Obsidian Graph View screenshot is worth 1000 words. Place it at the bottom of the Chinese README, resized to 500px: `<img src="assets/graph-view-demo.png" width="500">`
- **Bilingual = separate files.** `README.md` (English) + `README.zh-CN.md` (Chinese). GitHub auto-detects `zh-CN` and shows a language switcher. Don't mix languages in one file.
- **Lead with the 30-second pitch.** What is it → one command to start → what you get. Details below.
- **No walls of text.** Tables > paragraphs. Code blocks > descriptions.

- `references/vault-tencentdb-integration.md` — how Vault + TencentDB Memory complement each other

## GitHub Sharing

```bash
mkdir project-vault && cd project-vault
git init
cp -r ~/.hermes/skills/software-development/project-vault/* .
cp templates/STANDALONE_README.md README.md
git add . && git commit -m "initial: project vault v5.0.0"
gh repo create project-vault --public --source=. --push
```

## Philosophy

> **Project Vault is not a documentation folder. It's a project operating system — human-visual + agent-executable.**

- Agent writes structured knowledge
- Human verifies and enriches in Obsidian
- Both parties benefit from the shared knowledge base
- The vault adapts to the project's phase
- Security is enforced, not assumed

**One rule to remember:**
Every project starts with `docs/vault/`. Every Agent starts with `00_HOME.md`. No exceptions.
