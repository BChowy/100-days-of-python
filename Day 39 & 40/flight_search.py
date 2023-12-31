import requests
import pprint
from flight_data import FlightData


TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com"
TEQUILA_KEY = "YOUR API KEY"


class FlightSearch:
    def __init__(self):
        self.headers = {
            "apikey": TEQUILA_KEY,
        }

    def get_city_code(self, city_name):
        parameters = {
            "term": city_name,
            "location_types": "city",
        }
        response = requests.get(url=f"{TEQUILA_ENDPOINT}/locations/query", headers=self.headers, params=parameters)
        code = response.json()["locations"][0]["code"]
        return code

    def check_flights(self, departure_city_code, destination_city_code, date_from, date_to):
        parameters = {
            "fly_from": departure_city_code,
            "fly_to": destination_city_code,
            "date_from": date_from.strftime("%d/%m/%Y"),
            "date_to": date_to.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP",
        }

        response = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search", headers=self.headers, params=parameters)
        try:
            data = response.json()["data"][0]
        except IndexError:
            parameters["max_stopovers"] = 2
            response = requests.get(
                url=f"{TEQUILA_ENDPOINT}/v2/search",
                headers=self.headers,
                params=parameters,
            )
            data = response.json()["data"][0]
            pprint(data)
            flight_data = FlightData(
                price=data["price"],
                departure_city=data["route"][0]["cityFrom"],
                departure_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][1]["cityTo"],
                destination_airport=data["route"][1]["flyTo"],
                leave_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][2]["local_departure"].split("T")[0],
                stop_overs=1,
                via_city=data["route"][0]["cityTo"]
            )
            return flight_data
        else:
            flight_data = FlightData(
                price=data["price"],
                departure_city=data["route"][0]["cityFrom"],
                departure_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                leave_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0]
            )
            return flight_data
