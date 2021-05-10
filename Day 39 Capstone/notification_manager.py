import os
from twilio.rest import Client
from flight_data import FlightData

# account_sid = os.environ["TWILIO_ACCOUNT_SID"]
# auth_token = os.environ["TWILIO_AUTH_TOKEN"]
# from_number = os.environ["FROM_NUMBER"]
# to_number = os.environ["TO_NUMBER"]

TWILIO_ACCOUNT_SID = ""
TWILIO_AUTH_TOKEN = ""

FROM_NUMBER = ""
TO_NUMBER = ""


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(username=TWILIO_ACCOUNT_SID, password=TWILIO_AUTH_TOKEN)

    def send_sms(self, flight_data: FlightData):
        message_body = f"\nLow price alert!\nOnly £{flight_data.price} to fly from " \
                       f"{flight_data.departure_city}-{flight_data.departure_code} to " \
                       f"{flight_data.destination_city}-{flight_data.destination_code}, " \
                       f"from {flight_data.departure_date} to {flight_data.arrival_date}."

        # print(message_body)

        message = self.client.messages.create(
            body=message_body,
            from_=FROM_NUMBER,
            to=TO_NUMBER
        )

        print(message.sid)
