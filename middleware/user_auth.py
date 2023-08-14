from functools import wraps
from flask import abort, current_app as app, redirect, url_for
from flask_login import current_user


def roles_accepted(*role_names):
    # ensures the current user is logged and has *at least one* of the specified roles
    def wrapper(f):
        @wraps(f)
        def decorator(*args, **kwargs):
            login_manager = app.login_manager

            # User must be logged
            if not current_user.is_authenticated:
                return redirect(url_for(login_manager.login_view))

            # User must have the required roles
            if not current_user.has_roles(role_names):
                abort(403)

            # It's OK to call the view
            return f(*args, **kwargs)

        return decorator

    return wrapper


def roles_required(*role_names):
    # ensures the current user is logged and has *all* of the specified roles
    def wrapper(f):
        @wraps(f)
        def decorator(*args, **kwargs):
            login_manager = app.login_manager

            # User must be logged
            if not current_user.is_authenticated:
                return redirect(url_for(login_manager.login_view))

            # User must have the required roles
            if not current_user.has_roles(*role_names):
                abort(403)

            # It's OK to call the view
            return f(*args, **kwargs)

        return decorator

    return wrapper
