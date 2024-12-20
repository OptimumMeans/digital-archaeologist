from flask import Flask, jsonify
from generate_facts import get_current_artifact
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Digital Archaeologist API is running!"

@app.route('/api/artifact')
def get_artifact():
    try:
        artifact = get_current_artifact()
        # Return flattened structure
        return jsonify({
            "artifact_name": artifact["title"],
            "description": artifact["description"],
            "fun_fact": artifact["fun_fact"],
            "number": f"#{str(artifact['artifact_number']).zfill(3)}",
            "year": str(artifact["year"])
        })
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port, debug=True)