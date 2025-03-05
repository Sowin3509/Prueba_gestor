import sqlite3
from database import conectar
from models.usuario import Usuario

class GestorUsuarios:
    def registrar_usuario(self, username, password):
        """Registra un nuevo usuario."""
        with conectar() as conn:
            cursor = conn.cursor()
            try:
                cursor.execute("INSERT INTO usuarios (username, password) VALUES (?, ?)", (username, password))
                conn.commit()
                return True
            except sqlite3.IntegrityError:
                return False  # Usuario ya existe

    def autenticar_usuario(self, username, password):
        """Verifica si un usuario existe con la contraseña correcta."""
        with conectar() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id FROM usuarios WHERE username = ? AND password = ?", (username, password))
            usuario = cursor.fetchone()
            return usuario[0] if usuario else None  # Retorna el ID si es válido, sino None