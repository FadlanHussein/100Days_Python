import requests
from matplotlib import pyplot as plt

API_KEY = "c41b1a25e8b81046ef812395a7250686"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def fetch_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to fetch weather data: {response.status_code} - {response.text}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

def display_weather_data(data):
    print(f"City: {data['name']}")
    print(f"Temperature: {data['main']['temp']} °C")
    print(f"Humidity: {data['main']['humidity']}%")
    print(f"Weather: {data['weather'][0]['description']}")

def plot_weather_trend(days, temperatures):
    plt.plot(days, temperatures, marker='o', color='blue')
    plt.xlabel("Days")
    plt.ylabel("Temperature (°C)")
    plt.title("Weather Trend")
    plt.grid()
    plt.show()

def compare_weather(cities):
    valid_cities = []
    valid_temps = []
    for city in cities:
        city_name = city.strip()
        data = fetch_weather(city_name)
        if data and 'main' in data:
            valid_cities.append(data.get('name', city_name))
            valid_temps.append(data['main']['temp'])

    if valid_cities:
        plt.bar(valid_cities, valid_temps, color='skyblue')
        plt.xlabel("Cities")
        plt.ylabel("Temperature (°C)")
        plt.title("Weather Comparison")
        plt.grid(axis='y')
        plt.show()
    else:
        print("No weather data found for the given cities.")

def main():
    print("Welcome to the Global Weather Dashboard")
    city = input("Enter the city name: ")
    data = fetch_weather(city)
    if data:
        display_weather_data(data)

        # Simulated data for trend visualization
        days = ["Day 1", "Day 2", "Day 3", "Day 4", "Day 5"]
        temperatures = [25, 26, 27, 28, 29]
        plot_weather_trend(days, temperatures)

if __name__ == "__main__":
    main()