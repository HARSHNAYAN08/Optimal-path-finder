from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os

# Load environment variables from .env file (for local testing)
load_dotenv()

# Flask application instance
app = Flask(__name__)

# Example environment variable usage
API_KEY = os.getenv("API_KEY", "default_api_key")
ORS_API_KEY = os.getenv("ORS_API_KEY", "default_ors_api_key")

@app.route('/')
def home():
    return "Welcome to the Optimal Path API deployed on Vercel!"

@app.route('/api/predict', methods=['POST'])
def predict():
    # Example API endpoint for prediction
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid input, JSON expected"}), 400

    # Process input data (example)
    try:
        start_location = data['start']
        end_location = data['end']

        # Replace this with actual logic
        result = {
            "start": start_location,
            "end": end_location,
            "shortest_path": ["CityA", "CityB", "CityC"],  # Example path
            "pollution": 42,  # Example pollution score
            "crime_score": 15,  # Example crime score
            "total_weight": 57  # Example weighted score
        }

        return jsonify(result)
    except KeyError as e:
        return jsonify({"error": f"Missing key: {str(e)}"}), 400

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "OK"})

# Make sure this is exposed for Vercel
if __name__ == '__main__':
    app.run(debug=True)

