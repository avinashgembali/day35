# import os
import requests
from twilio.rest import Client
# from twilio.http.http_client import TwilioHttpClient

LATITUDE = 17.886190
LONGITUDE = 83.446342
api_key = "YOUR API KEY FROM OPEN WEATHER MAP"
account_id = "YOUR ACCOUNT ID FROM TWILLIO"
auth_key = "YOUR AUTH KEY FROM TWILLIO"

client = Client

parameters = {
    'lat': LATITUDE,
    'lon': LONGITUDE,
    'appid': api_key,
    'cnt': 4
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_list = weather_data["list"]
# to get id weather_list[0]["weather"][0]["id"]
# as we are checking for next 12 hours our count will be four
count = 4
flag = False
for i in range(count):
    weather_id = weather_list[i]["weather"][0]["id"]
    if weather_id < 700:
        flag = True
        break
if flag:
    # proxy_client = TwilioHttpClient()
    # proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    client = Client(account_id, auth_key)
    message = client.messages \
        .create(
        body="its going to rain today !! take the umbrella !",
        from_="YOUR TWILLIO FREE TRIAL NUMBER",
        to="YOUR MOBILE NUMBER"
        )
    print(message.status)

else:
    print("no need umbrella")

# to work on python any where the code take the toggles and run code there and save if you get queued