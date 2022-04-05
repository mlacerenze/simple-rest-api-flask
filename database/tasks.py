import sqlite3 
from sqlite3 import Error

from .connection import create_connection

def insert_task(data):
  conn = create_connection()
  
  sql = """ INSERT INTO tasks (title, created_date)
            VALUES (?, ?)
  """
  
  try: 
    cur = conn.cursor()
    cur.execute(sql, data)
    conn.commit()
    return cur.lastrowid
  except Error as e:
    print('Error inserting task:', str(e))
    return False 
  finally:
    if conn:
      cur.close()
      conn.close()
      

def select_task_by_id(_id):
  conn = create_connection()
  
  sql = f" SELECT * FROM tasks WHERE id = {_id}"
  
  try: 
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute(sql)
    task = dict(cur.fetchone()) # fetchone trae un solo valor en una tupla
    return task 
  except Error as r:
    print('Error selecting task:', str(r))
    return False 
  finally:
    if conn:
      cur.close()
      conn.close()
      
      
def select_all_tasks():
  conn = create_connection()
  
  sql = " SELECT * FROM tasks "
  
  try: 
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute(sql)
    task_row = cur.fetchall()
    tasks = [ dict(row)for row in task_row ] # convierto cada tupla en un diccionario
    return tasks 
  except Error as r:
    print('Error selecting all tasks:', str(r))
    return False 
  finally:
    if conn:
      cur.close()
      conn.close()
      

def update_task(_id, data):
  conn = create_connection()
  
  sql = f""" UPDATE tasks SET title = ?
            WHERE id = {_id}
  """
  
  try: 
    cur = conn.cursor()
    cur.execute(sql, data)
    conn.commit()
    return True
  except Error as e:
    print('Error updating task:', str(e))
    return False 
  finally:
    if conn:
      cur.close()
      conn.close()
      

def delete_task(_id):
  conn = create_connection()
  
  sql = f" DELETE FROM tasks WHERE id = {_id}"
  
  try: 
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    return True
  except Error as e:
    print('Error deleting task:', str(e))
    return False 
  finally:
    if conn:
      cur.close()
      conn.close()
      
      
def complete_task(_id, completed):
  conn = create_connection()
  
  sql = f" UPDATE tasks SET completed = {completed} WHERE id = {_id}"
  
  try: 
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    return True
  except Error as e:
    print('Error completing task:', str(e))
    return False 
  finally:
    if conn:
      cur.close()
      conn.close()