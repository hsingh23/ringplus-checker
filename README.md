# RingPlus Checker

A small Docker-containerized watcher that polled the RingPlus website
(`https://ringplus.net`) for changes to its free-plan offerings and sent an
SMS via Twilio whenever the plans section changed — so you could grab a new
free plan the moment it appeared.

> **Archived / legacy project.** RingPlus ceased operations in 2017, so the
> service this watches no longer exists. The code is retained for historical
> reference; it is not maintained and would need dependency updates (notably
> the Twilio helper library) to run against a live site today.

## How it worked

1. On startup the script fetches `https://ringplus.net`, selects the first
   `.content-row` element with BeautifulSoup, and stores it as the baseline.
2. Every `frequency_in_sec` seconds it re-fetches the page and compares the
   current `.content-row` against the baseline.
3. If the markup differs, it updates the baseline and sends an SMS through
   Twilio (text configurable in `config.json`), then keeps polling.

## Features

- Change detection scoped to a single DOM node (`.content-row`), ignoring
  unrelated page churn.
- SMS alerts through Twilio with configurable from/to numbers and body text.
- Configurable polling interval.
- Secrets kept out of git via a gitignored `config.json` (see
  `site-checker/example_config.json` for the template).
- Runs unattended as a Docker container.

## Stack

- Python 3 (alpine base image)
- `requests` — HTTP fetching
- `beautifulsoup4` — HTML parsing
- `twilio` (legacy `TwilioRestClient` API) — SMS delivery
- Docker

## Quickstart (as originally designed)

1. Create the config file from the template (values are yours to supply):

   ```
   cp site-checker/example_config.json site-checker/config.json
   ```

   `config.json` keys (names only — never commit real values):
   - `twilio.account`, `twilio.token` — Twilio API credentials
   - `twilio.from`, `twilio.to` — sender and recipient phone numbers
   - `twilio.body` — SMS text
   - `website.frequency_in_sec` — polling interval

2. Build and run the container:

   ```
   docker build -t ringplus-checker .
   docker run -d ringplus-checker
   ```

3. Manage it:

   - Stop (and remove): `docker rm -f ringplus-checker`
   - Check it is running: `docker ps`

To run without Docker: `pip install twilio requests beautifulsoup4`, place
`config.json` next to the script, then `python3 site-checker/monitor_ringplus.py`.

## Repository structure

```
.
├── Dockerfile                     # python:3-alpine image running the monitor
├── README.md
├── site-checker/
│   ├── example_config.json        # config template (placeholders only)
│   ├── config.json                # real config, gitignored, you create it
│   └── monitor_ringplus.py        # poll-and-alert loop
├── AGENTS.md                      # notes for coding agents
├── CHANGELOG.md
├── prompt.md                      # one-shot recreation prompt
└── architectural-diary/           # design notes and decision records
```

## Status

Archived. See `CHANGELOG.md` for the full history (one functional commit,
2016-04-14, plus a 2026 documentation pass) and `architectural-diary/` for the
reasoning behind the design.
