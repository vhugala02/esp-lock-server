from flask import request, jsonify

# Global variable to simulate a bike selection
test_bike_value = {"bike": "Vtuvia SN100"}

def bike_selection():
    try:
        data = request.get_json()
        bike = data.get("bike")
        print(f"Raw incoming data: {data}")
        print(f"Extracted bike selection: {bike}")
        if bike:
            return jsonify({"status": "success", "message": f"Bike {bike} selected"}), 200
        else:
            return jsonify({"status": "error", "message": "No bike selected"}), 400
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

def test_bike_selection():
    # Hardcoded test value returned as if it came from form
    return jsonify({"status": "success", "message": f"Bike {test_bike_value['bike']} selected"})

