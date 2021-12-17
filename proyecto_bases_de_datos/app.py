from flask import Flask, render_template, request, flash, redirect, url_for
import sqlite3

app = Flask(__name__)
app.secret_key = "Llavesecreta"

def sql_connection():
    connection = sqlite3.connect('agenda.db')
    return connection

@app.route('/')
def index():
    connection = sql_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM contactos')
    data = cursor.fetchall()
    return render_template('index.html', contacts=data)

@app.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        fullname = request.form['fullname']
        email = request.form['email']
        phone = request.form['phone']
        connection = sql_connection()
        cursor = connection.cursor()
        statement = 'INSERT INTO contactos (fullname, email, phone) VALUES (?,?,?)'
        cursor.execute(statement, [fullname, email, phone])
        connection.commit()
        flash("Contact added successfully")
        return redirect(url_for('index'))

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_contact(id):
    connection = sql_connection()
    cursor = connection.cursor()
    consulta = "SELECT * FROM contactos WHERE id=?"
    cursor = cursor.execute(consulta, [id])
    data = cursor.fetchone()
    cursor.close()
    return render_template('edit.html', contacts = data)

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_contact(id):
    if request.method == 'POST':
        connection = sql_connection()
        cursor = connection.cursor()
        fullname = request.form['fullname']
        email = request.form['email']
        phone = request.form['phone']
        consulta = "UPDATE contactos SET fullname=?, email=?, phone=? WHERE id=?"
        cursor = cursor.execute(consulta, [fullname, email, phone, id])
        connection.commit()
        cursor.close()
        flash("Contact updated successfully")
        return redirect(url_for('index'))

@app.route('/delete/<int:id>', ) # Default es GET
def delete_contact(id):
    connection = sql_connection()
    cursor = connection.cursor()
    cursor. execute('DELETE FROM contactos WHERE id={}'.format(id))
    connection.commit()
    flash("Contact deleted successfully")
    return redirect(url_for('index'))
