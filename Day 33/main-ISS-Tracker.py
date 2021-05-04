import smtplib
import requests
from datetime import datetime
import time

MY_LAT =   # Your latitude
MY_LONG =   # Your longitude

EMAIL_FROM = ""
PASSWORD = ""
EMAIL_TO = ""
SMTP_HOST = ""


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    # If it's dark outside
    if time_now <= sunrise or time_now >= sunset:
        return True


while True:
    # If the ISS is close to my current position and it is currently dark
    if is_iss_overhead() and is_night():
        # Then send me an email to tell me to look up.
        with smtplib.SMTP_SSL(host=SMTP_HOST, port=465) as connection:
            connection.login(user=EMAIL_FROM,
                             password=PASSWORD)
            connection.sendmail(from_addr=EMAIL_FROM,
                                to_addrs=EMAIL_TO,
                                msg="Subject:ISS Tracker\n\nThe ISS is above you in the sky. Step outside to view it.")

    # BONUS: run the code every 60 seconds.
    time.sleep(60)

