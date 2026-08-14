import requests
import matplotlib.pyplot as plt

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
    while True:
        print("\nMenu:")
        print("1. View Weather Forecast")
        print("2. Compare Weather")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            city = input("Enter the city name: ")
            data = fetch_weather(city)
            if data:
                display_weather_data(data)
        elif choice == "2":
            raw_cities = input("Enter the city names (comma separated): ")
            cities = raw_cities.split(",")
            compare_weather(cities)
        elif choice == "3":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()