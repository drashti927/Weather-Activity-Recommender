from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def generate_weather(city):
    city = city.lower()

    # deterministic variation (so every city is different)
    if "london" in city:
        return {"location": city, "tempC": 12, "condition": "rain"}
    elif "seattle" in city:
        return {"location": city, "tempC": 15, "condition": "cloud"}
    elif "dubai" in city:
        return {"location": city, "tempC": 38, "condition": "sunny"}
    elif "paris" in city:
        return {"location": city, "tempC": 18, "condition": "cloud"}
    elif "new york" in city:
        return {"location": city, "tempC": 20, "condition": "rain"}
    else:
        return {
            "location": city,
            "tempC": 22,
            "condition": "clear"
        }

@app.route("/weather")
def weather():
    city = request.args.get("city")
    return jsonify(generate_weather(city))

if __name__ == "__main__":
    app.run(port=5000, debug=True)
