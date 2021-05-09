class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, flight_search_result):
        self.price = flight_search_result["data"][0]["price"]
        self.departure_code = flight_search_result["data"][0]["cityCodeFrom"]
        self.departure_city = flight_search_result["data"][0]["cityFrom"]
        self.destination_code = flight_search_result["data"][0]["cityCodeTo"]
        self.destination_city = flight_search_result["data"][0]["cityTo"]
        self.departure_date = flight_search_result["data"][0]["route"][0]["local_departure"].split(".")[0]
        self.arrival_date = flight_search_result["data"][0]["route"][1]["local_arrival"].split(".")[0]

        departure_seconds = flight_search_result["data"][0]["duration"]["departure"]
        self.departure_duration = departure_seconds / 3600
        arrival_seconds = flight_search_result["data"][0]["duration"]["return"]
        self.return_duration = arrival_seconds / 3600

