# Vault Sync Discipline

> User correction: "agent 不会自己一边做项目一边更新 Project Vault"
> This is the #1 failure mode of vault-based workflows.

## The Problem

Agents tend to finish all code changes, then update the vault at the end. But "later" = never, because:
- Context gets compressed and details are lost
- The agent forgets what changed and why
- Vault becomes stale and useless

## The Rule

**Every code change MUST update the vault DURING the work, not after.**

| Code Action | Vault Action | When |
|-------------|-------------|------|
| `git commit` code | Update `01_CURRENT_BASELINE.md` | Immediately after commit |
| Fix a bug | Append to `08_INCIDENTS_AND_FIXES.md` | Immediately after fix |
| Make architecture decision | Append to `02_DECISION_LOG.md` | Immediately after decision |
| Add/delete component | Update `05_COMMANDS_AND_FILES.md` | Immediately |
| Change deploy method | Update `06_DEPLOYMENT.md` | Immediately |
| Final commit | `git add docs/vault/ && git commit -m "docs: vault sync"` | End of task |

## Anti-Patterns (Forbidden)

- ❌ Finish all features, then update vault in one batch
- ❌ Only update code, never update vault
- ❌ Wait for user to remind you to update vault

## Implementation

Embed this in each project's `09_AGENT_PROMPTS.md` under a `## 🔴 CORE RULE` heading. The rule must be the FIRST thing in the file, before any prompt templates.

## Template for 09_AGENT_PROMPTS.md

```markdown
## 🔴 CORE RULE: 边做边更新 Vault

**Every code change MUST update the vault DURING the work, NOT after.**

具体来说：
- 每次 commit 代码后 → 立即同步更新 `01_CURRENT_BASELINE.md`
- 每次修复 bug → 立即追加 `08_INCIDENTS_AND_FIXES.md`
- 每次做架构决策 → 立即追加 `02_DECISION_LOG.md`
- 每次新增/删除文件 → 立即更新 `05_COMMANDS_AND_FILES.md`
- 最后一次 commit 包含 vault 变更，前缀 `docs:`

**反模式（禁止）：**
- ❌ 做完所有功能再一次性更新 vault（记忆已丢失，信息不准确）
- ❌ 只更新代码不更新 vault（vault 变成废纸）
- ❌ 等用户提醒才更新 vault
```
