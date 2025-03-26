from flask import request, jsonify

def bike_selection():
    try:
        data = request.get_json()
        bike = data.get("bike")
        if bike:
            print(f"Received bike selection: {bike}")
            return jsonify({"status": "success", "message": f"Bike {bike} selected"}), 200
        else:
            return jsonify({"status": "error", "message": "No bike selected"}), 400
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# ADD THIS FUNCTION
def test_bike_selection():
    test_bike = "Titan E-TWO"
    print(f"[TEST] Responding with hardcoded bike: {test_bike}")
    return jsonify({"status": "success", "message": f"Bike {test_bike} selected"}), 200

