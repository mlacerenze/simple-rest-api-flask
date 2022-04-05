-- Aquí van los quieries de la tabla de tareas

CREATE TABLE IF NOT EXISTS tasks(
  id INTEGER PRIMARY KEY,
  title TEXT NOT NULL,
  created_date TEXT NOT NULL,
  completed BOOLEAN NOT NULL DEFAULT 0
)