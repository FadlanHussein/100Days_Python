from flask import Flask, jsonify

app = Flask(__name__)

# Root Endpoint
@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Mini Weather API!"})

if __name__ == '__main__':
    app.run(debug=True)
    
