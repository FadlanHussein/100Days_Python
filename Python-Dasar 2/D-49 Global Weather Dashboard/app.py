import requests

API_KEY = "c41b1a25e8b81046ef812395a7250686"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
def get_weather(city):
    try:
        response = requests.get(f"{BASE_URL}?q={city}&appid={API_KEY}")
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to fetch weather data: {response.status_code} - {response.text}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

if __name__ == "__main__":
    weather_data = get_weather("Jakarta")
    if weather_data:
        print("Weather Data:", weather_data)