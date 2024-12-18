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
    return jsonify(get_current_artifact())

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port, debug=True)