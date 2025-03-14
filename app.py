from flask import request, jsonify

def bike_selection():
    try:
        data = request.get_json()
        print(f"Raw incoming data: {data}")  # Debugging

        bike = data.get("bike", "").strip().lower()  # Ensure proper string handling

        if bike and bike != "none":
            print(f"Extracted bike selection: {bike}")
            return jsonify({"status": "success", "message": f"Bike {bike} selected"}), 200
        else:
            print("DEBUG: No valid bike received.")
            return jsonify({"status": "error", "message": "No bike selected"}), 400

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
