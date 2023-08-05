from flask import Blueprint, render_template, redirect, url_for
from flask_user import roles_required, current_user, login_required

bp = Blueprint('admin', __name__, template_folder='../../templates/admin', static_folder='../../static/admin', url_prefix='/admin')

# Admin routes

@bp.route('/')
def main():
    # check is logged and redirect
    if current_user.is_authenticated:
        return redirect(url_for('admin.dashboard'))
    else:
        return redirect('/admin/login')


@bp.route('/dashboard')
# @login_required
@roles_required('Admin')
def dashboard():
    return render_template(
        'dashboard.html',
        title='Dashboard'
    )

# Error handlers
@bp.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('error.html'), 404