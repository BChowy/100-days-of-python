from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from datetime import datetime, timedelta

DEPARTURE_CITY_IATA = "LON"

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()


prices_sheet = data_manager.get_destination_data()

if prices_sheet[0]["iataCode"] == "":
    for row in prices_sheet:
        city_code = flight_search.get_city_code(row["city"])
        row["iataCode"] = city_code
    print(prices_sheet)

    data_manager.destination_data = prices_sheet
    data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in prices_sheet:
    flight = flight_search.check_flights(
        DEPARTURE_CITY_IATA,
        destination["iataCode"],
        date_from=tomorrow,
        date_to=six_month_from_today
    )

    if flight is None:
        continue

    if flight.price < destination["lowestPrice"]:
        notification_manager.send_sms(
            message=f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        )
