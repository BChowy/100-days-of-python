import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
data = response.json()

iss_longitude = data["iss_position"]["longitude"]
iss_latitude = data["iss_position"]["latitude"]
iss_position = (iss_longitude, iss_latitude)
