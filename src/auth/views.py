from flask import Blueprint, render_template, redirect, url_for, request, flash, abort
from src.models import User
from werkzeug.security import check_password_hash
from src.auth.forms import LoginForm
from flask_login import login_user, logout_user, current_user


bp = Blueprint(
    'auth',
    __name__,
    template_folder="../../templates/auth",
    static_folder="../../static/auth",
    url_prefix='/auth'
)


@bp.route('/login', methods=['GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("admin.dashboard"))
    form = LoginForm()
    return render_template('auth/login.html', form=form)


@bp.route('/login', methods=['POST'])
def login_post():
    form = LoginForm()
    if form.validate_on_submit():
        # login code goes here
        email = request.form.get('email')
        password = request.form.get('password')
        remember = True if request.form.get('remember') else False

        # check if the user actually exists
        user = User.query.filter_by(email=email).first()
        if not user or not check_password_hash(user.password, password):
            flash('Please check your login details and try again.')
            return redirect(url_for('auth.login'))
        
        login_user(user, remember=remember)
        print(user)
        return redirect(url_for("admin.dashboard"))

    else:
        abort(500, "Form validation failed!")


@bp.route('/logout', methods=['GET'])
def logout():
    logout_user()
    return redirect(url_for("auth.login"))
