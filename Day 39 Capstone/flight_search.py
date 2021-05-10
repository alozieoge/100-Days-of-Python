import requests
import os
from pprint import pprint
from datetime import datetime, timedelta

# flight_search_endpoint = os.environ["FLIGHT_SEARCH_ENDPOINT"]
# flight_search_api_key = os.environ["FLIGHT_SEARCH_API_KEY"]

FLIGHT_SEARCH_ENDPOINT = ""
FLIGHT_SEARCH_API_KEY = ""


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.search_url = FLIGHT_SEARCH_ENDPOINT

        self.search_header = {
            "apikey": FLIGHT_SEARCH_API_KEY,
        }

        self.tomorrow = datetime.now() + timedelta(days=1)

    def get_iata_code(self, city):
        self.search_url = f"{FLIGHT_SEARCH_ENDPOINT}/locations/query"

        search_params = {
            "term": city,
            "location_types": "city",
        }

        response = requests.get(url=self.search_url, params=search_params, headers=self.search_header)
        # print(response.status_code)
        data = response.json()
        # print(data)
        return data["locations"][0]["code"]

    def search_flight_prices(self, destination):
        self.search_url = f"{FLIGHT_SEARCH_ENDPOINT}/v2/search"
        tomorrow_date = self.tomorrow.strftime("%d/%m/%Y")
        six_months_tomorrow_date = (self.tomorrow + timedelta(days=60*3)).strftime("%d/%m/%Y")

        search_params = {
            "fly_from": "LON",
            "fly_to": destination,
            "date_from": tomorrow_date,
            "date_to": six_months_tomorrow_date,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "curr": "GBP",
            "max_stopovers": 0,
            "sort": "price",
            "asc": 1,
            "limit": 2,
        }

        response = requests.get(url=self.search_url, params=search_params, headers=self.search_header)
        # print(response.status_code)
        # print(response.json())
        return response.json()




