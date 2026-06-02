---

type: report-index
status: active
confidence: medium
last_updated: YYYY-MM-DD
owner: both
reviewed_by: unreviewed
---# 📑 Report Index

> Summary index of all reports for this project.
> **Full reports live in `assets/intake/reports/`** — this file is the quick-access index only.
> This keeps Obsidian Graph View clean (reports don't pollute the main vault graph).

## How Reports Work

```
assets/intake/reports/           ← Full reports live here (not in vault graph)
├── 2026-06-01_setup-report.md
├── 2026-06-15_deploy-report.md
└── 2026-07-01_audit-report.md

docs/vault/10_REPORT_INDEX.md    ← This file: summaries only (in vault graph)
```

**Agent rule:** When generating a report:
1. Write full report to `assets/intake/reports/YYYY-MM-DD_{type}.md`
2. Add a summary row to this index file
3. Link to the full report with a relative path

## Report Index

| Date | Type | Topic | Status | Full Report |
|------|------|-------|--------|-------------|
| {DATE} | Setup | Initial vault creation | Active | [View](../../assets/intake/reports/{DATE}_setup-report.md) |
| {DATE} | Audit | Monthly health check | Active | [View](../../assets/intake/reports/{DATE}_audit-report.md) |
| {DATE} | Deploy | v1.2.3 production deploy | Archived | [View](../../assets/intake/reports/{DATE}_deploy-report.md) |

<!-- Add new reports above this line, newest first -->

## Report Types

| Type | Prefix | When | Where |
|------|--------|------|-------|
| Setup | `*_setup-report.md` | Vault init | `assets/intake/reports/` |
| Audit | `*_audit-report.md` | Monthly / handoff | `assets/intake/reports/` |
| Deploy | `*_deploy-report.md` | After deploy | `assets/intake/reports/` |
| Incident | `*_incident-report.md` | After incident | `assets/intake/reports/` |
| Analysis | `*_analysis-report.md` | Ad-hoc analysis | `assets/intake/reports/` |
