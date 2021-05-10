import os
import requests
import smtplib

sheety_endpoint = os.environ.get("SHEETY_ENDPOINT")
sheety_auth_token = os.environ.get("SHEETY_AUTH_TOKEN")

sheety_headers = {
    "Authorization": f"Bearer {sheety_auth_token}", 
    "Content-Type": "application/json", 
}

def validate_email():
    email_1 = input("What is your email?\n")
    email_2 = input("Type your email again.\n")
    if email_1 != email_2:
        print("Your email does not match. Please try again.")
        validate_email()
    # else:
    #     print("You're in the club!")
    return email_1


print("Welcome to Alozie's Flight Club.\nWhere we find the best flight deals and email you.")

# Get user full name and email
first_name = input("What is your first name?\n").title()
last_name = input("What is your last name?\n").title()
email = validate_email()

# POST user details to Google Sheet
users_sheet_url = f"{sheety_endpoint}/users"
users_data = {
    "user": {
        "firstName": first_name, 
        "lastName": last_name, 
        "email": email, 
    }
}

response = requests.post(url=users_sheet_url, json=users_data, headers=sheety_headers)
response.raise_for_status()
print("Success! Your email has been added to the Flight Club.")
print(response.text)

