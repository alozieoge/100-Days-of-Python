import requests
from datetime import datetime

USERNAME = ""
TOKEN = ""
GRAPH_ID = ""

pixela_endpoint = "https://pixe.la/v1/users"

# 1. Create a user account using HTTP POST request
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.status_code)
# print(response.text)

# 2. Create a Pixel graph using HTTP POST request and header authentication
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "km",
    "type": "float",
    "color": "momiji",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# 4. Create a day's pixel data using HTTP POST request and header authentication
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
# print(today)
# print(today.strftime("%Y%m%d"))
# print(today.strftime("%Y-%m-%d"))

yesterday = datetime(year=2021, month=5, day=6)

# pixel_data = {
#     "date": "20210507",
#     "quantity": "1.0",
# }

# 6. Autofill the day's date using datetime.strftime()
pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kilometers did you cycle today? "),
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)

# 7. Update yesterday's pixel using HTTP PUT request
date = yesterday.strftime("%Y%m%d")
pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date}"

pixel_update = {
    "quantity": "1.0",
}

# response = requests.put(url=pixel_update_endpoint, json=pixel_update, headers=headers)
# print(response.text)

# 8. Delete a day's pixel using HTTP DELETE request
pixel_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date}"

# response = requests.delete(url=pixel_delete_endpoint, headers=headers)
# print(response.text)
