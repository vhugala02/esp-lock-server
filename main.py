# main.py
from flask import Flask
from app import bike_selection, test_bike_selection

app = Flask(__name__)

@app.route("/")
def home():
    return "ESP Lock Server is Running!"

@app.route("/bike_selection", methods=["POST"])
def bike_selection_route():
    return bike_selection()

@app.route("/test_bike", methods=["GET"])
def test_bike_selection_route():
    return test_bike_selection()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
