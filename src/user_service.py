from flask import Flask, request, jsonify

app = Flask(__name__)

users = {}

@app.route("/user/<user_id>", methods=["GET"])
def get_user(user_id):
    return jsonify(users.get(user_id, {}))

@app.route("/user", methods=["POST"])
def create_user():
    data = request.json
    users[data["userId"]] = data
    return jsonify({"message": "user created"})

if __name__ == "__main__":
    app.run(port=5001)
