from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/bike_selection', methods=['POST'])
def bike_selection():
    try:
        data = request.get_json()
        bike = data.get("bike")  # Extract selected bike
        if bike:
            print(f"Received bike selection: {bike}")
            return jsonify({"status": "success", "message": f"Bike {bike} selected"}), 200
        else:
            return jsonify({"status": "error", "message": "No bike selected"}), 400
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
