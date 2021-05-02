import pandas as pd
import datetime as dt
import random
import smtplib

##################### Extra Hard Starting Project ######################
MY_EMAIL = ""
MY_PASSWORD = ""
SMTP_HOST = ""

# 1. Update the birthdays.csv
birthday_data = pd.read_csv("birthdays.csv")

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
month = now.month
day = now.day

for (index, row) in birthday_data.iterrows():
    if row["month"] == month and row["day"] == day:
        # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's
        # actual name from birthdays.csv
        with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as letter_file:
            random_letter = letter_file.read()
        birthday_letter = random_letter.replace("[NAME]", row["name"])

        # 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP_SSL(host=SMTP_HOST, port=465) as connection:
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            message = f"Subject:Happy Birthday\n\n{birthday_letter}"
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=row["email"],
                                msg=message.encode("utf-8"))




