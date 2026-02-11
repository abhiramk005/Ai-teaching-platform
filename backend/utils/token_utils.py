import jwt
import os
from datetime import datetime, timedelta

def generate_access_token(user_id):
    payload = {
        "user_id": str(user_id),
        "exp": datetime.utcnow() + timedelta(seconds=900)
    }
    return jwt.encode(payload, os.getenv("JWT_SECRET"), algorithm="HS256")

def generate_refresh_token(user_id):
    payload = {
        "user_id": str(user_id),
        "exp": datetime.utcnow() + timedelta(days=7)
    }
    return jwt.encode(payload, os.getenv("JWT_SECRET"), algorithm="HS256")

def decode_token(token):
    return jwt.decode(token, os.getenv("JWT_SECRET"), algorithms=["HS256"])
