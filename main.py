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
    # Structure the response exactly as TRMNL expects
    display_data = {
        "content": {
            "year": str(artifact["year"]),  # The large number at top
            "artifact_name": artifact["title"],  # The title/name of the artifact
            "description": artifact["description"],
            "fun_fact": artifact["fun_fact"],
            "number": f"#{str(artifact['artifact_number']).zfill(3)}"  # Formats as #001, #002, etc.
        },
        "meta": {
            "type": "digital-archaeologist",
            "display": {
                "font": "monospace",
                "layout": "standard"
            }
        }
    }
    return jsonify(display_data)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port, debug=True)