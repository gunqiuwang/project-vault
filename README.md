# 🏛️ Project Vault

> Project operating system — human-visual + agent-executable. Creates and maintains a structured knowledge vault so any agent (or human) can safely understand, maintain, and extend your project.

English | [中文](README.zh-CN.md)

## ⚡ 3-Step Quick Start → [QUICKSTART.md](QUICKSTART.md) | [中文](QUICKSTART.md#中文版)

See a live example → [`example-vault/`](example-vault/)

---

## What Is This?

AI agents often lack context when working on projects — they don't know what's safe to touch, what commands to run, or how the architecture works. **Project Vault** solves this by creating a structured knowledge base under `docs/vault/` that agents read before making any changes.

It's not just "init and forget" — it's a **full lifecycle system** with init, sync, audit, upgrade, and score capabilities.

## Quick Start

### Step 1: Get the Templates

**Option A: Download ZIP**

1. Click **Code → Download ZIP** on this GitHub page
2. Extract, copy `templates/INIT_PROMPT.md` to your project root

**Option B: Git Clone**

```bash
git clone https://github.com/gunqiuwang/project-vault.git /tmp/project-vault
cp /tmp/project-vault/templates/INIT_PROMPT.md /your/project/
```

**Option C: Hermes Agent** (built-in, no download needed)

```markdown
Run project-vault with action: init
```

### Step 2: Paste the Prompt to Your AI

Copy the contents of `INIT_PROMPT.md` and paste them into your AI agent's chat.

Works with: ChatGPT, Claude, Gemini, Copilot, DeepSeek, or any AI that can read a prompt.

The AI will automatically:
1. Inspect your project (read-only, no code changes)
2. Create `docs/vault/` with 13 structured knowledge files
3. Fill them with real project data
4. Commit to Git

**Platform shortcuts** (store as project file for one-command access):

<details>
<summary>Claude Code</summary>

```bash
cp /tmp/project-vault/templates/INIT_PROMPT.md .claude/commands/init-project-vault.md
# Then: /init-project-vault
```
</details>

<details>
<summary>Cursor</summary>

```bash
cp /tmp/project-vault/templates/INIT_PROMPT.md .cursor/rules/init-project-vault.md
# Then: @init-project-vault
```
</details>

<details>
<summary>GitHub Copilot</summary>

```bash
cp /tmp/project-vault/templates/INIT_PROMPT.md .github/copilot-init-vault.md
# Then: @workspace read .github/copilot-init-vault.md and execute it
```
</details>

<details>
<summary>Aider</summary>

```bash
cp /tmp/project-vault/templates/INIT_PROMPT.md .aider-init-vault.md
# Then: aider --read .aider-init-vault.md
```
</details>

<details>
<summary>Windsurf / Codeium</summary>

```bash
mkdir -p .windsurf/rules
cp /tmp/project-vault/templates/INIT_PROMPT.md .windsurf/rules/init-project-vault.md
```
</details>

### Step 3: Connect Obsidian (Optional but Recommended)

Obsidian is a free app that visualizes your vault's knowledge graph.

