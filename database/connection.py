import sqlite3
from sqlite3 import Error

def create_connection():
  conn = None 
  
  try:
    # la funcion connect cumple la función de abrir la conexión con la base de datos y crea una base de datos
    conn = sqlite3.connect('database/tasks.db')
  except Error as e:
    print('Error connecting to database:', str(e))
  return conn