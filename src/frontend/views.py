from flask import Blueprint, render_template, redirect, url_for, abort
from app import cache
from src.frontend.forms.contact import ContactForm


bp = Blueprint(
    "frontend",
    __name__,
    template_folder="../../templates/frontend",
    static_folder="../../static/frontend"
)


# Frontend routes


@bp.route("/")
@cache.cached(timeout=10)
def main():
    form = ContactForm()
    return render_template(
        "frontend/main.html",  # from templates folder
        title="Jinja Demo Site",
        content="Smarter page templates with Flask & Jinja.",
        form=form,
    )


@bp.route("/send-form", methods=["POST"])
def send_form():
    form = ContactForm()
    if form.validate_on_submit():
        # data = request.form.to_dict();
        print("Send Form!")
        return redirect(url_for("frontend.main"))
    else:
        abort(500, "Form validation failed!")


@bp.route("/error")
def error():
    code = 404
    message = "There's an error!"
    abort(code, message)


# Error handlers
@bp.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template("frontend/error.html"), 404
