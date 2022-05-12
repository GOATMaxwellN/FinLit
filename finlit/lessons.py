from flask import Blueprint, render_template

bp = Blueprint("lessons", __name__, url_prefix="/lessons")

@bp.route("/budgeting/")
def budgeting():
    return render_template("lessons/budgeting.html")

@bp.route("/saving/")
def saving():
    return render_template("lessons/saving.html")