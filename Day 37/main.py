import os
import requests

TOKEN = os.getenv("PIXELA_TOKEN")
USERNAME = "bchowy"

pixela_endpoint = "https://pixe.la/v1/users"
parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

response = requests.post(url=pixela_endpoint, json=parameters)
print(response.text)


