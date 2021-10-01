# $env:FLASK_APP = archivo.py en PowerShell
# $env:FLASK_ENV = "development" en PowerShell

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hola mundo flask"

@app.route('/articulos/')
def articulos():
    return "Lista de articulos nuevos"

@app.route('/articulos/<int:id>')
def ver_articulos(id):
    return "Vamos a mostrar el articulo con el id {}".format(id)

@app.route('/hello')
@app.route('/hello/<string:nombre>/')
@app.route('/hello/<string:nombre>/<int:edad>')

def hola(nombre=None, edad=None):
    if nombre and edad:
        return "Hola, {0} tienes {1} años.".format(nombre, edad)
    elif nombre:
        return "Hola, {0}".format(nombre)
    else:
        return "Hola Mundo"
