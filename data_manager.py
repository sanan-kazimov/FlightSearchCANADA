""" This class is responsible for TALKING to the Google SHEET. """

import os
import requests

# ---------------------------------------------------- FLIGHTDEALS SHEET
SHEET_BEST_ENDPOINT_FLIGHTDEALS = os.environ["SHEET_BEST_ENDPOINT_FLIGHTDEALS"]
SHEET_BEST_API_KEY_FLIGHTDEALS = os.environ["SHEET_BEST_API_KEY_FLIGHTDEALS"]


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEET_BEST_ENDPOINT_FLIGHTDEALS)
        # data = response.json()
        # self.destination_data = data["prices"]
        self.destination_data = response.json()
        return self.destination_data

# TODO SOLVE!!! only IATA Code column is updated, rest is being erased
    def update_destination_codes(self):
        for row_id, city in enumerate(self.destination_data):
            print(f'DATA_MANAGER, update_destination_codes, city: {city}')


            new_data = {
                "IATA Code": city["IATA Code"]
            }
            print(f'DATA_MANAGER, update_destination_codes, new_data: {new_data}')

            print(f'DATA_MANAGER, update_destination_codes, row_id: {row_id}')
            response = requests.put(
                url=f"{SHEET_BEST_ENDPOINT_FLIGHTDEALS}/{row_id}",
                json=new_data
            )

            print(response.text)
