from requests import get
from bs4 import BeautifulSoup
from twilio.rest import TwilioRestClient
from time import sleep
import json

json_data=open("config.json").read()
config = json.loads(json_data)
twilio_config = config["twilio"]
twilio_client = TwilioRestClient(twilio_config["account"], twilio_config["token"])
website = config["website"]
ringplus = "https://ringplus.net"

initial = BeautifulSoup(get(ringplus).text).select_one(".content-row")
while 1:
	current = BeautifulSoup(get(ringplus).text).select_one(".content-row")
	if (current != initial):
		initial = current
		twilio_client.messages.create(to=twilio_config["to"], from_=twilio_config["from"],
                                 body=twilio_config["body"])
	sleep(website["frequency_in_sec"])