import sqlite3

DB_NAME = "gestor_tareas.db"

def conectar():
    """Establece conexión con la base de datos."""
    return sqlite3.connect(DB_NAME)

def crear_tablas():
    """Crea las tablas necesarias en la base de datos."""
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tareas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                usuario_id INTEGER NOT NULL,
                descripcion TEXT NOT NULL,
                categoria TEXT NOT NULL,
                estado TEXT DEFAULT 'Pendiente',
                FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
            )
        """)
        conn.commit()

# Crear las tablas al iniciar
crear_tablas()
