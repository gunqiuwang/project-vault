# Free Sports Data APIs — Pitfalls & Alternatives

## API-Football (api-sports.io)

- **Free plan**: Does NOT support future seasons (e.g., 2026). Error: "Free plans do not have access to this season, try from 2022 to 2024."
- **Paid plan required** for upcoming/current tournaments.
- Key format: `x-apisports-key: <key>`

## ESPN Public API (recommended for free)

- **Free, unlimited, no key required**
- Base URL: `https://site.api.espn.com/apis/site/v2/sports/soccer/fifa.world`
- Endpoints:
  - `/scoreboard?dates=YYYYMMDD-YYYYMMDD&limit=100` — match scores + status
  - `/standings` — group standings (available once tournament starts)
- Match IDs match API-Football IDs (e.g., `760415` = Mexico vs South Africa)
- Status states: `pre` (scheduled), `in` (live), `post` (finished)
- Returns: scores, elapsed time, venue, team names, abbreviations
- **Limitation**: English team names only — need a mapping dict for Chinese

## Other Free Sources

- **football-data.org**: Free tier available, but WC 2026 endpoint returns 403
- **OpenLigaDB**: Free, mainly German football
- **RSS feeds** (ESPN, BBC): Good for news, not live scores

## Recommended Stack for Free Sports Apps

```
Live scores: ESPN API (free, unlimited)
News:        ESPN RSS + BBC RSS via rss2json.com
Odds:        The Odds API (free 500/month — tight for 96 matches)
```

## Pitfall: API-Football Season Restriction

If you register for API-Football thinking the free plan covers the current World Cup, it won't. The free tier is limited to seasons 2022-2024. Always test with a date-range query before building a pipeline around it.
