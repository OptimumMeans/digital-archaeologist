from flask import Flask, jsonify
from generate_facts import get_current_artifact
from flask_cors import CORS  # Add CORS support

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes


@app.route('/')
def home():
    return "Digital Archaeologist API is running!"


@app.route('/api/artifact')
def get_artifact():
    return jsonify(get_current_artifact())


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
