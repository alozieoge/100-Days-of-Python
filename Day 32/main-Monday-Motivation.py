import smtplib
import datetime as dt
import random

MY_EMAIL = ""
MY_PASSWORD = ""
SMTP_HOST = ""

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 0:
    with open("quotes.txt", "r", encoding="utf-8") as quotes_file:
        quotes = quotes_file.readlines()
        random_quote = random.choice(quotes)

    # print(random_quote)
    with smtplib.SMTP_SSL(host=SMTP_HOST, port=465) as connection:
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        message = f"Subject:Motivation\n\n{random_quote}"
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs="",
                            msg=message.encode("utf-8"))
