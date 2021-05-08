import requests
from datetime import datetime
import os

NUTRIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
# Since the Sheety API endpoint contains your Google Sheet URL, add the endpoint to the environment variables.
SHEETY_TOKEN = os.environ["<sheety-token>"]
SHEETY_ENDPOINT = os.environ["https://api.sheety.co/<google-sheet-url>/<sheety-project-name>/<google-sheet-name>"]

# 1. Define header and body dictionaries for the NutritionIX API request.
nutrix_headers = {
    "x-app-id": "",
    "x-app-key": "",
    "Content-Type": "application/json",
}

nutrix_body = {
    "query": "",
    "gender": "",
    "weight_kg": 0,
    "height_cm": 0,
    "age": 0,
}

# 2. Get user input about exercise in free text
query = input("Tell me which exercises you did: ")
nutrix_body["query"] = query

# 3. Make HTTP POST request to NutritionIX API to format and return additional exercise data e.g. calories
response = requests.post(url=NUTRIX_ENDPOINT, json=nutrix_body, headers=nutrix_headers)
# print(response.status_code)
# print(response.text)

exercise_data = response.json()

# 4. Define header and body for the Sheety API request
# Bearer Token
sheety_header = {
    "Authorization": f"Bearer {SHEETY_TOKEN}"
}

# Sheety expects your record to be nested in a singular root property named after your sheet.
# For example if your endpoint is named 'workouts', nest your record in a property called 'workout'.
# https://sheety.co/docs/requests.html

sheety_body = {
    "workout": {
        "date": "",  # "21/07/2020",
        "time": "",  # "15:00:00",
        "exercise": "",  # "Running",
        "duration": 0,  # 22,
        "calories": 0,  # 130,
    }
}

# 5. Convert today's date and the current time into strings
today = datetime.now()
sheety_body["workout"]["date"] = today.strftime("%d/%m/%Y")
sheety_body["workout"]["time"] = today.strftime("%H:%M:%S")

# 6. For each exercise type returned from the NutritionIX API POST request,
# create a new row in the Google sheet using the Sheety API POST request.
for exercise in exercise_data["exercises"]:
    sheety_body["workout"]["exercise"] = exercise["name"].title()
    sheety_body["workout"]["duration"] = float(exercise["duration_min"])
    sheety_body["workout"]["calories"] = float(exercise["nf_calories"])

    # print(sheety_body)

    response = requests.post(url=SHEETY_ENDPOINT, json=sheety_body, headers=sheety_header)
    print(response.status_code)
    print(response.text)
