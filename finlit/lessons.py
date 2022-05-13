from flask import Blueprint, render_template

bp = Blueprint("lessons", __name__, url_prefix="/lessons")

@bp.route("/budgeting/")
def budgeting():
    return render_template("lessons/budgeting.html")

@bp.route("/saving/")
def saving():
    return render_template("lessons/saving.html")

@bp.route("/debt/")
def debt():
    return render_template("lessons/debt.html")

@bp.route("/credit-cards/")
def credit_cards():
    return render_template("lessons/credit-cards.html")

@bp.route("/line-of-credit/")
def line_of_credit():
    return render_template("lessons/line-of-credit.html")

@bp.route("/mortgage/")
def mortgage():
    return render_template("lessons/mortgage.html")
