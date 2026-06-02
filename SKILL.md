---
name: project-vault
description: "Use when starting any new project, onboarding an existing codebase, or syncing project knowledge after changes. Creates and maintains a structured knowledge vault (docs/vault/) with quality signals, orphan detection, project phases, and lifecycle management. Human-visual + agent-executable project operating system."
version: 5.0.0
author: guoku
license: MIT
platforms: [linux, macos, windows, wsl]
metadata:
  hermes:
    tags: [project-init, knowledge-base, documentation, onboarding, vault, agent-safety, lifecycle, schema, quality, obsidian, phases]
    related_skills: [writing-plans, requesting-code-review, codebase-inspection, plan, llm-wiki, systematic-debugging, obsidian]
# References: design-rationale.md, audit-methodology.md, obsidian-integration.md, walkthrough-two-char-diary.md, walkthrough-worldcup.md, iterative-development-pattern.md, wsl-github-push-proxy.md
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
├── 00_HOME.md                          # Agent entry page + project overview
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

**Critical: Add `aliases` to distinguish projects in Obsidian Graph View.**

```yaml
---
type: home
aliases: ["项目中文名", "Project English Name", "project-slug"]
---
```

Without aliases, Graph View shows multiple identical `00_HOME` nodes and you can't tell which project is which.

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

## Agent Task-End Rule

**Every Agent task MUST end with these updates:**

1. **`01_CURRENT_BASELINE.md`** — if branch, commit, or project status changed
2. **`10_REPORT_INDEX.md`** — if any report was generated (full report → `assets/intake/reports/`)
3. **`VAULT_CHANGELOG.md`** — append a log entry

No exceptions. A task that changes the project but doesn't update the vault is incomplete.

## How Init Works

### Mode 1: Standard Init (existing codebase)

**Option A: Automated script (recommended)**

```bash
bash templates/init-vault.sh /path/to/project "Project Name" mvp
```

The script auto-detects: phase, tech stack, commands, sensitive patterns, .gitignore.
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

## Obsidian Integration

Project Vault uses Obsidian-native `[[wikilinks]]` syntax.

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

### Pitfall: Obsidian Default Files

New vaults in Obsidian auto-create `未命名.base` and `欢迎.md`. These are Obsidian defaults, not vault content. Safe to delete.

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
Write incident report to assets/intake/reports/YYYY-MM-DD_incident-{slug}.md
Add summary to 10_REPORT_INDEX.md. Set reviewed_by: agent.
```

### Feature

```
Read vault. Identify affected modules. Propose implementation plan.
Do not touch files in 03_DO_NOT_TOUCH.md without approval.
Run tests. Update 01_CURRENT_BASELINE.md. Append to VAULT_CHANGELOG.md.
```

### Task Completion (ALWAYS last)

```
Task complete. Now update the vault:
1. If branch/commit/status changed → update 01_CURRENT_BASELINE.md
2. If report generated → write to assets/intake/reports/, add summary to 10_REPORT_INDEX.md
3. Append entry to VAULT_CHANGELOG.md
4. Update last_updated on all changed vault files
5. Commit vault changes with prefix "docs:"
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

## Common Pitfalls

1. **Agent skips vault read.** Enforce startup checklist from `00_HOME.md`.
2. **Vault becomes stale.** Use `vault sync` after significant changes.
3. **03_DO_NOT_TOUCH is too vague.** Name exact files, exact commands, exact conditions.
4. **Inventing facts.** Write "Unknown — not verified in this pass." Set `confidence: low`.
5. **No metadata.** Every file MUST have full frontmatter.
6. **Orphan references.** After deleting a project file, check if vault references it.
7. **Reports in vault.** Full reports go in `assets/intake/reports/`, not `docs/vault/`.
8. **Secrets in vault.** Never put API keys, passwords, or internal URLs in vault files.
9. **Hardcoded thresholds.** Staleness/review thresholds belong in `VAULT_SCHEMA.md`.
10. **No phase awareness.** Don't create 08_INCIDENTS for an idea-phase project.
11. **Multi-agent conflicts.** Check write protocol in `VAULT_SCHEMA.md` before editing state files.
12. **Never upgrading.** Run `vault upgrade` when skill version changes or phase changes.
13. **WSL symlink doesn't work with Windows Obsidian.** `ln -sf` creates Linux symlinks that Windows can't read. Use `powershell.exe -Command "cmd /c mklink /J"` for directory junctions instead.
14. **Obsidian default files confuse users.** `未命名.base` and `欢迎.md` are auto-created by Obsidian, not by agent-vault. Safe to delete.

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
