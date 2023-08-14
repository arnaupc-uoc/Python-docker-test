from functools import wraps
from flask import request, abort, current_app as app
from src.models import User
import jwt


def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None
        if "Authorization" in request.headers:
            token = request.headers["Authorization"]
        if not token:
            return {"message": "Authentication Token is missing!", "data": None, "error": "Unauthorized"}, 401
        try:
            data = jwt.decode(token, app.config["SECRET_KEY"], algorithms=["HS256"])
            token_user = User.query.filter_by(id=data["id"], active=1).first()
            if token_user is None:
                return {"message": "Invalid Authentication token!", "data": None, "error": "Unauthorized"}, 401
        except Exception as e:
            return {"message": "Something went wrong", "data": None, "error": str(e)}, 500

        return f(token_user, *args, **kwargs)

    return decorator
