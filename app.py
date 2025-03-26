# app.py
from flask import request, jsonify

def bike_selection():
    try:
        data = request.get_json()
        bike = data.get("bike", "").lower()
        print(f"Extracted bike selection: {bike}")

        if bike:
            return jsonify({"status": "success", "message": f"Bike {bike} selected"}), 200
        else:
            return jsonify({"status": "error", "message": "No bike selected"}), 400
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

def test_bike_selection():
    # Send fake test response to ESP
    response = {
        "status": "success",
        "message": "Bike Vtuvia SN100 selected"
    }
    print("Sent test response to ESP: Vtuvia SN100")
    return jsonify(response), 200
