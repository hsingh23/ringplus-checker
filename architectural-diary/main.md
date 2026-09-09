# Architectural diary — ringplus-checker

## Overview

The entire system is one loop in one file
(`site-checker/monitor_ringplus.py`, 21 lines) wrapped in a Docker image.
There is no architecture beyond: read config → fetch page → compare a DOM
node → maybe SMS → sleep → repeat.

## Timeline

### 2016-04-14 — `d604cae` — feat: add RingPlus site watcher with Twilio SMS alerts

The only functional commit; it created the whole project:

- The watcher script: baseline snapshot of the first `.content-row` element
  on `https://ringplus.net`, then an infinite poll-compare-alert loop with a
  configurable sleep. BeautifulSoup for parsing, `requests` for HTTP, the
  legacy `TwilioRestClient` for SMS.
- `example_config.json` as a placeholders-only template for the gitignored
  `config.json`.
- `Dockerfile` on `python:3-alpine` with `pip install twilio requests
  beautifulsoup4`, `ADD site-checker .`, and the script as entrypoint —
  intended to run unattended (`docker run -d`).
- A short README with Docker usage.

Key decisions made here are recorded as ADRs:
[001-diff-single-dom-node.md](decisions/001-diff-single-dom-node.md),
[002-docker-alpine-unattended-deployment.md](decisions/002-docker-alpine-unattended-deployment.md),
[003-secrets-in-gitignored-config.md](decisions/003-secrets-in-gitignored-config.md).

### 2026-09-08 — documentation pass

RingPlus had long since ceased operations (2017), so the project was treated
as an archive: commit message of the sole commit improved via a
messages-only rewrite (`0605e46` → `d604cae`, trees unchanged), README
rewritten with what/why and archived framing, and `CHANGELOG.md`,
`AGENTS.md`, this diary, and `prompt.md` added. No application code touched.

## Observations / known limitations

- No error handling: any HTTP failure or Twilio error kills the loop (and
  the container, absent a restart policy).
- Node comparison is BeautifulSoup object inequality; whitespace or dynamic
  content inside `.content-row` triggers false alerts.
- Dependencies unpinned; the twilio API used here (`TwilioRestClient`) no
  longer exists in modern versions of the library.
- The first change after startup is always detected relative to the startup
  snapshot, which is the intended behavior (alert on any change after boot).
