from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import json
import random

app = Flask(__name__)
CORS(app)

with open("data/recommendations.json") as f:
    REC_DATA = json.load(f)

@app.route("/recommend")
def recommend():
    user_id = request.args.get("userId")
    city = request.args.get("city")

    weather = requests.get(f"http://localhost:5000/weather?city={city}").json()
    user = requests.get(f"http://localhost:5001/user/{user_id}").json()

    condition = weather.get("condition", "default")

    if "rain" in condition:
        options = REC_DATA["rain"]
    elif "clear" in condition or "sun" in condition:
        options = REC_DATA["clear"]
    elif "cloud" in condition:
        options = REC_DATA["cloud"]
    else:
        options = REC_DATA["default"]

    recommendation = random.choice(options)

    return jsonify({
        "userId": user_id,
        "location": city,
        "weather": condition,
        "recommendation": recommendation
    })

if __name__ == "__main__":
    app.run(port=5002, debug=True)
