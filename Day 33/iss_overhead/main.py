import requests
from datetime import datetime

# got it from https://www.latlong.net/
ABHA_LONG = 42.499481
ABHA_LAT = 18.217051

response = requests.get(url="http://api.open-notify.org/iss-now.json")
data = response.json()

iss_longitude = data["iss_position"]["longitude"]
iss_latitude = data["iss_position"]["latitude"]
iss_position = (iss_longitude, iss_latitude)

parameters = {
    "lat": ABHA_LAT,
    "long": ABHA_LONG,
    "formatted": 0,  # to get the time in unix format
}
# Require parameters of longitude and latitude
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()  # in case there's a mistake, raise an error
data = response.json()

# split it by "T", take the second part, split it by ":", take the first part which is the hour
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

time_now = datetime.now().hour
print(sunset)

