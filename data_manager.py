""" This class is responsible for TALKING to the Google SHEET. """

import os
import requests

# ---------------------------------------------------- FLIGHTDEALS SHEET
ENDPOINT_FLIGHTDEALS_SHEET = os.environ["SHEET_BEST_ENDPOINT_FLIGHTDEALS"]
TAB_PRICES_FLIGHTDEALS = "/tabs/prices"
TAB_USERS_FLIGHTDEALS = "/tabs/users"
API_KEY_FLIGHTDEALS_SHEET = os.environ["SHEET_BEST_API_KEY_FLIGHTDEALS"]


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=ENDPOINT_FLIGHTDEALS_SHEET)
        self.destination_data = response.json()
        return self.destination_data

    def update_destination_codes(self):
        for row_id, row in enumerate(self.destination_data):
            new_row = {
                "City": row["City"],
                "IATA Code": row["IATA Code"],
                "Lowest Price": row["Lowest Price"]
            }

            response = requests.put(
                url=f"{ENDPOINT_FLIGHTDEALS_SHEET}/{row_id}",
                json=new_row
            )

            print(response.text)
