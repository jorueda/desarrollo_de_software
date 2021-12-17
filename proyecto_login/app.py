import os
from werkzeug.utils import redirect
import yagmail as yagmail
from flask import Flask, render_template, flash, request
import utils
from db import sqlconnection

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/')
def index():
    return render_template("register.html")

@app.route('/login/')
def login():
    return render_template('login.html')

@app.route('/register', methods=('GET', 'POST'))
def register():
    try:
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            correo = request.form['correo']

            error = None
            if not utils.isUsernameValid(username):
                error = "El usuario debe ser alfanumérico."
                flash(error)
                return render_template('login.html')
            if not utils.isPasswordValid(password):
                error = "La contraseña debe tener al menos una minúscula."
                flash(error)
                return render_template('login.html')
            if not utils.isEmailValid(correo):
                error = "Correo inválido."
                flash(error)
                return render_template('login.html')

            user = sqlconnection.execute("SELECT * FROM usuario WHERE usuario=? and password=?", (username, password))
            user = user.fetchone()
            if user is None:
                error = "Usuario y contraseña no válidos."
            else:
                return redirect('mensaje')

            yag = yagmail.SMTP('uninortegrupo6@gmail.com', '%Grupo6%')
            yag.send(to=correo, subject="Activa tu cuenta",
            contents = "Bienvenido, usa este link para activar tu cuenta.")
            flash("Revisa tu correo electrónico para activar tu cuenta.")
            return render_template('login.html')
    except:
        return render_template('register.html')
