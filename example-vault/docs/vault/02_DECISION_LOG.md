---
type: decision-log
status: active
confidence: high
last_updated: 2026-06-02
owner: both
reviewed_by: human
---

# Decision Log

## Decision: Use SQLite instead of PostgreSQL

**Date:** 2026-06-02 | **Status:** Accepted
**Decision:** Use SQLite for local development and production
**Why:** Single-file database, zero config, perfect for a todo app scale
**Alternatives rejected:**
- PostgreSQL — overkill for a simple todo app
- JSON file — no query capability
**Do not reverse unless:** App needs multi-server deployment

## Decision: React + Vite instead of Next.js

**Date:** 2026-06-02 | **Status:** Accepted
**Decision:** React 18 with Vite bundler
**Why:** Fast dev server, simple setup, no SSR needed for a todo app
**Do not reverse unless:** SEO becomes important
