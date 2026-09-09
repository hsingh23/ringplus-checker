# ADR 001 — Detect changes by diffing a single DOM node

- Date: 2016-04-14
- Status: accepted (historical)

## Context

The watcher needs to know when RingPlus's free-plan offerings change. A
whole-page comparison is noisy: the homepage also contains ads, session
tokens, timestamps, and other dynamic markup that would fire constant false
positions.

## Decision

Fetch the page, parse it with BeautifulSoup, and compare only the first
element matching the `.content-row` selector — the region that lists plan
content. Keep the last-seen value as the baseline; on inequality, update the
baseline and send one SMS.

## Consequences

- Simple and effective for the target site as it existed in 2016: unrelated
  page churn is ignored.
- The selector is brittle; any redesign of ringplus.net would break
  detection silently (`select_one` returning `None`).
- "Comparison" is BeautifulSoup object inequality rather than a normalized
  text/hash diff, so insignificant whitespace changes inside the node could
  in principle trigger a false alert.
