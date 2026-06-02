# Deploy Report

**Date:** {DATE}
**Commit:** `{COMMIT_SHA}` — {COMMIT_MESSAGE}
**Tag:** {TAG or "None"}
**Environment:** {Production / Staging}

## Build

| Check | Status | Notes |
|-------|--------|-------|
| Build | ✅/❌ | {NOTES} |
| Tests | ✅/❌ | {NOTES} |
| Lint | ✅/❌ | {NOTES} |
| Type check | ✅/❌ | {NOTES} |

## Deploy

| Step | Status | Duration | Notes |
|------|--------|----------|-------|
| Build artifact | ✅/❌ | {TIME} | {NOTES} |
| Upload/deploy | ✅/❌ | {TIME} | {NOTES} |
| Health check | ✅/❌ | {TIME} | {NOTES} |

## Routes Checked

| Route | Status | Response Time | Notes |
|-------|--------|--------------|-------|
| `/` | ✅/❌ | {TIME} | {NOTES} |
| `/api/health` | ✅/❌ | {TIME} | {NOTES} |

## Issues Found

| Issue | Severity | Resolved | Notes |
|-------|----------|----------|-------|
| {ISSUE} | {LEVEL} | Yes/No | {NOTES} |

## Rollback Plan

```bash
{ROLLBACK_COMMAND}
```

**Rollback verified:** Yes/No

## Final Verdict

**Deploy:** ✅ SUCCESS / ❌ FAIL / ⚠️ PARTIAL

**Notes:** {ADDITIONAL_NOTES}
