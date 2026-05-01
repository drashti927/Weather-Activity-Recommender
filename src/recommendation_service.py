from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/recommend")
def recommend():

    user_id = request.args.get("userId")
    city = request.args.get("city")

    weather = requests.get(f"http://localhost:5000/weather?city={city}").json()
    user = requests.get(f"http://localhost:5001/user/{user_id}").json()

    condition = weather.get("condition", "clear")
    indoor = user.get("indoorPreferred", True)

    if "rain" in condition:
        suggestion = "Visit a museum"
    elif indoor:
        suggestion = "Go to a café or gallery"
    else:
        suggestion = "Go hiking outdoors"

    return jsonify({
        "userId": user_id,
        "location": city,
        "recommendation": suggestion
    })

if __name__ == "__main__":
    app.run(port=5002)
