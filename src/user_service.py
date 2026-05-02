from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

users = {
    "1": {"indoorPreferred": True, "activities": ["museum", "movies", "cafes"]},
    "2": {"indoorPreferred": False, "activities": ["sports", "hiking", "cycling",]}
}

@app.route("/user/<user_id>")
def get_user(user_id):
    return jsonify(users.get(user_id, users["1"]))

if __name__ == "__main__":
    app.run(port=5001, debug=True)
