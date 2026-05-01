from flask import Flask, request, jsonify
import requests
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_weather(city):

    # DEMO MODE (no setup required)
    if not API_KEY:
        return {
            "location": city,
            "tempC": 22,
            "condition": "clear"
        }

    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        data = requests.get(url).json()

        return {
            "location": data["name"],
            "tempC": data["main"]["temp"],
            "condition": data["weather"][0]["main"].lower()
        }

    except:
        return {"error": "Weather service failed"}

@app.route("/weather")
def weather():
    city = request.args.get("city")
    return jsonify(get_weather(city))

if __name__ == "__main__":
    app.run(port=5000)
