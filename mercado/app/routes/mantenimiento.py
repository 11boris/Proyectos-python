from flask import Blueprint, render_template

bp = Blueprint('mantenimiento', __name__, url_prefix='/mantenimiento')

@bp.route('/preventivo')
def preventivo():
    return render_template('mantenimiento/preventivo.html')

@bp.route('/ejecutado')
def ejecutado():
    return render_template('mantenimiento/ejecutado.html')
