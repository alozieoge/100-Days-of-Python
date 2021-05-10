from pprint import pprint
import requests

SHEETY_PRICES_ENDPOINT = ""
SHEETY_USERS_ENDPOINT = ""
SHEETY_AUTH_TOKEN = ""

sheety_headers = {
    "Authorization": f"Bearer {SHEETY_AUTH_TOKEN}",
}

class DataManager:

    def __init__(self):
        self.destination_data = {}
        self.user_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=sheety_headers)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                headers=sheety_headers
            )
            print(response.text)

    def get_email(self):
        response = requests.get(url=SHEETY_USERS_ENDPOINT, headers=sheety_headers)
        data = response.json()
        self.user_data = data["users"]
        return self.user_data
