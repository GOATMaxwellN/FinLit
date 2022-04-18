from flask import Blueprint, render_template

bp = Blueprint("dashboard", __name__)

@bp.route("/dashboard/")
def dashboard():
    return render_template("dashboard/dashboard.html")