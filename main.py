import requests
from twilio.rest import Client


### GET key from openweathermap.org
OWM_ENDPOINT="https://api.openweathermap.org/data/2.5/forecast"
api_key = "<USE YOUR KEY>"

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
client = Client(account_sid, auth_token)

## Get Longitude and latitude from https://latlong.net/ for your city and replace.
weaher_params = {
    "lat" : 28.485840,
    "lon" : 77.500710,
    "appid" : api_key,
    "cnt": 4
}


weather_value = requests.get(OWM_ENDPOINT,params=weaher_params)
weather_value.raise_for_status()

weather_data = weather_value.json()["list"]
#print(weather_data)

will_rain = True
for weather in weather_data:
     weather_cond = weather["weather"]
     for cond in weather_cond:
        # print(cond["id"])
         if cond["id"] < 700:
             will_rain = True

if will_rain:
    message = client.messages.create(
        body="Today going to rain take umbrella!!",
        from_="<Twilo give you a number>",
        to="Number to send ",
    )
    print(message.body)


