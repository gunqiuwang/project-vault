# Example Vault — Todo App

This is a **complete example** of what Project Vault produces.

It shows a vault for a fictional "Todo App" built with React + Express.

## Files

```
docs/vault/
├── 00_HOME.md              ← Agent entry page (with aliases)
├── 01_CURRENT_BASELINE.md  ← Current state with git log
├── 02_DECISION_LOG.md      ← SQLite vs PostgreSQL decision
├── 03_DO_NOT_TOUCH.md      ← Schema + CRUD logic protected
├── 04_ARCHITECTURE.md      ← React + Express + SQLite
├── 05_COMMANDS_AND_FILES.md ← Commands by risk level
├── ... (13 files total)
```

## What to Notice

- **Every file has metadata** (type/status/confidence/last_updated/owner/reviewed_by)
- **00_HOME has aliases** so Obsidian Graph View shows "Todo App" not "00_HOME"
- **03_DO_NOT_TOUCH is specific** — names exact files, exact reasons
- **02_DECISION_LOG records "why"** — not just what, but why and alternatives
- **05_COMMANDS classifies by risk** — 🟢 Safe → 🔴 Critical

## Try It

1. Fork this repo
2. Open in Obsidian → see Graph View
3. Run `audit-vault.sh example-vault/` → see the health check
