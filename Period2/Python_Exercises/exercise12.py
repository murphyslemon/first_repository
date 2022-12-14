import json
import textwrap
import requests

# Problem 1
request1 = "https://api.chucknorris.io/jokes/random"
try:
    response1 = requests.get(request1)
    if response1.status_code == 200:
        json_response1 = response1.json()
        print("Your random and terrible Chuck Norris joke of the day is: ")
        print(textwrap.fill(json_response1['value'], width=100))

except requests.exceptions.RequestException as e:
    print("Request could not be completed.")

# Problem 2
ex12_api_key = "873df6e3e029ba2d8538f1482461817f"
location_name = input("Please enter city name: ")
request2 = "https://api.openweathermap.org/data/2.5/weather?q=" + location_name + "&appid=" + ex12_api_key + "&units=metric"

try:
    response2 = requests.get(request2)
    if response2.status_code == 200:
        json_response2 = response2.json()
        print(f"The weather in {location_name} is {json_response2['weather'][0]['description']}"
              f" and the temperature is {json_response2['main']['temp']} degrees")

except requests.exceptions.RequestException as e:
    print("Request could not be completed.")
