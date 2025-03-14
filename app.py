from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()  # This ensures Flask reads JSON data
    if not data:
        return jsonify({"error": "Invalid JSON data"}), 400
    return jsonify({"message": "Success", "received": data})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)  # Required for deployment