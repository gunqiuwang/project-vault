# Iterative Skill Development Pattern

> How project-vault was built: from v1.0 to v5.0.0 through conversation-driven iteration.

## The Pattern

1. **Start with user's raw prompt** — don't over-engineer upfront
2. **Build v1, get feedback** — user sees gaps immediately
3. **Absorb external ideas** — user suggests improvements from other systems (e.g., Karpathy's LLM Wiki)
4. **Real-world test** — run on actual project, discover what breaks
5. **Fix and iterate** — each fix reveals the next gap
6. **Rename when scope changes** — "Agent Vault" → "Project Vault" when humans became users too

## Version History

| Version | What Changed | Why |
|---------|-------------|-----|
| v1.0 | Basic init + 11 vault files | Original template |
| v2.0 | + sync/audit lifecycle | "Only init, no maintenance" gap |
| v3.0 | + VAULT_SCHEMA, quality signals, orphan detection | Absorbed llm-wiki patterns |
| v3.1 | + Obsidian integration | User installed Obsidian |
| v4.0 | + standardized metadata, reviewed_by, report separation, task-end rules | User's 3 conventions |
| v4.1 | + greenfield mode, vault upgrade/score, multi-agent protocol, security rules, project phases | 12-gap audit |
| v4.1.1 | + cross-platform Obsidian script, WSL junction fix | Real-world test on 二字日记 |
| v5.0 | + Graph link discipline, rename to project-vault | User: "不只是 Agent 看" |

## Lessons Learned

1. **Theory < Practice** — The Obsidian symlink issue (`ln -sf` invisible to Windows) was only discovered by actually running vault init on a real project. Always test on real projects before declaring done.

2. **User corrections are gold** — Each user suggestion (metadata fields, report separation, link discipline) made the skill significantly better. Don't resist, absorb.

3. **Scope creep is evolution** — The skill started as "init template" and became "project operating system". Rename when the name no longer fits.

4. **Cross-platform is never free** — WSL↔Windows has specific gotchas (symlinks, UNC paths, PowerShell vs cmd). Always test on the target platform.

5. **Incremental patches > full rewrites** — Used `patch` for most changes, `write_file` only when the file needed complete restructuring.
