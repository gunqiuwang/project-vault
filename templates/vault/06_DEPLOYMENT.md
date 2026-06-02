---

type: deployment
status: active
confidence: medium
last_updated: YYYY-MM-DD
owner: both
reviewed_by: unreviewed
---# 🚀 Deployment

> How to build, deploy, and rollback. If you don't know, write "Unknown".

## Build

```bash
{BUILD_COMMAND}
```

**Build output:** {OUTPUT_DIR_OR_ARTIFACT}
**Build time:** ~{DURATION}

## Deploy

```bash
{DEPLOY_COMMAND}
```

**Environment:** {PRODUCTION_URL}
**Deploy time:** ~{DURATION}

## Environment Requirements

| Requirement | Version | Notes |
|------------|---------|-------|
| Node.js | {VERSION} | {NOTES} |
| Python | {VERSION} | {NOTES} |
| {OTHER} | {VERSION} | {NOTES} |

## Environment Variables

| Variable | Required | Description | Where to Get It |
|----------|----------|-------------|-----------------|
| `{VAR}` | Yes | {DESCRIPTION} | {SOURCE} |

## Health Check

```bash
{HEALTH_CHECK_COMMAND}
```

**Expected:** {EXPECTED_RESPONSE}

## Route Verification

| Route | Expected Status | Expected Content |
|-------|----------------|-----------------|
| `/` | 200 | {CONTENT} |
| `/api/health` | 200 | `{"status": "ok"}` |

## Rollback Strategy

```bash
{ROLLBACK_COMMAND}
```

**Rollback time:** ~{DURATION}
**Rollback verification:** {HOW_TO_VERIFY}

## Cache Purge

```bash
{CACHE_PURGE_COMMAND}
```

## Tagging Convention

```
v{MAJOR}.{MINOR}.{PATCH}
```

Example: `v1.2.3`

## Docs-Only Commits

Prefix with `docs:` — no deploy needed.

```
docs: update vault after API refactor
```
