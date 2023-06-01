from functools import wraps

import jwt
from flask import current_app
from flask import request

from .models import Users


def login_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        token = None
        if "Authorization" in request.headers:
            token = request.headers["Authorization"]
        if not token:
            return {
                       "message": "Unauthorized"
                   }, 401
        try:
            user_id = jwt.decode(
                token,
                current_app.config["SECRET_KEY"],
                algorithms=["HS256"])["user_id"]

            user_obj = Users.query.filter_by(id_=user_id).scalar()
            if not user_obj:
                return {
                           "message": "This account is blocked"
                       }, 403
            return func(user_obj, *args, **kwargs)
            # return func(*args, **kwargs)
        except Exception as e:
            print(f"exception ==> {e}")
            return {
                       "message": "Unauthorized"
                   }, 403
    return decorated
