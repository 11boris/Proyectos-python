from flask import Blueprint, render_template, request, redirect, url_for
from app.models import Catastro, Comerciante, db
from datetime import datetime

bp = Blueprint('catastro', __name__, url_prefix='/catastro')

@bp.route('/', methods=['GET', 'POST'])
def registrar():
    if request.method == 'POST':
        cedula = request.form['cedula']
        comerciante = Comerciante.query.filter_by(cedula=cedula).first()

        if not comerciante:
            return "Comerciante no encontrado", 400

        nuevo = Catastro(
            fecha=datetime.strptime(request.form['fecha'], '%Y-%m-%d'),
            cedula=cedula,
            fecha_nacimiento=datetime.strptime(request.form['fecha_nacimiento'], '%Y-%m-%d'),
            actividad=request.form['actividad'],
            plaza=request.form['plaza'],
            puesto=request.form['puesto'],
            referencia1_nombre=request.form['ref1_nombre'],
            referencia1_apellido=request.form['ref1_apellido'],
            referencia1_telefono=request.form['ref1_telefono'],
            referencia1_parentesco=request.form['ref1_parentesco'],
            referencia2_nombre=request.form['ref2_nombre'],
            referencia2_apellido=request.form['ref2_apellido'],
            referencia2_telefono=request.form['ref2_telefono'],
            referencia2_parentesco=request.form['ref2_parentesco']
        )

        db.session.add(nuevo)
        db.session.commit()
        return redirect(url_for('catastro.listar'))

    return render_template('comerciantes/catastro.html')

@bp.route('/listar')
def listar():
    registros = Catastro.query.all()
    return render_template('comerciantes/lista_catastro.html', catastros=registros)
