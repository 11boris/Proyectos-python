from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models import Comerciante, db

bp = Blueprint('comerciantes', __name__, url_prefix='/comerciantes')

@bp.route('/')
def index():
    buscar = request.args.get('buscar', '')
    if buscar:
        comerciantes = Comerciante.query.filter(
            (Comerciante.nombre.ilike(f'%{buscar}%')) |
            (Comerciante.cedula.ilike(f'%{buscar}%'))
        ).all()
    else:
        comerciantes = Comerciante.query.all()
    return render_template('comerciantes/index.html', comerciantes=comerciantes)

@bp.route('/nuevo', methods=['GET', 'POST'])
def nuevo():
    if request.method == 'POST':
        nuevo = Comerciante(
            nombre=request.form.get('nombre'),
            apellido=request.form.get('apellido'),
            cedula=request.form.get('cedula'),
            direccion=request.form.get('direccion'),
            telefono=request.form.get('telefono')
        )
        db.session.add(nuevo)
        db.session.commit()
        return redirect(url_for('comerciantes.index'))
    return render_template('comerciantes/form.html', comerciante=None)

@bp.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    comerciante = Comerciante.query.get_or_404(id)
    if request.method == 'POST':
        comerciante.nombre = request.form.get('nombre')
        comerciante.apellido = request.form.get('apellido')
        comerciante.cedula = request.form.get('cedula')
        comerciante.direccion = request.form.get('direccion')
        comerciante.telefono = request.form.get('telefono')
        db.session.commit()
        return redirect(url_for('comerciantes.index'))
    return render_template('comerciantes/form.html', comerciante=comerciante)

@bp.route('/eliminar/<int:id>')
def eliminar(id):
    comerciante = Comerciante.query.get_or_404(id)
    db.session.delete(comerciante)
    db.session.commit()
    return redirect(url_for('comerciantes.index'))

@bp.route('/api/<cedula>')
def buscar_por_cedula(cedula):
    c = Comerciante.query.filter_by(cedula=cedula).first()
    if c:
        return jsonify({'nombre': c.nombre, 'apellido': c.apellido})
    return jsonify({}), 404
