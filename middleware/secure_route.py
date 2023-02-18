from http import HTTPStatus
from functools import wraps
from flask import request, g
import jwt
from config.environment import secret
from models.users import UserModel

def secure_route(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        raw_token = request.headers.get('Authorization')
        if not raw_token:
            return { "message": "Unauthorized" }, HTTPStatus.UNAUTHORIZED
        
        clean_token = raw_token.replace("Bearer ", "")

        try:
            payload = jwt.decode(
                clean_token,
                secret,
                "HS256"
            )
            user_id = payload['sub']
            user = UserModel.query.get(user_id)

            if not user:
                return { "message": "Unauthorized" }, HTTPStatus.UNAUTHORIZED
            
            g.current_user = user

        except jwt.ExpiredSignatureError:
            return { "message": "Unauthorized" }, HTTPStatus.UNAUTHORIZED
        except Exception:
            return { "message": "Unauthorized" }, HTTPStatus.UNAUTHORIZED
        return func(*args, **kwargs)
    return wrapper