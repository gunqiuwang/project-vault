---

type: baseline
status: active
confidence: high
last_updated: YYYY-MM-DD
owner: agent
reviewed_by: unreviewed
---# 📊 Current Baseline — Source of Truth

> This file is the project's source of truth. Update it after every significant change.
> **Agent rule: Every task MUST update this file if branch/commit/status changed.**

## Current State

| Key | Value | Confidence |
|-----|-------|------------|
| **Current Branch** | {BRANCH} | high |
| **HEAD Commit** | `{COMMIT_SHA}` — {COMMIT_MESSAGE} | high |
| **Latest Stable Tag** | {TAG or "None"} | high |
| **Production Commit** | `{COMMIT_SHA}` or "Not deployed" | medium |
| **Build Status** | {Passing / Failing / Unknown} | high |
| **Test Status** | {Passing / Failing / Unknown} | high |
| **Deploy Status** | {Live / Staging / Not deployed} | medium |
| **Last Updated** | {DATE} | — |

## Main Product Capabilities

1. {CAPABILITY_1}
2. {CAPABILITY_2}
3. {CAPABILITY_3}

## Current Known Issues

| Issue | Severity | Status | Confidence | Notes |
|-------|----------|--------|------------|-------|
| {ISSUE_1} | {HIGH/MED/LOW} | {Open/Fixed} | high/medium/low | {NOTES} |

## Recently Completed Work

| Date | What | Commit | Confidence |
|------|------|--------|------------|
| {DATE} | {DESCRIPTION} | `{SHA}` | high |

## Things That Must NOT Be Regressed

> If any of these break, it's a critical incident.
> Confidence MUST be `high` for all entries here.

- {CRITICAL_FEATURE_1}
- {CRITICAL_FEATURE_2}
- {CRITICAL_FEATURE_3}

## Verification Command

```bash
{VERIFICATION_COMMAND}
```
