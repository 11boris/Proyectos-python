from flask import Blueprint, render_template, request, redirect, url_for
from app.models import Comerciante, db

bp = Blueprint('comerciantes', __name__, url_prefix='/comerciantes')

@bp.route('/')
def index():
    lista = Comerciante.query.all()
    return render_template('comerciantes/index.html', comerciantes=lista)

@bp.route('/nuevo', methods=['GET', 'POST'])
def nuevo():
    if request.method == 'POST':
        nuevo = Comerciante(
            nombre=request.form['nombre'],
            apellido=request.form['apellido'],
            cedula=request.form['cedula'],
            direccion=request.form['direccion'],
            telefono=request.form['telefono'],
            rubro=request.form['rubro'],
            puesto=request.form['puesto']
        )
        db.session.add(nuevo)
        db.session.commit()
        return redirect(url_for('comerciantes.index'))
    return render_template('comerciantes/form.html')

