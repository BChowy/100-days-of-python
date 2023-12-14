import os
import requests
from datetime import datetime

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

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
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

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

today_date = datetime.today().strftime('%Y%m%d')

post_pixel_endpoint = f"{graph_endpoint}/{graph_config["id"]}"
pixel_data = {
    "date": today_date,
    "quantity": "5",
}

# response = requests.post(url=post_pixel_endpoint, json=pixel_data, headers=headers)
# print(response.text)

update_pixel_endpoint = f"{post_pixel_endpoint}/{today_date}"
update_pixel_data = {
    "quantity": "9",
}

# response = requests.put(url=update_pixel_endpoint, json=update_pixel_data, headers=headers)
# print(response.text)

delete_pixel_endpoint = f"{post_pixel_endpoint}/{today_date}"
response = requests.delete(url=delete_pixel_endpoint, headers=headers)

print(response.text)
