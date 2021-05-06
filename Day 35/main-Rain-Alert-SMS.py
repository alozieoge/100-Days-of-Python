import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY = os.environ.get("OWM_API_KEY")

account_sid = "..."
auth_token = os.environ.get("AUTH_TOKEN")

weather_params = {
    "lat": 10.642707,
    "lon": -71.612534,
    "exclude": "current,minutely,daily",
    "appid": API_KEY,
}

response = requests.get(url=OWM_ENDPOINT, params=weather_params)
print(response.status_code)
response.raise_for_status()
weather_data = response.json()
hourly_data = weather_data["hourly"]

weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
        .create(body="It's going to rain today. Remember to bring an umbrella ☂.",
                from_='my_twilio_num',
                to='my_num'
                )

    print(message.sid)
    print(message.status)
