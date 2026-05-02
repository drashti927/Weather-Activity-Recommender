from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

API_KEY = os.getenv("OPENWEATHER_API_KEY")

@app.route("/weather")
def weather():
    city = request.args.get("city")

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    res = requests.get(url)

    if res.status_code != 200:
        return jsonify({"error": "City not found"}), 400

    data = res.json()

    return jsonify({
        "location": city,
        "tempC": data["main"]["temp"],
        "condition": data["weather"][0]["main"].lower()
    })

if __name__ == "__main__":
    app.run(port=5000, debug=True)
