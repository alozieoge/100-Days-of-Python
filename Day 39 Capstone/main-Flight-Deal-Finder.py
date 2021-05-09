# This file will need to use the DataManager, FlightSearch, FlightData, NotificationManager classes
# to achieve the program requirements.

from pprint import pprint
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager


data_manager = DataManager()
flight_search = FlightSearch()
messenger = NotificationManager()

sheet_data = data_manager.get_data_rows()
# pprint(sheet_data)

updated_sheet_data = []

for row in sheet_data:
    if row["iataCode"] == "":
        row["iataCode"] = flight_search.get_iata_code(row["city"])
        updated_sheet_data.append(row)

pprint(updated_sheet_data)

search_results = []
for row in updated_sheet_data:
    data_manager.update_data_rows(row["id"], row["city"], row["iataCode"], row["lowestPrice"])
    search_data = flight_search.search_flight_prices(row["iataCode"])
    # print(search_data)

    flight_data = FlightData(search_data)
    search_results.append(flight_data)

    print(f"{flight_data.destination_city}: £{flight_data.price}")

    if float(flight_data.price) < float(row["lowestPrice"]):
        messenger.send_sms(flight_data)






