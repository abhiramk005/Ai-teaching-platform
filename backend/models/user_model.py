from datetime import datetime

class UserModel:

    @staticmethod
    def create_user(db, name, email, password_hash):
        user = {
            "name": name,
            "email": email,
            "password_hash": password_hash,
            "role": "user",
            "is_verified": False,
            "refresh_token": None,
            "created_at": datetime.utcnow(),
            "last_login": None
        }
        return db.users.insert_one(user)

    @staticmethod
    def find_by_email(db, email):
        return db.users.find_one({"email": email})

    @staticmethod
    def find_by_id(db, user_id):
        from bson import ObjectId
        return db.users.find_one({"_id": ObjectId(user_id)})

    @staticmethod
    def update_refresh_token(db, user_id, refresh_token):
        from bson import ObjectId
        db.users.update_one(
            {"_id": ObjectId(user_id)},
            {"$set": {"refresh_token": refresh_token}}
        )
