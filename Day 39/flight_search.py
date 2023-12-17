import requests

TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com/locations/query"
TEQUILA_KEY = "wiufCFDZqKp5UQVuGFEssaFr9fAMfSsW"


class FlightSearch:
    def get_city_code(self, city_name):
        headers = {
            "apikey": TEQUILA_KEY,
        }
        parameters = {
            "term": city_name,
            "location_types": "city",
        }
        response = requests.get(url=TEQUILA_ENDPOINT, headers=headers, params=parameters)
        code = response.json()["locations"][0]["code"]
        return code