1. **Download Obsidian**: [obsidian.md](https://obsidian.md) (free, all platforms)
2. **Run the setup script**:

```bash
bash /tmp/project-vault/templates/setup-obsidian-link.sh /your/project/path/docs/vault "Project Name"
```

3. **Open Obsidian**, select your vault directory
4. **Sidebar** shows all vault files, **Graph View** (Ctrl+G) shows the knowledge map

### Step 4: Daily Use

Every time you ask an AI to work on your project, add one line:

```
Read docs/vault/00_HOME.md before making changes.
```

Switch models, switch agents, switch platforms — this one line is all you need.

## Full Workflow

```
User downloads Project Vault templates
        ↓
Paste INIT_PROMPT.md to AI Agent
        ↓
AI creates docs/vault/ automatically (13 files)
        ↓
User connects Obsidian (optional)
        ↓
┌──────────────────────────────────────────┐
│         Daily Development Loop           │
│                                          │
│  AI reads 00_HOME → understands → works  │
│       ↓                                  │
│  Task done → update vault → git commit   │
│       ↓                                  │
│  Obsidian auto-refreshes → user reviews  │
│       ↓                                  │
│  Next AI reads 00_HOME → loop repeats    │
└──────────────────────────────────────────┘
```

## 6 Lifecycle Commands

| Command | When | What It Does |
|---------|------|-------------|
| `vault init` | New project / onboarding | Create vault from scratch |
| `vault init --greenfield` | Empty project (idea only) | Minimal vault, grow later |
| `vault sync` | After significant changes | Update affected vault files |
| `vault audit` | Monthly / before handoff | Health check, detect stale knowledge |
| `vault upgrade` | Skill version bump / phase change | Migrate vault structure |
| `vault score` | Anytime | Calculate vault health (0-100) |

## Vault Structure

```
docs/vault/
├── 00_HOME.md                    # Agent entry page (single entry point)
├── 01_CURRENT_BASELINE.md        # Source of truth: branch, commit, status
├── 02_DECISION_LOG.md            # Why we made key choices
├── 03_DO_NOT_TOUCH.md            # 🚫 Danger zones + security rules
├── 04_ARCHITECTURE.md            # Tech stack, data flow
├── 05_COMMANDS_AND_FILES.md      # What you can run and touch
├── 06_DEPLOYMENT.md              # How to ship it
├── 07_TESTING_AND_VERIFICATION.md # How to verify it works
├── 08_INCIDENTS_AND_FIXES.md     # What broke and how we fixed it
├── 09_AGENT_PROMPTS.md           # Reusable prompts for tasks
├── 10_REPORT_INDEX.md            # Report summaries only
├── VAULT_SCHEMA.md               # Project rules + thresholds
├── VAULT_CHANGELOG.md            # Append-only operation log
└── templates/                    # Template files

assets/intake/reports/            # Full reports (outside vault graph)
```

## Project Phases

The vault adapts to your project's lifecycle:

| Phase | Description | Files Required |
|-------|-------------|---------------|
| **idea** | Just the vision | 00_HOME + 04_ARCHITECTURE |
| **prototype** | Working code, no deploys | + 01_BASELINE + 05_COMMANDS |
| **mvp** | First users | + 03_DO_NOT_TOUCH + 06_DEPLOY + 07_TESTING |
| **growth** | Full vault | All 13 files |
| **maintenance** | Focus on decisions + incidents | All 13 files |
| **sunset** | Read-only project | 00_HOME + 03_DO_NOT_TOUCH only |

## Obsidian Integration

### Setup

```bash
# One command, auto-detects your OS
bash templates/setup-obsidian-link.sh /your/project/path/docs/vault "Project Name"
```

| Your System | Script Handles It |
|------------|-------------------|
| macOS | Creates symlink |
| Linux | Creates symlink |
| Windows | Creates junction (no admin needed) |
| WSL + Windows | Creates junction (no admin needed) |

### Graph View Link Discipline

```
00_HOME (hub — largest node)
├──→ 01_CURRENT_BASELINE
├──→ 03_DO_NOT_TOUCH
├──→ 05_COMMANDS_AND_FILES
├──→ 09_AGENT_PROMPTS (second entry)
├──→ 10_REPORT_INDEX (report gateway)
└──→ task-specific files
```

### What You Can Do in Obsidian

| Feature | Use Case |
|---------|----------|
| **Graph View** | See project knowledge map, 00_HOME is the center |
| **Backlinks** | See which files reference the current file |
| **Search** | Global search across vault content |
| **Direct Edit** | Edit vault files in Obsidian, AI reads them next time |
| **Dataview Plugin** | Query `confidence: low` or `status: stale` files |

### Human-Agent Loop

```
AI Agent writes vault files → Git commit
        ↓
Obsidian auto-refreshes (file watcher)
        ↓
You review, annotate, edit in Obsidian
        ↓
Next AI Agent reads 00_HOME → reads your confirmed version
```

## Standardized Metadata

Every vault file has:

```yaml
---
type: baseline          # File type
status: active          # active / stale / archived
confidence: high        # high / medium / low
last_updated: 2026-06-02
owner: both             # agent / human / both
reviewed_by: human      # agent / human / unreviewed
---
```

Query in Obsidian with Dataview:

```dataview
LIST FROM "docs/vault" WHERE confidence = "low"    -- Find uncertain content
LIST FROM "docs/vault" WHERE status = "stale"      -- Find outdated files
LIST FROM "docs/vault" WHERE reviewed_by = "unreviewed"  -- Find unconfirmed
```

## Why This Matters

| Without Vault | With Vault |
|--------------|------------|
| AI breaks production | AI reads DO_NOT_TOUCH first |
| AI rewrites working code | AI knows what must not regress |
| AI runs dangerous commands | AI checks command risk levels |
| AI invents facts | AI reads baseline source of truth |
| No record of decisions | Decision log preserves context |
| Incidents repeat | Incident log prevents recurrence |
| Switching AI = re-explain everything | Read 00_HOME and it's all there |
| Vault goes stale | Sync + audit keep it current |

## Templates Included

| File | Purpose |
|------|---------|
| `INIT_PROMPT.md` | Full initialization prompt (paste into any AI) |
| `setup-obsidian-link.sh` | Cross-platform Obsidian setup script |
| `DECISION_TEMPLATE.md` | Record architectural decisions |
| `INCIDENT_TEMPLATE.md` | Document incidents and fixes |
| `DEPLOY_REPORT_TEMPLATE.md` | Verify deployments |
| `AGENT_TASK_TEMPLATE.md` | Define safe agent tasks |
| `git-hook-post-commit` | Git hook to remind vault sync |
| `ci-vault-check.yml` | GitHub Actions health check |

## Philosophy

1. **Read before write** — Agents must understand before they change
2. **Explicit over implicit** — Document what's dangerous, don't assume
3. **Living documentation** — Update the vault as the project evolves
4. **Safety first** — DO_NOT_TOUCH.md prevents the most common agent mistakes
5. **Audit regularly** — Stale knowledge is worse than no knowledge
6. **Human-agent loop** — Agent writes structured knowledge, human verifies in Obsidian

## Contributing

1. Fork this repo
2. Improve templates or add new ones
3. Submit a PR

## License

MIT — Use freely, modify as needed.

---

*"The best time to document a project was at the start. The second best time is now."*
