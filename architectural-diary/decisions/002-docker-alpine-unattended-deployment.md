# ADR 002 — Ship as an unattended python:3-alpine Docker container

- Date: 2016-04-14
- Status: accepted (historical)

## Context

The watcher must run continuously for days or weeks (free plans appeared
sporadically), on whatever machine the author had, without a process manager
or service setup.

## Decision

Package the script in a `python:3-alpine` image: `pip install twilio
requests beautifulsoup4`, `ADD site-checker .`, and run
`monitor_ringplus.py` as the entrypoint. Deploy with `docker run -d`;
including `config.json` inside `site-checker/` at build time bakes the
configuration into the image.

## Consequences

- Tiny image, trivial deployment, restarts possible via Docker's restart
  policies (though none was configured).
- Config baked into the image means credential rotation requires a rebuild;
  mounting the config as a volume would have been cleaner.
- Unpinned dependencies make the build unreproducible across time.
