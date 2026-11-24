from flask import Blueprint, render_template, abort
from models.user import User

user_bp = Blueprint("user", __name__, url_prefix="/users")


@user_bp.route("/")
def list_users():
    return render_template("user/list.html", users=User.get_all())


@user_bp.route("/<int:id>")
def view_user(id):
    user = User.get_by_id(id)
    if user is None:
        abort(404)
    return render_template("user/profile.html", user=user)
