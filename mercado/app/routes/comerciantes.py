from flask import Blueprint, render_template, request, redirect, url_for
from app.models import Comerciante, db

bp = Blueprint('comerciantes', __name__, url_prefix='/comerciantes')

@bp.route('/')
def index():
    q = request.args.get('buscar', '')
    if q:
        lista = Comerciante.query.filter(
            (Comerciante.nombre.ilike(f'%{q}%')) |
            (Comerciante.cedula.ilike(f'%{q}%'))
        ).all()
    else:
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
            
        )
        db.session.add(nuevo)
        db.session.commit()
        return redirect(url_for('comerciantes.index'))
    return render_template('comerciantes/form.html', comerciante=None)

@bp.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    comerciante = Comerciante.query.get_or_404(id)
    if request.method == 'POST':
        comerciante.nombre = request.form['nombre']
        comerciante.apellido = request.form['apellido']
        comerciante.cedula = request.form['cedula']
        comerciante.direccion = request.form['direccion']
        comerciante.telefono = request.form['telefono']
        db.session.commit()
        return redirect(url_for('comerciantes.index'))
    return render_template('comerciantes/form.html', comerciante=comerciante)

@bp.route('/eliminar/<int:id>')
def eliminar(id):
    comerciante = Comerciante.query.get_or_404(id)
    db.session.delete(comerciante)
    db.session.commit()
    return redirect(url_for('comerciantes.index'))

@bp.route('/catastro')
def catastro():
    return render_template('comerciantes/catastro.html')

@bp.route('/api/<cedula>')
def buscar_por_cedula(cedula):
    c = Comerciante.query.filter_by(cedula=cedula).first()
    if c:
        return {
            'nombre': c.nombre,
            'apellido': c.apellido
        }
    return {}, 404


