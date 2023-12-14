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

# response = requests.post(url=pixela_endpoint, json=parameters)
# print(response.text)

graph_endpoint = "https://pixe.la/v1/users/bchowy/graphs"
graph_config = {
    "id": "testgraph",
    "name": "Coding Graph",
    "unit": "commit",
    "type": "int",
    "color": "kuro",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)
