from flask import Flask, send_from_directory
from flask_cors import CORS

app = Flask(__name__, static_folder="../web")
CORS(app)

# Serve homepage
@app.route("/")
def home():
    return send_from_directory("../web", "index.html")

# Serve CSS/JS files
@app.route("/<path:path>")
def static_files(path):
    return send_from_directory("../web", path)

if __name__ == "__main__":
    app.run(port=5500, debug=True)
