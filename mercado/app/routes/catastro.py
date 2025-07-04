@bp.route('/verificar/<cedula>')
def verificar_catastro(cedula):
    existe = Catastro.query.filter_by(cedula=cedula).first()
    return {'catastrado': bool(existe)}
