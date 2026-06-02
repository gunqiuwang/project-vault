---

type: testing
status: active
confidence: medium
last_updated: YYYY-MM-DD
owner: both
reviewed_by: unreviewed
---# 🧪 Testing & Verification

> How to verify the project works. Run these before and after any change.

## Quick Verification

```bash
# Build check
{BUILD_COMMAND}

# Test suite
{TEST_COMMAND}

# Lint
{LINT_COMMAND}

# Type check
{TYPECHECK_COMMAND}
```

## Test Commands

| Command | Purpose | Time | Coverage |
|---------|---------|------|----------|
| `{TEST_CMD}` | {PURPOSE} | ~{DURATION} | {COVERAGE} |

## Manual QA Checklist

> Run through this checklist for any significant change.

- [ ] {CHECK_1}
- [ ] {CHECK_2}
- [ ] {CHECK_3}
- [ ] No console errors
- [ ] No broken links
- [ ] Mobile responsive (if applicable)

## Critical User Flows

| Flow | Steps | Expected Result |
|------|-------|-----------------|
| {FLOW_1} | {STEPS} | {RESULT} |
| {FLOW_2} | {STEPS} | {RESULT} |

## Routes to Verify

| Route | Method | Expected | Auth Required |
|-------|--------|----------|--------------|
| `/` | GET | 200 | No |
| `/api/health` | GET | 200 | No |
| `{ROUTE}` | {METHOD} | {EXPECTED} | {YES/NO} |

## Regression Checks

> After changes, verify these still work:

- [ ] {REGRESSION_1}
- [ ] {REGRESSION_2}

## Forbidden Wording Checks

> If the project has branding/content rules, check here.

```bash
# Example: check for forbidden terms
grep -r "{FORBIDDEN_TERM}" src/ && echo "FAIL: forbidden term found" || echo "PASS"
```
