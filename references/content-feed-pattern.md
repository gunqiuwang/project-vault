# Content Feed Pipeline Pattern

> Reusable pattern for any project with a news/content RSS feed that needs auto-updating.

## The Problem

Content feeds accumulate forever, mix relevant and irrelevant items, and go stale.

## The Pattern: Filter → Merge → Prune → Cap

```python
def merge_and_prune(old_articles, new_articles, max_age_hours, max_count):
    cutoff = datetime.now(timezone.utc) - timedelta(hours=max_age_hours)

    # 1. Merge: new first, old second
    combined = new_articles + old_articles

    # 2. Deduplicate by title prefix (first 30 chars)
    seen = set()
    unique = []
    for a in combined:
        key = a["title"][:30]
        if key in seen: continue
        seen.add(key)

        # 3. Prune: drop articles older than cutoff
        dt = parse_iso(a.get("time_iso", ""))
        if dt and dt < cutoff:
            continue

        unique.append(a)

    # 4. Cap: keep only top N
    return unique[:max_count]
```

## Three Levels of Filtering

| Level | What | Example |
|-------|------|---------|
| **Keyword match** | Title must contain core terms | "世界杯" OR "2026" OR "FIFA" |
| **Negative filter** | Exclude by category | Not club football, not transfer news |
| **Relevance gate** | Team name alone is NOT enough | "巴西" without "世界杯" = skip |

**Pitfall:** Starting with loose filters (any mention of a team name) leads to 300+ irrelevant articles. Start strict, loosen only if too few results.

## Rolling Window

- **48h window** for news (content goes stale fast)
- Store `time_iso` (ISO 8601) as the canonical timestamp, derive display `time` ("3小时前") on read
- Old articles auto-expire on each fetch cycle

## Cap

- **30 articles max** for a mobile feed (one screen of scrolling)
- More than 30 → users stop reading anyway

## Auto-Update Pipeline

```
GitHub Action (cron every 2h)
    → Python script fetches RSS/web sources
    → Strict filter (core keywords required)
    → Merge with existing news.json
    → Prune old (>48h)
    → Cap at 30
    → Write public/news.json
    → git commit + push
    → Frontend fetches /news.json every 10min
```

## Implementation Checklist

- [ ] `time_iso` field on every article (canonical time)
- [ ] Merge logic loads existing JSON before writing
- [ ] Dedup by title prefix, not full title (minor wording changes)
- [ ] Rolling window uses `time_iso`, not display `time`
- [ ] GitHub Action workflow in `.github/workflows/`
- [ ] Frontend has manual refresh button + auto-refresh interval
- [ ] Fallback/mock data for when fetch fails
