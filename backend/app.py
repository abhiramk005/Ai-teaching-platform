from flask import Flask
from flask_cors import CORS
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# -------------------------
# Load environment variables
# -------------------------
load_dotenv()

mongo_uri = os.getenv("MONGO_URI")

if not mongo_uri:
    raise ValueError("❌ MONGO_URI not found in .env file")

# -------------------------
# Initialize Flask App
# -------------------------
app = Flask(__name__)

# Enable CORS for React frontend
CORS(app, supports_credentials=True,origins=["http://localhost:3000"])

# -------------------------
# MongoDB Connection
# -------------------------
try:
    client = MongoClient(mongo_uri)
    db = client["ai_learning_app"]  # Explicit DB selection
    print("✅ Connected to MongoDB Atlas")
except Exception as e:
    print("❌ MongoDB Connection Failed:", e)
    raise e

from routes.auth_routes import auth_bp

app.register_blueprint(auth_bp, url_prefix="/api/auth")

# -------------------------
# Test Route
# -------------------------
@app.route("/")
def home():
    return {"message": "Backend running successfully"}

# -------------------------
# Run Server
# -------------------------
if __name__ == "__main__":
    app.run(debug=True)
