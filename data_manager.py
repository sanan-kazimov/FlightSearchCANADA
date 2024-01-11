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

# TODO SOLVE!!! row_id problem. all data appears only on the first row!!!
    def update_destination_codes(self, row_id):
        for city in self.destination_data:
            new_data = {
                "IATA Code": city["IATA Code"]
            }
            response = requests.put(
                url=f"{SHEET_BEST_ENDPOINT_FLIGHTDEALS}/{row_id}",
                json=new_data
            )
            print(response.text)
