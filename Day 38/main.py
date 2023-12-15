import os
from datetime import datetime
import requests

nutritionix_APP_ID = os.getenv("nutritionix_APP_ID")
nutritionix_APP_KEY = os.getenv("nutritionix_APP_KEY")

exersice_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/bce0e9cffafb92f8c306cf27c93f3821/myWorkouts/workouts"

headers = {
    "x-app-id": nutritionix_APP_ID,
    "x-app-key": nutritionix_APP_KEY,
}

parameters = {
    "query": input("What exercises did you do today?"),
}

response = requests.post(url=exersice_endpoint, headers=headers, json=parameters)
response.raise_for_status()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")


for exercise in response.json()["exercises"]:
    sheety_row = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }
    add_row = requests.post(url=sheety_endpoint, json=sheety_row)
    add_row.raise_for_status()
    print(add_row.text)
