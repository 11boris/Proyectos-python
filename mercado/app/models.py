from . import db

class Comerciante(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=False)
    cedula = db.Column(db.String(10), unique=True, nullable=False)
    direccion = db.Column(db.String(150), nullable=True)
    telefono = db.Column(db.String(15), nullable=True)
    rubro = db.Column(db.String(50), nullable=False)
    puesto = db.Column(db.String(20), nullable=False)
    activo = db.Column(db.Boolean, default=True)
