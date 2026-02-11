from flask import Blueprint, request, jsonify, make_response
from models.user_model import UserModel
from utils.password_utils import hash_password, verify_password
from utils.token_utils import generate_access_token, generate_refresh_token, decode_token
from datetime import datetime

auth_bp = Blueprint("auth", __name__)

def set_auth_cookies(response, access_token, refresh_token):
    response.set_cookie(
        "access_token",
        access_token,
        httponly=True,
        samesite="Lax"
    )
    response.set_cookie(
        "refresh_token",
        refresh_token,
        httponly=True,
        samesite="Lax"
    )

@auth_bp.route("/signup", methods=["POST"])
def signup():
    from app import db

    data = request.json
    name = data.get("name")
    email = data.get("email")
    password = data.get("password")

    if UserModel.find_by_email(db, email):
        return jsonify({"error": "Email already exists"}), 400

    password_hash = hash_password(password)

    result = UserModel.create_user(db, name, email, password_hash)

    access_token = generate_access_token(result.inserted_id)
    refresh_token = generate_refresh_token(result.inserted_id)

    UserModel.update_refresh_token(db, result.inserted_id, refresh_token)

    response = make_response({"message": "Signup successful"})
    set_auth_cookies(response, access_token, refresh_token)

    return response


@auth_bp.route("/login", methods=["POST"])
def login():
    from app import db

    data = request.json
    email = data.get("email")
    password = data.get("password")

    user = UserModel.find_by_email(db, email)

    if not user or not verify_password(password, user["password_hash"]):
        return jsonify({"error": "Invalid credentials"}), 401

    access_token = generate_access_token(user["_id"])
    refresh_token = generate_refresh_token(user["_id"])

    UserModel.update_refresh_token(db, user["_id"], refresh_token)

    response = make_response({"message": "Login successful"})
    set_auth_cookies(response, access_token, refresh_token)

    return response

@auth_bp.route("/me", methods=["GET"])
def get_current_user():
    from app import db

    access_token = request.cookies.get("access_token")

    if not access_token:
        return {"error": "Unauthorized"}, 401

    try:
        payload = decode_token(access_token)
        user_id = payload["user_id"]

        user = UserModel.find_by_id(db, user_id)

        if not user:
            return {"error": "User not found"}, 404

        return {
            "user": {
                "id": str(user["_id"]),
                "name": user["name"],
                "email": user["email"],
                "role": user["role"]
            }
        }

    except Exception:
        return {"error": "Invalid token"}, 401