# AGENTS.md — guide for coding agents working in this repo

## What this is

An archived, single-purpose tool: poll ringplus.net's free-plan section and
send a Twilio SMS on change. One functional commit (`d604cae`, 2016-04-14)
plus a 2026 documentation pass. There are no tests, no CI, no linters, and no
package manifest — dependencies are installed directly in the `Dockerfile`.

## Ground rules

- **Do not run `site-checker/monitor_ringplus.py`.** It makes real HTTP
  requests to an external site and would send real SMS if given credentials.
  Never call RingPlus or Twilio from this repo.
- **Never commit `config.json`.** It holds Twilio credentials and is
  gitignored on purpose; `example_config.json` is the only config that
  belongs in VCS.
- This is effectively read-only archival code. Prefer documentation and
  explanation over "fixing" Python-2-era idioms unless explicitly asked.

## Code notes

- `monitor_ringplus.py` uses the legacy `TwilioRestClient` from the old
  twilio helper library; the modern equivalent is `Client`. Any revival would
  need that upgrade plus pinned dependencies.
- "Comparison" of BeautifulSoup nodes is object/string inequality — good
  enough for a hacky watcher, but prone to false positives if the page
  includes dynamic content inside `.content-row`.
- Config is read from a file next to the script (cwd-relative
  `config.json`), which works because the Dockerfile `ADD`s the whole
  `site-checker/` directory into the image root.

## Repo layout

See `README.md` for the structure table and `architectural-diary/` for the
design rationale (`main.md` plus numbered decision records under
`decisions/`).
