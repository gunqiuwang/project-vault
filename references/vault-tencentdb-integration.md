# Vault + TencentDB Memory Integration

## Why Both

Project Vault and TencentDB Agent Memory solve different problems:

| | Project Vault | TencentDB Memory |
|---|---|---|
| Stores | Project knowledge (arch, decisions, danger zones) | Conversation memory (L0→L3) |
| Format | Structured markdown, git-tracked | SQLite + BM25/vector search |
| Written by | Agent (during work, manual) | LLM (auto-extracted from conversations) |
| Read by | Agent + human (Obsidian) | Agent (recall API) |
| Survives | Context compression (file on disk) | Context compression (DB) |
| Strength | Structured, auditable, human-readable | Automatic capture, cross-session search |

## Integration Pattern (Lightweight)

**Do NOT** build sync bridges. Use Agent reading order as the connector.

### In each project's `00_HOME.md`, add to Agent Entry Page section:

```markdown
**If vault information is incomplete, search conversation history:**
`memory_tencentdb_memory_search(query="project-name relevant-keyword")`
```

### Agent Reading Order with TencentDB:

```
1. Read vault (00_HOME → 01_BASELINE → 03_DO_NOT_TOUCH → task-specific)
2. If info missing → memory_tencentdb_conversation_search / memory_tencentdb_memory_search
3. If still missing → ask user
```

## When TencentDB Covers Vault Gaps

- Context was compressed mid-session → TencentDB L0 recovers conversation
- Decision discussed in chat but never written to vault → L0 has it
- User preference correction → L1 auto-captures it
- Multi-session project context → survives across sessions automatically

## When Vault Covers TencentDB Gaps

- Structured state (branch, commit, deploy) → `01_CURRENT_BASELINE.md`
- Explicit danger zones → `03_DO_NOT_TOUCH.md`
- Audit trail → `VAULT_CHANGELOG.md` (append-only, git-tracked)
- Human-readable project overview → `00_HOME.md`

## Anti-Patterns

1. **Auto-sync vault ↔ TencentDB** — different lifecycles, different audiences. Coupling creates maintenance burden.
2. **Putting vault content into TencentDB manually** — vault is the structured source of truth; TencentDB captures what naturally flows through conversation.
3. **Relying only on TencentDB for project state** — DB can lose data; git-tracked vault files are more durable.
4. **Relying only on vault for context recovery** — vault won't capture conversations that never made it into structured files.
