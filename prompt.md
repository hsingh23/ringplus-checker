# One-shot recreation prompt

Give this prompt (plus nothing else) to a coding agent to recreate this
repository from scratch.

---

Create a minimal Git repository named `ringplus-checker` containing a
website-watcher that sends an SMS when a specific section of a target page
changes. Requirements:

1. `site-checker/monitor_ringplus.py` — a Python script that:
   - reads `config.json` (in the script's working directory) with the shape:
     `{"twilio": {"account", "token", "from", "to", "body"}, "website":
     {"frequency_in_sec"}}`;
   - constructs the legacy Twilio helper client (`TwilioRestClient`) with the
     account/token from config;
   - fetches `https://ringplus.net` with `requests.get`, parses the body with
     BeautifulSoup, and selects the first `.content-row` element as the
     baseline;
   - loops forever: re-fetch and re-select `.content-row`; if it differs from
     the baseline, store the new value and send an SMS via Twilio
     (`messages.create` with `to`, `from_`, `body` from config); then sleep
     `frequency_in_sec` seconds.
2. `site-checker/example_config.json` — the config template with obvious
   placeholder strings for account/token/numbers, body text
   "Ringplus has a new updates", and `frequency_in_sec: 900`.
3. `Dockerfile` — `FROM python:3-alpine`, maintainer label, `pip install
   twilio requests beautifulsoup4`, `ADD site-checker .`, entrypoint
   `python3 monitor_ringplus.py`.
4. `.gitignore` — exactly `config.json`.
5. `README.md` — short usage: copy `example_config.json` to `config.json`
   with real values, `docker build -t SITENAME .`, `docker run -d SITENAME`,
   plus the stop/inspect commands.

Style notes: 2016-era Python, no functions or error handling — top-to-bottom
script with an infinite `while 1:` loop. Do not include any real credentials;
placeholders only. Do not call any external service.

---

Expected result: 5 tracked files, 48 lines total, one initial commit.
