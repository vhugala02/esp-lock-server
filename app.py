from flask import request, jsonify

def bike_selection():
    try:
        data = request.get_json()
        bike = data.get("bike", "").strip()  # Extract and remove spaces

        if bike and bike.lower() != "none":
            print(f"Received bike selection: {bike}")
            return jsonify({"status": "success", "message": f"Bike {bike} selected"}), 200
        else:
            print("DEBUG: No valid bike received.")
            return jsonify({"status": "error", "message": "No bike selected"}), 400
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
