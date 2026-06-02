---

type: agent-prompts
status: active
confidence: high
last_updated: YYYY-MM-DD
owner: both
reviewed_by: unreviewed
---# 🤖 Agent Prompts

> Reusable prompts for common tasks. Copy-paste or reference these when starting a task.

## New Task Startup (ALWAYS use this first)

```
Read docs/vault/00_HOME.md, docs/vault/01_CURRENT_BASELINE.md,
docs/vault/03_DO_NOT_TOUCH.md, and docs/vault/05_COMMANDS_AND_FILES.md
before making changes.

Then read the task-specific vault note.

Do not change unrelated systems.
Do not deploy unless explicitly asked.
Summarize your plan before editing.
```

## Bugfix Prompt

```
Read the project vault first (00_HOME → 01_BASELINE → 03_DO_NOT_TOUCH → 05_COMMANDS).

Task: Fix {BUG_DESCRIPTION}.

Rules:
- Identify the bug before proposing a fix
- Do not refactor unrelated code
- Do not change more than necessary
- Run tests after fix
- Document in docs/vault/08_INCIDENTS_AND_FIXES.md
```

## Feature Prompt

```
Read the project vault first (00_HOME → 01_BASELINE → 03_DO_NOT_TOUCH → 05_COMMANDS).

Task: Implement {FEATURE_DESCRIPTION}.

Rules:
- Identify affected modules before coding
- Do not touch files listed in 03_DO_NOT_TOUCH.md without approval
- Run tests after implementation
- Update 01_CURRENT_BASELINE.md if capabilities change
- Update 04_ARCHITECTURE.md if structure changes
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
- Update 01_CURRENT_BASELINE.md after deploy
```

## Audit Prompt

```
Read the entire project vault.

Task: Audit the project for {AUDIT_FOCUS}.

Rules:
- Read-only — do not modify any files
- Report findings in a new report file
- Check 03_DO_NOT_TOUCH.md for known issues
- Check 08_INCIDENTS_AND_FIXES.md for patterns
- Update 10_REPORT_INDEX.md with your report
```

## Vault Update Prompt

```
Read the project vault.

Task: Update the vault to reflect current project state.

Rules:
- Inspect git log, branch, tags
- Update 01_CURRENT_BASELINE.md with current state
- Update 05_COMMANDS_AND_FILES.md if commands changed
- Update 04_ARCHITECTURE.md if structure changed
- Do not modify code files
- Commit with prefix "docs:"
```
