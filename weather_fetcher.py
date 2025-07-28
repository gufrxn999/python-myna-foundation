import requests

API_KEY = "7e07e81ca7465257067c2ead931ffdf2"  # Replace with your OpenWeatherMap API key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter city name: ")
params = {'q': city, 'appid': API_KEY, 'units': 'metric'}

response = requests.get(BASE_URL, params=params)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temp = data['main']['temp']
    print(f"\nWeather in {city}: {weather}")
    print(f"Temperature: {temp}°C")
else:
    print(f"\nError fetching data for '{city}'. Please check the city name.")
