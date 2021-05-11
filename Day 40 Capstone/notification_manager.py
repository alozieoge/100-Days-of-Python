from twilio.rest import Client
import smtplib

TWILIO_SID = ""
TWILIO_AUTH_TOKEN = ""
TWILIO_VIRTUAL_NUMBER = ""
TWILIO_VERIFIED_NUMBER = ""

EMAIL_FROM = ""
PASSWORD = ""
EMAIL_TO = ""
SMTP_HOST = ""


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
        # print(message)

    def send_email(self, message, url, email):
        message_body = f"Subject: New Low Price Flight!\n\n{message}\n{url}"
        # print(email)
        # print(message_body)
        with smtplib.SMTP_SSL(host=SMTP_HOST, port=465) as connection:
            connection.login(user=EMAIL_FROM, password=PASSWORD)
            connection.sendmail(from_addr=EMAIL_FROM,
                                to_addrs=email,
                                msg=message_body.encode("utf-8")
                                )

