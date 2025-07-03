from flask import redirect, url_for, render_template
from app import create_app

app = create_app()

@app.route('/')
def inicio():
    return render_template('inicio.html')
