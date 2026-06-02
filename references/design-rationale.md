# Agent Vault — Design Rationale

## Why a Lifecycle System, Not Just Init

An init-only skill creates artifacts that go stale within weeks. The real value is keeping knowledge current. Agent Vault has 6 lifecycle commands:

1. **init** — Create from scratch (one-time)
2. **init --greenfield** — Minimal vault for empty projects
3. **sync** — Update affected files after changes (ongoing)
4. **audit** — Detect stale knowledge (periodic)
5. **upgrade** — Migrate vault structure on version/phase change
6. **score** — Calculate health score (0-100)

## Change→File Mapping

The core mechanism that makes sync work. Without it, "sync" means "rebuild everything". With it, sync only touches what changed.

## Why Obsidian-Style Links

`[[01_CURRENT_BASELINE]]` works in Obsidian, VS Code with Foam, and is readable as plain text. It creates a navigable knowledge graph when viewed in compatible editors.

## Naming Evolution

- `project-vault-init` — Too narrow (implies init-only)
- `vault-system` — Too abstract
- `agent-vault` — ✅ Emphasizes the audience (agents) and the artifact (vault)

Rule: Name the class of work, not the first action.

## Cross-Pollination from llm-wiki (v3.0)

Key designs borrowed and adapted from Karpathy's LLM Wiki:

| Feature | llm-wiki Original | agent-vault Adaptation |
|---------|------------------|----------------------|
| Quality signals | `confidence` + `contested` in frontmatter | Same, applied to all vault files |
| SCHEMA.md | Domain rules, tag taxonomy | `VAULT_SCHEMA.md` with project-specific rules |
| Append-only log | `log.md` with date+action format | `VAULT_CHANGELOG.md` with rotation |
| Orphan detection | Pages with no inbound links | Extended: deleted-file refs, zero-inbound, placeholders |
| Page thresholds | When to create/split/archive | Adapted with urgency levels |

**What was NOT borrowed:** `raw/` immutable layer, sha256 checksums, entity page types, Obsidian Sync.

## v4.0 — User-Driven Conventions

User proposed 3 conventions:

1. **Standardized frontmatter** — `type/status/confidence/last_updated/owner` on every file
2. **Task-end rule** — every agent task MUST update `01_BASELINE` + `10_REPORT_INDEX` + `VAULT_CHANGELOG`
3. **Report separation** — full reports in `assets/intake/reports/`, vault only has summaries

**Lesson:** User-provided conventions > agent-invented ones. Always ask "what conventions do you want?" before finalizing.

## v4.1 — 12-Issue Systematic Audit

A critical review found 12 gaps (4 logic defects, 4 process gaps, 4 enhancements):

| Category | Count | Examples |
|----------|-------|---------|
| Logic defects | 4 | Report contradiction, missing mkdir, field name inconsistency, empty-project edge case |
| Process gaps | 4 | No upgrade path, no multi-agent protocol, hardcoded thresholds, security blind spots |
| Enhancements | 4 | Project phases, reviewed_by field, split/merge docs, health score |

See `references/audit-methodology.md` for the full audit pattern.
