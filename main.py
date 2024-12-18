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
    artifact = get_current_artifact()
    # Format specifically for TRMNL display
    display_data = {
        "artifact": {
            "year": str(artifact["year"]),
            "number": str(artifact["artifact_number"]).zfill(3),
            "title": artifact["title"],
            "description": artifact["description"],
            "didYouKnow": artifact["fun_fact"]
        },
        "display": {
            "layout": "digital-archaeologist",
            "font": "monospace"
        }
    }
    return jsonify(display_data)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port, debug=True)