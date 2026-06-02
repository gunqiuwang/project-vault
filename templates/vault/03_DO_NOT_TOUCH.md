---
type: danger-zones
status: active
confidence: high
last_updated: YYYY-MM-DD
owner: human
reviewed_by: human
---

# 🚫 DO NOT TOUCH — Danger Zones

> This file lists things that will break if you change them casually. Read this before editing ANYTHING.
> **This file can only be modified by humans.** Agents can suggest additions but cannot remove entries.

## Files That Must NOT Be Changed

| File | Why | Who Can Change It |
|------|-----|-------------------|
| `{FILE_1}` | {REASON} | {APPROVER} |
| `{FILE_2}` | {REASON} | {APPROVER} |

## Business Logic — Hands Off

| System | Rule | Exception |
|--------|------|-----------|
| {SYSTEM_1} | {WHAT_NOT_TO_DO} | {WHEN_IT_IS_OK} |

## Database & Migrations

| Rule | Details |
|------|---------|
| No schema changes | Without explicit approval + migration plan |
| No data deletion | Without explicit approval + backup |

## Deployment Restrictions

| Rule | Details |
|------|---------|
| No auto-deploy | Always confirm with user first |
| No deploy on Fridays | Unless explicitly approved |

## 🔒 Security Rules

> Auto-populated during `vault init` from `.env.example` and `.gitignore` analysis.
> Agents MUST NOT put these in vault files.

**Never include in any vault file:**
- API keys, tokens, passwords, or secrets
- Database connection strings
- Internal URLs (non-public)
- Private IP addresses or ports
- Contents of `.env` files
- Personal data (emails, phone numbers) without explicit approval

**Sensitive patterns detected in project:**

| Pattern | Source | Rule |
|---------|--------|------|
| `{PATTERN_1}` | `.env.example` | Never include in vault |
| `{PATTERN_2}` | `.gitignore` | Never include in vault |

## Known Fragile Systems

| System | What Breaks | How to Avoid |
|--------|-------------|--------------|
| {SYSTEM_1} | {WHAT_BREAKS} | {PREVENTION} |

## Commands Requiring Explicit User Approval

| Command | Why It's Dangerous |
|---------|-------------------|
| `rm -rf` | Deletes files permanently |
| `DROP TABLE` | Destroys data |
| `git push --force` | Overwrites history |
| `{DEPLOY_CMD}` | Pushes to production |

## ⚠️ Golden Rule

> If you're not sure whether you should touch something — **DON'T.**
> Ask the user first. It's always safer to ask than to fix a broken production.
