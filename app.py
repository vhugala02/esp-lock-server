from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Render is working!"

# New route for bike selection
@app.route('/bike_selection', methods=['POST'])
def bike_selection():
    data = request.get_json()  # Get JSON data from Power Automate
    if 'bike' in data:
        selected_bike = data['bike']
        print(f"Received bike selection: {selected_bike}")  # This will appear in Render logs
        return jsonify({"message": f"Bike {selected_bike} selected"}), 200

    return jsonify({"error": "Invalid request"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
