import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
import os


# the plan has changed, and the api doesn't have a free option anymore.
OWM_endpoint = "https://api.openweathermap.org/data/3.0/onecall"
api_key = os.environ.get("OWM_API_KEY")
account_sid = "twilio account id"
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

from_number = "twilio acc phone number"
to_number = "receiver phone number"  # it should be added to the twilio account

parameters = {
    "lat": 44.34,
    "lon": 10.99,
    "appid": api_key,
    "exclude": "current,minutely,daily"  # no spaces
}

response = requests.get(OWM_endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages.create(body="It's gonna rain, bring an ☔",
                                     from_=from_number, to=to_number)

    print(message.status)
