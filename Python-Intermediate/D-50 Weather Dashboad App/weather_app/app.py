from flask import Flask, render_template, request
import requests

API_KEY = "71ae6cf2ddaab748db49ef346f50e3d1"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

app = Flask(__name__)


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


def parse_weather(data):
    city = data['name']
    temperature = data['main']['temp']
    description = data['weather'][0]['description']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']
    pressure = data['main']['pressure']
    return {
        "city": city,
        "temperature": temperature,
        "description": description,
        "humidity": humidity,
        "wind_speed": wind_speed,
        "pressure": pressure
    }


@app.route('/', methods=['GET', 'POST'])
def home():
    weather = None
    if request.method == 'POST':
        city = request.form.get('city')
        if city:
            data = fetch_weather(city)
            if data:
                weather = parse_weather(data)
    return render_template("index.html", weather=weather)


if __name__ == '__main__':
    app.run(debug=True)