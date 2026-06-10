# Vault Startup Sync Pattern

## Problem
Agents complete work (commits, features, fixes) but never update vault files. After 3+ days, vault is stale by 30+ commits. The "边做边更新" rule fails because agents forget during work, not because they don't know the rule.

## Solution: Check-First-Read-Later
Make vault staleness detection the **very first action** when entering a project. Zero extra cost — one `git log` command.

### Trigger Chain
```
MEMORY.md → "先读 00_HOME.md（含 VAULT STARTUP SYNC 过期检查）"
  ↓
00_HOME.md → VAULT STARTUP SYNC block (right after frontmatter)
  ↓
git log --oneline --since=<last_updated>
  ↓
有未同步 → 先 sync 再干活 | 没过期 → 正常开工
```

### Placement
VAULT STARTUP SYNC block goes in `00_HOME.md` **right after frontmatter**, before all other content.

### Block Template
```markdown
## 🔴 VAULT STARTUP SYNC (第一步，读任何文件之前)

**vault 可能已过期。先检查，再开工：**

1. 读本文件的 last_updated（上方 frontmatter）
2. cd 到项目根目录
3. git log --oneline --since=<last_updated> | grep -v "chore: update news" | grep -v "docs:"
4. 如果有未同步的 commit → 先跑 vault sync，再开始干活

**如果 vault 是最新的 → 正常开工，继续读下方 Mandatory reading order。**
```

### Why Not Cron
Daily LLM cron = ~50K tokens/run (~1.5M/month) just to check timestamps. Check-first uses one shell command (zero tokens) and only triggers full sync when needed.

### Deployment Checklist
1. Add block to `00_HOME.md` after frontmatter
2. Add detailed sync instructions to `09_AGENT_PROMPTS.md`
3. Update MEMORY.md 开工纪律 to reference sync check
4. Update skill template for future projects

## Pitfall: execute_code + read_file Line Numbers
`read_file()` inside `execute_code` returns content with line number prefixes (`1|content`). Writing back with `write_file()` embeds line numbers permanently.

**Fix:** Use `terminal("cat '<path>'")` for raw content, or strip `^\s*\d+\|` regex before writing.

## Real-World Data Point
世界杯项目 2026-06-10: 37 commits in 3 days, vault completely stale. Manual sync took ~15 min.
