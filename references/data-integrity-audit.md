# Data Integrity Audit Pattern

> How to find and fix fake, random, or misleading data in frontend components.

## Red Flags

| Pattern | Code Sign | Severity |
|---------|-----------|----------|
| **Fake randomness** | `Math.random()`, pseudo-random seed from ID | 🔴 Misleading |
| **Hardcoded "dynamic" data** | `setInterval` fetching static `.json` file | 🟡 Illusion of live |
| **Stale timestamps** | `new Date().toISOString()` written at build time | 🟡 Stale |
| **Placeholder that shipped** | `// TODO: replace with real API` | 🟡 Placeholder |
| **Computed from wrong source** | Upset index from match ID instead of odds | 🔴 Wrong |

## The Audit

1. **Grep for `Math.random`, `Date.now()`, pseudo-random patterns** — these often hide fake "live" indicators
2. **Trace each data field to its source** — if the source is a static `.ts` file, the data can't be live
3. **Check if "auto-update" actually works** — does the pipeline end in a real API, or a static file?
4. **Label each component: static / periodic / real-time** — users deserve to know

## Information Hierarchy Principle

When a page has multiple data cards, order by **user value**, not implementation order:

| Priority | Criterion | Example |
|----------|-----------|---------|
| 🥇 Top | Core value proposition — why users come here | Odds overview (betting site) |
| 🥈 Second | Time-sensitive actionable info | Today's focus matches |
| 🥉 Third | Analytical/secondary | Upset warnings, trends |
| 4️⃣ Bottom | Background/static reference | Team tier rankings |

**Test:** If a user only scrolls 50%, do they see the most important thing? If not, reorder.

## Fix Decision Tree

```
Is the data fake/random?
├── YES → Can you get real data?
│   ├── YES (API available) → Build data pipeline
│   └── NO (no API) → DELETE the component entirely
└── NO → Is it in the right position?
    ├── YES → Keep
    └── NO → Reorder by user value
```

**The rule:** Fake data is worse than no data. Delete first, add back when real data is available.
