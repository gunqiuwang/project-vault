# TencentDB + Vault Sync Pattern

## Problem
Project vaults go stale because agents forget to update them during work. The "边做边更新" rule is aspirational but unreliable in practice.

## Solution: TencentDB as Vault Auditor
TencentDB Agent Memory automatically captures all conversations (L0 layer). Use this as ground truth to detect vault staleness.

## Workflow

### 1. Detect Staleness
For each project with a vault:
- Read `docs/vault/VAULT_SCHEMA.md` → get `staleness_threshold_days`
- Read `docs/vault/01_CURRENT_BASELINE.md` → get `last_updated`
- Run `git log --oneline --since=<last_updated>` → count missing commits
- If commits exist and threshold exceeded → stale

### 2. Find Missing Context
- Search TencentDB: `conversation_search(query="<project-name> <keyword>")`
- Filter by date range (after vault's last_updated)
- Extract: new decisions, incidents, feature changes, architecture shifts

### 3. Categorize Commits → Vault Files

| Commit prefix | Update these vault files |
|---------------|-------------------------|
| `feat:` | 01_BASELINE, 04_ARCHITECTURE, 05_COMMANDS, VAULT_CHANGELOG |
| `fix:` | 01_BASELINE, 08_INCIDENTS, VAULT_CHANGELOG |
| `refactor:` | 01_BASELINE, 04_ARCHITECTURE, VAULT_CHANGELOG |
| `remove:` | 01_BASELINE, 04_ARCHITECTURE, 05_COMMANDS, VAULT_CHANGELOG |
| `style:` | 01_BASELINE (usually skip unless major) |
| `docs:` | VAULT_CHANGELOG only |
| `chore:` | Skip (usually automated) |

### 4. Write Updates
- Use `patch` tool for targeted edits (update last_updated, add entries)
- Use `write_file` for full rewrites when major restructuring needed
- Always update `VAULT_CHANGELOG.md` with sync summary
- Always commit: `git commit -m "docs: vault sync — N commits补更新"`

### 5. Report
Summarize what was stale, what was updated, any decisions/incidents found in TencentDB but missing from vault.

## Cron Job Template

```yaml
# Nightly vault health check
schedule: "0 22 * * *"  # 10pm daily
prompt: |
  For each project in ~/.hermes/memory paths:
  1. Find vault: docs/vault/VAULT_SCHEMA.md
  2. Check staleness_threshold_days and last_updated
  3. git log --oneline --since=<last_updated> in project dir
  4. If stale: run full vault sync (categorize commits, update files)
  5. If not stale: skip silently
  6. Report summary of any changes made
```

## Real-World Example (2026-06-10)
worldcup2026 vault was 3 days behind. 37 commits found.
- 9 vault files updated
- 6 new incidents documented
- 3 new decisions logged
- Visual upgrade details captured (FotMob MatchCard, split-flap countdown, etc.)
- Committed as `a6c21b1 docs: vault sync — 37 commits补更新`
