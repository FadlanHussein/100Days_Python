from flask import Flask, jsonify

app = Flask(__name__)

# Mock weather data
weather_data = {
    "New York": {"temperature": 15, "condition": "Cloudy"},
    "Los Angeles": {"temperature": 25, "condition": "Sunny"},
    "Chicago": {"temperature": 10, "condition": "Rainy"},
    "San Francisco": {"temperature": 18, "condition": "Foggy"},
    "Seattle": {"temperature": 12, "condition": "Rainy"},
}

# Root Endpoint
@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Mini Weather API!"})

# Root Endpoint
@app.route('/weather', methods=['GET'])
def get_weather():
    return jsonify(weather_data)

# Get Weather for a Specific City
@app.route('/weather/<city>', methods=['GET'])
def get_weather_by_city(city):
    city = city.title()
    if city in weather_data:
        return jsonify({city: weather_data[city]})
    return jsonify({"error": "City not found"}), 404

# Run Application
if __name__ == '__main__':
    app.run(debug=True, port=5006)
