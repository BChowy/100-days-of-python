import requests
from twilio.rest import Client

# the plan has changed, and the api doesn't have a free option anymore.
OWM_endpoint = "https://api.openweathermap.org/data/3.0/onecall"
api_key = "0b244508a847476787d7709bb82d0169"
account_sid = "twilio account id"
auth_token = "twilio_auth_token"

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
    client = Client(account_sid, auth_token)
    message = client.messages.create(body="It's gonna rain, bring an ☔",
                                     from_=from_number, to=to_number)

    print(message.status)
