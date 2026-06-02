---
type: commands-files
status: active
confidence: high
last_updated: 2026-06-02
owner: agent
reviewed_by: human
---

# Commands and Files

## Commands

### Safe Local

| Command | Purpose | Risk |
|---------|---------|------|
| `npm run dev` | Start dev server (frontend + backend) | 🟢 Safe |
| `npm test` | Run 12 tests | 🟢 Safe |
| `npm run lint` | Check code style | 🟢 Safe |

### Deploy

| Command | Purpose | Risk |
|---------|---------|------|
| `npm run deploy` | Deploy to Vercel + Railway | 🔴 Critical |

## File Inventory

| File | Purpose | Risk |
|------|---------|------|
| `src/server.js` | Express entry point | 🟡 Medium |
| `src/models/todo.js` | CRUD operations | 🟡 Medium |
| `src/db/schema.sql` | Database schema | 🔴 High |
| `src/App.jsx` | React entry point | 🟡 Medium |
| `src/components/*.jsx` | UI components | 🟢 Low |
