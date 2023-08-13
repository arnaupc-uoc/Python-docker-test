from functools import wraps
from flask import request, abort, current_app as app
from flask_login import current_user
from src.models import User


def roles_accepted(*role_names):
    # ensures the current user is logged and has *at least one* of the specified roles (OR operation)
    def wrapper(f):
        @wraps(f)    # Tells debuggers that is is a function wrapper
        def decorator(*args, **kwargs):
            user_manager = app.user_manager

            # User must be logged
            allowed = _is_logged_in_with_confirmed_email(user_manager)
            if not allowed:
                # Redirect to unauthenticated page
                return user_manager.unauthenticated_view()

            # User must have the required roles
            if not current_user.has_roles(role_names):
                # Redirect to the unauthorized page
                return user_manager.unauthorized_view()

            # It's OK to call the view
            return f(*args, **kwargs)

        return decorator

    return wrapper


def roles_required(*role_names):
    # ensures the current user is logged and has *all* of the specified roles (OR operation)
    def wrapper(f):
        @wraps(f)
        def decorator(*args, **kwargs):
            user_manager = app.user_manager

            # User must be logged in with a confirmed email address
            allowed = _is_logged_in_with_confirmed_email(user_manager)
            if not allowed:
                # Redirect to unauthenticated page
                return user_manager.unauthenticated_view()

            # User must have the required roles
            if not current_user.has_roles(*role_names):
                # Redirect to the unauthorized page
                return user_manager.unauthorized_view()

            # It's OK to call the view
            return f(*args, **kwargs)

        return decorator

    return wrapper
