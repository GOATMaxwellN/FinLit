from flask import Blueprint, render_template

bp = Blueprint("lessons", __name__, url_prefix="/lessons")

@bp.route("/budgeting-and-saving/")
def budgeting_and_saving():
    return render_template("lessons/budgeting_and_saving.html")