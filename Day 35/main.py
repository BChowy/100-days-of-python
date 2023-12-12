import requests

# the plan has changed, and the api doesn't have a free option anymore.
OWM_endpoint = "https://api.openweathermap.org/data/3.0/onecall"
api_key = "0b244508a847476787d7709bb82d0169"
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
    print("It's gonna rain, bring an ☔")
