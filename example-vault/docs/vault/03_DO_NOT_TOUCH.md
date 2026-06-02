---
type: danger-zones
status: active
confidence: high
last_updated: 2026-06-02
owner: human
reviewed_by: human
---

# DO NOT TOUCH

## Files That Must NOT Be Changed

| File | Why | Who |
|------|-----|-----|
| `src/db/schema.sql` | Database schema — any change needs migration | Human |
| `src/models/todo.js` | Core CRUD logic — tested and stable | Agent (with tests) |

## Business Logic — Hands Off

| System | Rule |
|--------|------|
| Todo status | Only 3 states: active, completed, deleted |
| ID format | UUID v4 — do not change to auto-increment |
| Date format | ISO 8601 — do not change to locale string |

## Security Rules

- No API keys in vault
- No database credentials in vault
