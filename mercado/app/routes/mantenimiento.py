from flask import Blueprint, render_template

bp = Blueprint('mantenimiento', __name__, url_prefix='/mantenimiento')

@bp.route('/')
def index():
    return render_template('mantenimiento/index.html')
