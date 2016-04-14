FROM python:3-alpine
MAINTAINER hsingh23@illinois.edu
RUN pip install twilio requests beautifulsoup4
ADD site-checker .
ENTRYPOINT python3 monitor_ringplus.py
