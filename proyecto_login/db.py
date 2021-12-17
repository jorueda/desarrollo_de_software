import sqlite3

def sqlconnection():
    connection = sqlite3.connect('database.db')
    return connection

def get_db(connection):
    connection = connection.sql_connection()

def close_db(connection):
    connection.close()
