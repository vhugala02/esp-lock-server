from flask import request, jsonify

def bike_selection():
    try:
        data = request.get_json()
        bike = data.get("bike")  # Extract selected bike

        if not bike or bike.lower() == "none":
            print("DEBUG: No valid bike received.")  # Debugging log
            return jsonify({"status": "error", "message": "No bike selected"}), 400

        print(f"DEBUG: Extracted bike selection: {bike}")
        return jsonify({"status": "success", "message": f"Bike {bike} selected"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
