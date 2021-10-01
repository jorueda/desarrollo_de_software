from flask import Flask, render_template, request, flash
import utils

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("formularioClase.html")

@app.route('/login/')
def login():
    return render_template('login.html')

@app.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        correo = request.form['correo']
        # if not utils.isUsernameValid(username):
        #     error = "El usuario debe ser alfanumérico."
        #     flash(error)
        #     return render_template()
        return render_template('respuesta.html')
