import os
import requests

nutritionix_APP_ID = os.getenv("nutritionix_APP_ID")
nutritionix_APP_KEY = os.getenv("nutritionix_APP_KEY")

exersice_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": nutritionix_APP_ID,
    "x-app-key": nutritionix_APP_KEY,
}

parameters = {
    "query": input("What exersice did you do? "),
}

response = requests.post(url=exersice_endpoint, headers=headers, json=parameters)
response.raise_for_status()

print(response.json())