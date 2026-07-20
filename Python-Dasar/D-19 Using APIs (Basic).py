# %% What is API

import requests
url = "https://api.openweathermap.org/data/2.5/weather"

informasi_tambahan = { "q": "Jakarta", "appid": "71ae6cf2ddaab748db49ef346f50e3d1"}

response = requests.get(url, params=informasi_tambahan)

if response.status_code == 200:
    data = response.json()
    print(data)

else:
    print("An error occured. Status Code:  ", response.status_code)
    


# %% Weather App Using OpenWeatherMap API
# Step 1: Api Setup
import requests
API_KEY = "71ae6cf2ddaab748db49ef346f50e3d1"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# Step 2: Get Weather Data

def get_weather(city):
    try:
        url = f"{BASE_URL}?Q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather = {
                "City": data['name'],
                "Temperature": data['main']['temp'],
                "Humidity": data['main']['humidity'],
                "Description": data['weather'][0]['description'],
                "Wind Speed": data['wind']['speed']
            }
            return weather
        else:
            print("City Not Found!")
            return None
    except Exception as e:
        print(f"Error: {str(e)}")
        return None
