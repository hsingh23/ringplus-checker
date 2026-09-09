# ADR 003 — Keep secrets in a gitignored config.json

- Date: 2016-04-14
- Status: accepted (historical)

## Context

The script needs Twilio account credentials, phone numbers, and a polling
interval. The project lives in a public GitHub repository, so real
credentials must never be committed.

## Decision

Read all configuration at startup from `config.json` next to the script.
Commit a placeholders-only template (`site-checker/example_config.json`) and
exclude the real file via `.gitignore` (`config.json`).

## Consequences

- No secrets in version control; the template doubles as documentation of
  the config schema (`twilio.account`, `twilio.token`, `twilio.from`,
  `twilio.to`, `twilio.body`, `website.frequency_in_sec`).
- The runtime fails immediately if `config.json` is missing — deployment
  requires a manual copy-from-template step (documented in the README).
- No env-var support, so the same limitation as ADR 002 applies: config
  changes mean rebuilding the image.
