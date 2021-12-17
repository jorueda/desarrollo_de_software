import os
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import AnyOf, DataRequired, InputRequired, Length, input_required
from wtforms.widgets.core import Input

app = Flask(__name__)
# secret_key = os.urandom(24)
app.config['SECRET_KEY'] = "Llavesecreta"


@app.route('/', methods=['GET', 'POST'])
def form():
    form = login_form()
    if form.validate_on_submit():
        return '<h1> The username is {}. The password is {}.'.format(form.username.data, form.password.data)

    return render_template('form.html', form=form)


class login_form(FlaskForm):
    username = StringField('username', validators=[InputRequired("El usuario es requerido."),
                                                Length(min=5, max=10, message="Debe ingresar entre 5 y 10 caracteres.")])
    password = PasswordField('password', validators=[InputRequired("La contraseña es requerida."),
                                                AnyOf(values=['password', 'secret'])])


if __name__ == '__main__':
    app.run(debug=True)
