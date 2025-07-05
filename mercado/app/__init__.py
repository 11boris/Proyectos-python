from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('../config.py')

    db.init_app(app)

    # Importación de blueprints desde app.routes
    from app.routes import comerciantes, mantenimiento, reportes, catastro

    # Registro de blueprints
    app.register_blueprint(comerciantes.bp)
    app.register_blueprint(mantenimiento.bp)
    app.register_blueprint(reportes.bp)
    app.register_blueprint(catastro.bp)

    return app
