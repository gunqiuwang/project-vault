---
type: home
status: active
confidence: medium
last_updated: YYYY-MM-DD
owner: both
reviewed_by: unreviewed
aliases: ["{PROJECT_NAME}", "{PROJECT_NAME} Home", "{PROJECT_SLUG}"]
---

## 🔴 VAULT STARTUP SYNC (第一步，读任何文件之前)

**vault 可能已过期。先检查，再开工：**

```
1. 读本文件的 last_updated（上方 frontmatter）
2. cd 到项目根目录
3. git log --oneline --since=<last_updated> | grep -v "chore: update news" | grep -v "docs:"
4. 如果有未同步的 commit → 先跑 vault sync（见 09_AGENT_PROMPTS.md），再开始干活
```

**如果 vault 是最新的 → 正常开工，继续读下方 Mandatory reading order。**

# 🏠 {PROJECT_NAME} — Project Vault
> {ONE_LINE_DESCRIPTION}

## Quick Facts

| Key | Value |
|-----|-------|
| **Project** | {PROJECT_NAME} |
| **Stable Branch** | {BRANCH} |
| **HEAD Commit** | `{COMMIT_SHA}` |
| **Production Status** | {STATUS} |
| **Vault Schema** | [[VAULT_SCHEMA]] v1.0.0 |
| **Last Updated** | {DATE} |

## Most Important Files

| File | Why It Matters | Confidence |
|------|---------------|------------|
| `{FILE_1}` | {REASON} | high/medium/low |
| `{FILE_2}` | {REASON} | high/medium/low |
| `{FILE_3}` | {REASON} | high/medium/low |

## Most Important Commands

| Command | Purpose | Risk |
|---------|---------|------|
| `{COMMAND_1}` | {PURPOSE} | 🟢/🟡/🟠/🔴 |
| `{COMMAND_2}` | {PURPOSE} | 🟢/🟡/🟠/🔴 |

## 🔴 Agent Entry Page

> **Every new Agent MUST read this page first.**
> This is the project's central hub. All knowledge flows through here.

**Mandatory reading order:**

1. [[00_HOME]] — You are here
2. [[01_CURRENT_BASELINE]] — Source of truth for project state
3. [[03_DO_NOT_TOUCH]] — Things that will break if you touch them
4. [[05_COMMANDS_AND_FILES]] — What you can and cannot run
5. [[VAULT_SCHEMA]] — Rules for maintaining this vault
6. Task-specific vault note (e.g., [[04_ARCHITECTURE]] for refactors)

**Rules:**
- Do not implement product features without reading the vault first
- Do not change business logic without explicit approval
- Do not deploy unless explicitly asked
- Do not run destructive commands
- Summarize your plan before editing

**After completing any task, you MUST:**
- Update [[01_CURRENT_BASELINE]] if branch/commit/status changed
- Append to [[10_REPORT_INDEX]] if a report was generated
- Append to [[VAULT_CHANGELOG]]

## Current Known Risks

| Risk | Severity | Confidence | Mitigation |
|------|----------|------------|------------|
| {RISK_1} | {HIGH/MED/LOW} | high/medium/low | {MITIGATION} |

## Next Recommended Action

{NEXT_ACTION}

## Vault Navigation

- [[01_CURRENT_BASELINE]] — Where we are now
- [[02_DECISION_LOG]] — Why we made key choices
- [[03_DO_NOT_TOUCH]] — Danger zones
- [[04_ARCHITECTURE]] — How it all fits together
- [[05_COMMANDS_AND_FILES]] — What you can run and touch
- [[06_DEPLOYMENT]] — How to ship it
- [[07_TESTING_AND_VERIFICATION]] — How to verify it works
- [[08_INCIDENTS_AND_FIXES]] — What broke and how we fixed it
- [[09_AGENT_PROMPTS]] — Reusable prompts for common tasks
- [[10_REPORT_INDEX]] — All reports at a glance
- [[VAULT_SCHEMA]] — Vault rules and conventions
- [[VAULT_CHANGELOG]] — Vault operation log
