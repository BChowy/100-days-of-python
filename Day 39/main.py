from data_manager import DataManager
from flight_search import FlightSearch

data_manager = DataManager()

prices_sheet = data_manager.get_destination_data()

if prices_sheet[0]["iataCode"] == "":
    flight_search = FlightSearch()
    for row in prices_sheet:
        city_code = flight_search.get_city_code(row["city"])
        row["iataCode"] = city_code
    print(prices_sheet)

    data_manager.destination_data = prices_sheet
    data_manager.update_destination_codes()
