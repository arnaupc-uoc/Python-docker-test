from functools import wraps
from flask import g, request, abort, current_app as app
from src.models import User
import jwt


def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None
        if "Authorization" in request.headers:
            token = request.headers["Authorization"]
        if not token:
            return {"msg": "Authentication Token is missing!"}, 401
        try:
            data = jwt.decode(token, app.config["SECRET_KEY"], algorithms=["HS256"])
            token_user = User.query.filter_by(id=data["id"], active=1).first()
            if token_user is None:
                return {"msg": "Invalid Authentication token!"}, 401
        except Exception as e:
            return {"msg": "Something went wrong", "error": str(e)}, 500

        g.token_user = token_user
        return f(*args, **kwargs)

    return decorator
