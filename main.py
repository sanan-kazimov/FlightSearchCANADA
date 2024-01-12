from datetime import datetime, timedelta
from pprint import pprint

from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

DEPARTURE_AIRPORT_IATA = "GYD"
DEPARTURE_DATE_FROM = "18/04/2024"
DEPARTURE_DATE_TO = "24/04/2024"
# DEPARTURE_DATE_FROM = datetime.now() + timedelta(days=1)
# DEPARTURE_DATE_TO = datetime.now() + timedelta(days=(6 * 30))

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()

if sheet_data[0]["IATA Code"] == "":
    pprint(f'MAIN, sheet_data: {sheet_data}')
    for row in sheet_data:
        print(f"MAIN, row in sheet_data: {row}")
        row["IATA Code"] = flight_search.get_destination_code(row["City"])
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

for destination in sheet_data:
    flight = flight_search.check_flights(
        DEPARTURE_AIRPORT_IATA,
        destination["IATA Code"],
        from_time=DEPARTURE_DATE_FROM,
        to_time=DEPARTURE_DATE_TO
    )

    if flight.price < float(destination["Lowest Price"]):
        notification_manager.send_email(
            message=f"""Lower ticket price alert!
                    - Current date and time: {datetime.now().strftime("%d.%m.%Y, %H:%M")}
                    - Flight date: {flight.out_date}
                    - Flight price for today: ${flight.price} USD
                    - Departure city:  {flight.origin_city}-{flight.origin_airport}
                    - Destination city: {flight.destination_city}-{flight.destination_airport}"""
        )
