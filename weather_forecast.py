import requests

# Enter your OpenWeatherMap API key here
api_key = "your_api_key"

# URL for OpenWeatherMap API
weather_url = "https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"

# URL for GeoDB Cities API to check city validity
cities_url = "https://wft-geo-db.p.rapidapi.com/v1/geo/cities"

# Headers for GeoDB Cities API
headers = {
    "x-rapidapi-host": "wft-geo-db.p.rapidapi.com",
    "x-rapidapi-key": "your_rapidapi_key"
}

# Get city input from user
city = input("Enter city name: ")

# Check if city is valid using GeoDB Cities API
response = requests.get(cities_url, headers=headers, params={"namePrefix": city})
data = response.json()

# If city is not found, raise an error and exit the program
if len(data["data"]) == 0:
    print("City not found.")
    exit()

# Get city ID from GeoDB Cities API
city_id = data["data"][0]["id"]

# Get weather data for city from OpenWeatherMap API
url = weather_url.format(city=city, api_key=api_key)
response = requests.get(url)
data = response.json()

# Print weather forecast for next 5 days
print("Weather forecast for", city, "\n")
for forecast in data["list"][:5]:
    date = forecast["dt_txt"].split()[0]
    time = forecast["dt_txt"].split()[1]
    weather = forecast["weather"][0]["description"]
    temp = forecast["main"]["temp"]
    print(date, time, "-", weather, "-", str(temp) + "°C")
