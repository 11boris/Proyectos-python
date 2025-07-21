from . import db

# Comerciantes
class Comerciante(db.Model):
    __tablename__ = 'comerciantes'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=False)
    cedula = db.Column(db.String(10), unique=True, nullable=False)
    direccion = db.Column(db.String(150), nullable=True)
    telefono = db.Column(db.String(15), nullable=True)
    activo = db.Column(db.Boolean, default=True)

    catastros = db.relationship('Catastro', backref='comerciante', lazy=True)

# Catastro de comerciantes
class Catastro(db.Model):
    __tablename__ = 'catastros'

    id = db.Column(db.Integer, primary_key=True)
    cedula = db.Column(db.String(10), db.ForeignKey('comerciantes.cedula'), nullable=False)
    fecha = db.Column(db.Date, nullable=False)
    fecha_nacimiento = db.Column(db.Date, nullable=False)
    actividad = db.Column(db.String(100), nullable=False)
    plaza = db.Column(db.String(100), nullable=False)
    puesto = db.Column(db.String(20), nullable=False)
    referencia1_nombre = db.Column(db.String(100))
    referencia1_apellido = db.Column(db.String(100))
    referencia1_telefono = db.Column(db.String(20))
    referencia1_parentesco = db.Column(db.String(50))
    referencia2_nombre = db.Column(db.String(100))
    referencia2_apellido = db.Column(db.String(100))
    referencia2_telefono = db.Column(db.String(20))
    referencia2_parentesco = db.Column(db.String(50))
