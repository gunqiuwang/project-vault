---
type: schema
status: active
confidence: high
last_updated: YYYY-MM-DD
owner: human
reviewed_by: human
---

# 📐 Vault Schema

> This file defines the rules, conventions, and thresholds for this project's vault.
> Only humans should modify this file. Agents can suggest changes but not override.

## Project Identity

**Project:** {PROJECT_NAME}
**Description:** {ONE_PARAGRAPH_DESCRIPTION}

## Vault Version

```yaml
vault_version: 4.1.0
vault_created: YYYY-MM-DD
last_upgraded: YYYY-MM-DD
```

## Project Phase

```yaml
project_phase: growth  # idea | prototype | mvp | growth | maintenance | sunset
```

| Phase | Required Files | Optional |
|-------|---------------|----------|
| **idea** | 00_HOME, 04_ARCHITECTURE, VAULT_SCHEMA, VAULT_CHANGELOG | All others |
| **prototype** | + 01_BASELINE, 05_COMMANDS | 06-08 |
| **mvp** | + 03_DO_NOT_TOUCH, 06_DEPLOY, 07_TESTING | 08_INCIDENTS |
| **growth** | All 13 files | None |
| **maintenance** | All 13 files | None (focus on 02 + 08) |
| **sunset** | 00_HOME, 03_DO_NOT_TOUCH | Rest archived |

## Staleness Thresholds

```yaml
staleness_threshold_days: 30     # how old before a file is "stale"
review_threshold_days: 14        # how long before unreviewed content needs attention
audit_interval_days: 30          # how often to run vault audit
```

Adjust based on project activity:
- Active development: 30 days
- Maintenance mode: 90 days
- Frozen/sunset: 365 days

## Multi-Agent Write Protocol

### File Ownership

| File | Primary Writer | Rule |
|------|---------------|------|
| `00_HOME.md` | Human | Agent can suggest |
| `01_CURRENT_BASELINE.md` | Last committer | Read before write |
| `02_DECISION_LOG.md` | Human decides, Agent records | Append only |
| `03_DO_NOT_TOUCH.md` | Human | Agent can suggest, not override |
| `04_ARCHITECTURE.md` | Agent | Human reviews |
| `05_COMMANDS_AND_FILES.md` | Agent | Auto-generated |
| `VAULT_SCHEMA.md` | Human | Agent cannot modify |
| `VAULT_CHANGELOG.md` | Any | Append only |

### Conflict Rules

1. **Append-only files:** No conflicts — always append at end
2. **State files (01, 05):** Last writer wins — read current state first
3. **Rule files (03, SCHEMA):** Human has veto
4. **Git merge conflict:** Agent MUST stop, ask human to resolve

## Tag Taxonomy

**Technical:** `architecture`, `database`, `api`, `frontend`, `backend`, `infrastructure`, `security`
**Process:** `deployment`, `testing`, `documentation`, `refactoring`
**Meta:** `urgent`, `blocked`, `deprecated`

## Page Thresholds

| Action | Condition |
|--------|-----------|
| **Create** | New decision/incident/command/danger area discovered |
| **Update** | Related code changed, or `last_updated` is stale |
| **Split** | Any file exceeds ~300 lines |
| **Archive** | Decision superseded, feature removed, incident resolved |

## Vault Score Formula

```
vault_score = confidence_score * 0.35
            + freshness_score * 0.30
            + completeness_score * 0.20
            + review_score * 0.15

confidence_score  = high_confidence_files / total_files * 100
freshness_score   = files_within_threshold / total_files * 100
completeness_score = existing_files / phase_required_files * 100
review_score      = human_reviewed_files / total_files * 100
```

| Score | Grade | Action |
|-------|-------|--------|
| 90-100 | 🟢 Excellent | Maintain |
| 70-89 | 🟡 Good | Review low-confidence items |
| 50-69 | 🟠 Needs work | Run vault sync |
| 0-49 | 🔴 Critical | Run vault audit, fix issues |

## Orphan Detection Rules

An orphan is:
- A `[[wikilink]]` pointing to a file that doesn't exist
- A vault file with zero inbound links from other vault files
- A `03_DO_NOT_TOUCH.md` entry referencing a deleted file
- A section with only placeholder text and `confidence: low`

## Security Rules

Vault files MUST NOT contain:
- API keys, tokens, passwords, secrets
- Internal URLs (non-public)
- Database connection strings
- Private IP addresses or ports
- Personal data without explicit approval

During `vault init`, agent scans `.env.example` and `.gitignore` to auto-populate `03_DO_NOT_TOUCH.md` with security rules.

## Audit Checklist

```
1.  Existence     — phase-required files exist?
2.  Baseline      — HEAD matches git log -1?
3.  Orphan links  — [[wikilinks]] to missing files?
4.  Orphan files  — files with zero inbound links?
5.  Confidence    — low that should be high?
6.  Review        — unreviewed older than threshold?
7.  Staleness     — last_updated older than threshold?
8.  Commands      — matches package.json?
9.  DO_NOT_TOUCH  — referenced files exist? Security rules current?
10. Cross-ref     — every file has ≥1 inbound link?
```
