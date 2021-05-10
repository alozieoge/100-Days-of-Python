import os
import requests

# sheet_endpoint = os.environ["SHEET_ENDPOINT"]
# sheet_auth_token = os.environ["SHEET_AUTH_TOKEN"]
SHEET_ENDPOINT = ""
SHEET_AUTH_TOKEN = ""

sheet_headers = {
    "Authorization": f"Bearer {SHEET_AUTH_TOKEN}",
}


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheet_url = SHEET_ENDPOINT
        self.sheet_params = {
            "price": {
                "city": None,
                "iataCode": None,
                "lowestPrice": None,
            }
        }

    def get_data_rows(self):
        # Use the Sheety API to GET all the data in that sheet and print it out
        self.sheet_url = SHEET_ENDPOINT
        response = requests.get(url=self.sheet_url, headers=sheet_headers)
        # print(response.status_code)
        data = response.json()
        # pprint(data)
        # Pass everything stored in the "prices" key back to the main.py file
        return data["prices"]

    def update_data_rows(self, row_id, city, iata, price):
        # Make a PUT request and use the row id  from sheet_data to update the Google Sheet with the IATA codes
        self.sheet_url = f"{SHEET_ENDPOINT}/{row_id}"
        self.sheet_params["price"]["city"] = city
        self.sheet_params["price"]["iataCode"] = iata
        self.sheet_params["price"]["lowestPrice"] = price

        response = requests.put(url=self.sheet_url, json=self.sheet_params, headers=sheet_headers)
        # pprint(response.json())



