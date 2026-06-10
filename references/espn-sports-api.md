# ESPN API — Free Sports Data + Betting Odds

> Discovered 2026-06-07. Replaces paid API-Football (free tier doesn't support current season).

## Key Facts

- **Base URL:** `https://site.api.espn.com/apis/site/v2/sports/soccer/fifa.world`
- **Auth:** None needed — completely free, no key, no rate limit
- **Data:** Live scores, match status, DraftKings odds, standings
- **Coverage:** FIFA World Cup (all years), plus other ESPN sports

## Endpoints

### Scoreboard (scores + odds)
```
GET /scoreboard?dates=20260611-20260627&limit=100
```
Returns: events[] with fixture id, date, status, teams, scores, and full DraftKings odds.

### Standings
```
GET /standings
```
Returns: groups with team records (W/D/L, GF/GA, points). Empty before tournament starts.

### Single Day
```
GET /scoreboard?dates=20260611
```

## DraftKings Odds Structure

Each event's `competitions[0].odds[0]` contains:
- `moneyline.home.close.odds` — American odds (e.g., "-225")
- `moneyline.draw.close.odds` — Draw odds (e.g., "+340")
- `moneyline.away.close.odds` — Away odds (e.g., "+700")
- `pointSpread` — Spread with lines
- `total` — Over/under with lines
- `details` — Summary string (e.g., "MEX -225")

## American Odds → Probability

```python
def american_to_prob(odds):
    if odds < 0:
        return round(abs(odds) / (abs(odds) + 100) * 100, 1)
    return round(100 / (odds + 100) * 100, 1)
```

Must normalize: `prob / total * 100` to sum to 100%.

## Match Status States

- `state: "pre"` → STATUS_SCHEDULED
- `state: "in"` → STATUS_LIVE (match in progress)
- `state: "post"` → STATUS_FINISHED

## Pitfalls

1. **API-Football free tier** doesn't support current season (2026). ESPN does.
2. **`details` field** matches American odds format (e.g., "MEX -225") — can be used directly as display string.
3. **Standings endpoint** returns empty before tournament — don't error, just skip.
4. **Match IDs** are consistent across ESPN endpoints (fixture ID = 760415 etc.)
5. **Team abbreviations** may differ from your codes (e.g., ESPN "USA" vs your "USA", ESPN "Türkiye" vs "TUR"). Need a mapping table.

## In-Place TypeScript Update Pattern

For auto-updating `.ts` data files without breaking other exports:

```python
import re
pattern = r"export const PREDICTIONS: MatchPrediction\[\] = \[.*?\];"
updated = re.sub(pattern, new_array, existing_content, flags=re.DOTALL)
```

This replaces ONLY the array, preserving interfaces, functions, and other exports.
