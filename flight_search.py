""" This class is responsible for TALKING to the flight search api. """

import os
import requests
from flight_data import FlightData


# --------------------------------------------------------------------- FLIGHT
FLIGHT_API_KEY = os.environ["FLIGHT_API_KEY"]
FLIGHT_SEARCH_ENDPOINT = "https://api.tequila.kiwi.com/v2/search"
FLIGHT_LOCATION_ENDPOINT = "https://api.tequila.kiwi.com/locations/query"
FLIGHT_SEARCH_HEADER = {"apikey": FLIGHT_API_KEY}


class FlightSearch:

    def get_destination_code(self, city_name):
        location_endpoint = f"{FLIGHT_LOCATION_ENDPOINT}"
        headers = {"apikey": FLIGHT_API_KEY}
        query = {"term": city_name, "location_types": "city"}
        response = requests.get(url=location_endpoint, headers=headers, params=query)
        results = response.json()["locations"]
        code = results[0]["code"]
        return code

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        headers = {"apikey": FLIGHT_API_KEY}
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time,  # .strftime("%d/%m/%Y")
            "date_to": to_time,  # .strftime("%d/%m/%Y")
            "selected_cabins": "M",
            "adult_hold_bag": "1",
            "adult_hand_bag": "1",
            "curr": "USD"
        }

        response = requests.get(
            url=f"{FLIGHT_SEARCH_ENDPOINT}",
            headers=headers,
            params=query,
        )

        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["cityFrom"],
            origin_airport=data["flyFrom"],
            destination_city=data["cityTo"],
            destination_airport=data["flyTo"],
            out_date=data["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: ${flight_data.price}")
        return flight_data
