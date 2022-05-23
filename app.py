import requests
import os
from datetime import datetime

from dotenv import load_dotenv

load_dotenv()
APIkey = os.getenv('APIkey')

location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+APIkey


api_link = requests.get(complete_api_link)
api_data = api_link.json()


try:
    api_link = requests.get(complete_api_link)
    api_data = api_link.json()
    temp_city = ((api_data['main']['temp']) - 273.15)
    weather_desc = api_data['weather'][0]['description']
    hmdt = api_data['main']['humidity']
    wind_spd = api_data['wind']['speed']
    date_time = datetime.now().strftime("%d/%m/%y | %I:%M:%S %p")
except Exception as e:
    print("invalid")
else:
    print("--------------------------------------------------------")
    print(f"Weather stats for - {location} || {date_time}")
    print("--------------------------------------------------------")

    print(f"Current temperature is: {temp_city} .C")
    print(f"Current weather description: {weather_desc}")
    print(f"Current Humidity: {hmdt}")
    print(f"Current wind speed: {wind_spd}")

