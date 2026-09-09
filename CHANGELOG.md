# Changelog

Notable changes to this project. Dates are commit dates.

> **History note (2026-09-08):** Commit messages in this repository were improved
> via a messages-only history rewrite (`git filter-branch --msg-filter`). The
> original single commit `0605e46` became `d604cae`. File contents, trees,
> authors, and dates are unchanged; only commit messages differ.

## 2016-04-14 — `d604cae` — feat: add RingPlus site watcher with Twilio SMS alerts

Initial (and only functional) commit; scaffolds the entire project.

- `site-checker/monitor_ringplus.py`: polls `https://ringplus.net` every
  `frequency_in_sec` seconds, parses the page with BeautifulSoup, and compares
  the `.content-row` element against the previously seen snapshot; on change it
  sends an SMS through the Twilio REST client.
- `site-checker/example_config.json`: template for the gitignored
  `config.json` holding Twilio credentials, message fields, and poll frequency.
- `Dockerfile`: `python:3-alpine` image that pip-installs
  `twilio`, `requests`, and `beautifulsoup4`, copies `site-checker/`, and runs
  the monitor as the entrypoint.
- `README.md`: Docker build/run instructions.
- `.gitignore`: excludes the real `config.json` so credentials never enter VCS.

## 2026-09-08 — docs pass

Added `CHANGELOG.md`, rewrote `README.md`, added `AGENTS.md`, the
`architectural-diary/`, and `prompt.md` (one-shot recreation prompt). No
application code was changed.
