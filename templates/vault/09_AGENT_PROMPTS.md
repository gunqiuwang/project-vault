---
type: agent-prompts
status: active
confidence: high
last_updated: YYYY-MM-DD
owner: both
reviewed_by: unreviewed
---

# Agent Prompts

## 🔴 VAULT STARTUP SYNC (每次开工必做)

**在做任何事情之前，先检查 vault 是否过期：**

```
1. cat docs/vault/00_HOME.md → 获取 last_updated 日期
2. git log --oneline --since=<last_updated> | grep -v "chore: update news" | grep -v "docs:"
3. 如果有未同步的 commit → 先执行 vault sync，再开始干活
```

**vault sync 流程：**
```
1. git log --oneline --since=<vault_last_updated> | grep -v "chore: update news"
2. 按 commit 类型归类: feat/fix/refactor/remove
3. 更新受影响的 vault 文件（参考 VAULT_CHANGELOG 中的变更→文件映射）
4. git commit -m "docs: vault sync — <简述>"
```

**为什么：** vault 腐烂的原因不是没有自动化，而是 agent 做完活忘了更新。这个检查让 vault 同步变成每个 session 的第一个动作，零额外成本。

## 🔴 CORE RULE: 边做边更新 Vault

**Every code change MUST update the vault DURING the work, NOT after.**

| When | Update This File |
|------|-----------------|
| Commit code | `01_CURRENT_BASELINE.md` |
| Fix a bug | `08_INCIDENTS_AND_FIXES.md` |
| Make architecture decision | `02_DECISION_LOG.md` |
| Add/remove files | `05_COMMANDS_AND_FILES.md` |
| Change deploy method | `06_DEPLOYMENT.md` |

**Anti-patterns (FORBIDDEN):**
- ❌ Finish all work then update vault in one batch (memory lost, info inaccurate)
- ❌ Only update code, never update vault (vault becomes worthless)
- ❌ Wait for user to remind you to update vault

**Correct pattern:**
- ✅ Code changes → vault files update simultaneously
- ✅ Last commit of work session includes vault changes with prefix `docs:`

## New Task Startup (ALWAYS use this first)

```
Read docs/vault/00_HOME.md, docs/vault/01_CURRENT_BASELINE.md,
docs/vault/03_DO_NOT_TOUCH.md, and docs/vault/05_COMMANDS_AND_FILES.md
before making changes.

Karpathy Principles (always apply):
1. Think Before Coding — state assumptions, surface tradeoffs, ask when confused
2. Simplicity First — minimum code, no speculative features
3. Surgical Changes — touch only what's needed, every line traces to the request
4. Goal-Driven Execution — define success criteria, loop until verified

Do not change unrelated systems.
Do not deploy unless explicitly asked.
State your plan and success criteria before editing.
```

## Bugfix Prompt

```
Read the project vault first (00_HOME → 01_BASELINE → 03_DO_NOT_TOUCH → 05_COMMANDS).

Task: Fix {BUG_DESCRIPTION}.

1. Identify the bug → verify: root cause clearly stated
2. Propose fix with affected files (surgical, no refactoring) → verify: diff only touches bug
3. Implement fix → verify: tests pass, build clean
4. 【边做边更新】Immediately append 08_INCIDENTS_AND_FIXES.md
5. 【边做边更新】Immediately update 01_CURRENT_BASELINE.md
6. Write incident report to assets/intake/reports/YYYY-MM-DD_incident-{slug}.md
7. Append to VAULT_CHANGELOG.md. Commit with prefix "docs:"
```

## Feature Prompt

```
Read the project vault first (00_HOME → 01_BASELINE → 03_DO_NOT_TOUCH → 05_COMMANDS).

Task: Implement {FEATURE_DESCRIPTION}.

1. Identify affected modules → verify: list of files to change
2. State assumptions and plan (Think Before Coding) → verify: user confirms direction
3. Implement with surgical changes (Simplicity First) → verify: no unrelated edits
4. Run tests / build → verify: all pass
5. 【边做边更新】Update 05_COMMANDS_AND_FILES.md if files changed
6. 【边做边更新】Update 04_ARCHITECTURE.md if structure changed
7. 【边做边更新】Update 01_CURRENT_BASELINE.md
8. Append to VAULT_CHANGELOG.md. Commit with prefix "docs:"
```

## Docs-Only Prompt

```
Read the project vault first (00_HOME → 01_BASELINE).

Task: Update documentation for {AREA}.

Rules:
- Docs-only changes — no code modifications
- Commit with prefix "docs:"
- No deploy needed
- Update vault files if project state has changed
```

## Deploy Prompt

```
Read the project vault first (00_HOME → 01_BASELINE → 06_DEPLOYMENT).

Task: Deploy {VERSION/COMMIT} to {ENVIRONMENT}.

Rules:
- Verify build passes before deploying
- Check 06_DEPLOYMENT.md for the correct process
- Do NOT deploy without explicit user confirmation
- Create deploy report using docs/vault/templates/DEPLOY_REPORT_TEMPLATE.md
- 【边做边更新】Update 01_CURRENT_BASELINE.md after deploy
```

## Vault Sync Prompt

```
Read the project vault.

Task: Sync vault to reflect current project state.

1. Check git log for recent changes
2. Update affected files using change→file mapping (see VAULT_SCHEMA.md)
3. Update metadata (last_updated, confidence)
4. Append to VAULT_CHANGELOG.md
5. Commit with prefix "docs:"
```

## Audit Prompt

```
Read all vault files. Run 10-point checklist from VAULT_SCHEMA.md.

Check orphans, confidence, staleness, cross-references, security rules.
Write full report to assets/intake/reports/YYYY-MM-DD_audit-report.md.
Add summary to 10_REPORT_INDEX.md.
```

## Task Completion (ALWAYS last)

```
Task complete. Final vault check:
1. Verify all vault files were updated DURING work (not batching!)
2. Append entry to VAULT_CHANGELOG.md with session summary
3. Commit vault changes with prefix "docs:"
4. git push
```
