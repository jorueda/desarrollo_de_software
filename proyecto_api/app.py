from flask import Flask, json, jsonify
from articulos import articulos

app = Flask(__name__)

@app.route('/')
def api():
    return jsonify({'message': "Hola, mundo!"})

@app.route('/articulos/') # Colocar siempre / al final
def getArticulos():
    return jsonify({'Todos los articulos': articulos})

@app.route('/articulos/<string:nombre_articulo>')
def getArticulo(nombre_articulo):
    encontrado = [articulo for articulo in articulos if articulo['nombre'] == nombre_articulo]
    return jsonify({'articulo': encontrado[0]})
