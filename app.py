from flask import request, jsonify

def bike_selection():
    try:
        data = request.get_json()
        bike = data.get("bike")  # Extract selected bike
        
        print(f"DEBUG: Raw incoming data: {data}")  # Log full data to check correctness
        print(f"DEBUG: Extracted bike selection: {bike}")

        if bike and bike != "none":  # Ensure bike is not empty or "none"
            print(f"Received bike selection: {bike}")
            return jsonify({"status": "success", "message": f"Bike {bike} selected"}), 200
        else:
            print("DEBUG: No valid bike received.")
            return jsonify({"status": "error", "message": "No bike selected"}), 400

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
