from flask import Blueprint, render_template, jsonify, render_template, request, redirect, url_for, abort
from flask_assets import Bundle, Environment

bp = Blueprint('frontend', __name__, template_folder='templates', static_folder='static', url_prefix='')

# Frontend routes

@bp.route("/")
def main():
    return render_template(
        'main.html',  # from templates folder
        title='Jinja Demo Site',
        content='Smarter page templates with Flask & Jinja.'
    )
    # return "Hello World!"

@bp.route('/send-form', methods=['POST'])
def send_form():
    data = request.form.to_dict();
    print('Send Form!')
    return redirect(url_for('frontend.main'))
    #return jsonify({"msg": "Form send."})

@bp.route("/error")
def error():
    code = 404
    message = 'There\'s an error!'
    abort(code, message)

# Error handlers
@bp.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('error.html'), 404