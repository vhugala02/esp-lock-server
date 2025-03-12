from flask import Flask, request, jsonify
from app import bike_selection  # Import the function

app = Flask(__name__)  # Define the Flask app

# Define the existing routes
@app.route("/")
def home():
    return "ESP Lock Server is Running!"

@app.route("/unlock", methods=["POST"])
def unlock():
    return "Unlocking the Bike!", 200

@app.route("/lock", methods=["POST"])
def lock():
    return "Locking the Bike!", 200

# Include the bike selection route
@app.route("/bike_selection", methods=["POST"])
def bike_selection_route():
    return bike_selection()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
