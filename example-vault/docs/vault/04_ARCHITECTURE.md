---
type: architecture
status: active
confidence: high
last_updated: 2026-06-02
owner: agent
reviewed_by: human
---

# Architecture

## Tech Stack

| Layer | Technology |
|-------|-----------|
| **Frontend** | React 18 + Vite |
| **Backend** | Express.js |
| **Database** | SQLite (better-sqlite3) |
| **Tests** | Vitest |
| **Deploy** | Vercel (frontend) + Railway (backend) |

## Data Flow

```
User → React UI → fetch API → Express → SQLite
```

## Main Structure

```
src/
├── components/
│   ├── TodoList.jsx      # Main list component
│   ├── TodoItem.jsx      # Single item
│   ├── AddTodo.jsx       # Input form
│   └── Filter.jsx        # Status filter
├── db/
│   └── schema.sql        # Database schema (DO NOT TOUCH)
├── models/
│   └── todo.js           # CRUD operations
├── server.js             # Express entry point
└── App.jsx               # React entry point
```
