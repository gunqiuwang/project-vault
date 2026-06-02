# Source Documentation Pattern

## Problem

Six months after a project starts, someone asks "why did we choose X over Y?" The answer was in a chat log, meeting note, or planning doc — but nobody can find it.

## Solution

Link original planning documents in `04_ARCHITECTURE.md` under a "Source Documentation" section:

```markdown
## Source Documentation

> Links to original planning docs, design docs, or discussions that informed this project.

- [[项目构想.md]] — original planning document
- [[PRD]] — product requirements
- [[design-spec]] — design specifications
```

### What to Link

| Source Type | Example |
|-------------|---------|
| Planning doc | `项目构想.md`, `README.md` |
| Design spec | Figma link, style guide |
| Decision chat | "We chose X because..." screenshot or transcript |
| Architecture doc | System design, data flow diagram |
| Meeting notes | Key decisions from kickoff meeting |

### Why This Matters

- Code shows **what** was built
- Git log shows **when** it changed
- Source docs show **why** it was built that way

The "why" is the most valuable and most easily lost information.

### Where to Put It

In the vault template `04_ARCHITECTURE.md`, there's a `## Source Documentation` section.
The `00_HOME.md` template also has a `## Source Documentation` section for quick access.

### Obsidian Benefit

If the source doc is also in the Obsidian vault (e.g., `[[项目构想.md]]`), it becomes a clickable link in Graph View. The planning doc and the vault are visually connected.
