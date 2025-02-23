import os 
import requests
from dotenv import load_dotenv


city_name = input("Enter your city: ").strip().lower()
print("\nFetching Weather data..\n")

load_dotenv(dotenv_path=".env")
API_KEY = os.getenv("WEATHER_API_KEY")


response = requests.get(f"http://api.weatherstack.com/current?access_key={API_KEY}&query={city_name}")

if response.status_code == 200:
    data = response.json()

    if "current" in data:

        temperature = data["current"]["temperature"]
        humidity = data["current"]["humidity"]
        wea_des = data["current"]["weather_descriptions"][0]
        wind_speed = data["current"]["wind_speed"]

        print(f"Weather in {city_name}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {wea_des}")
        print(f"Wind Speed: {wind_speed}")

    else:
        print(f"Error: {data.get('error', {}).get('info', 'Invalid city or API issue')}")

else:
    print(f"Error: Unable to fetch weather data. HTTP Status Code: {response.status_code}") 



