
from database import conectar
from models.tarea import Tarea

class GestorTareas:
    def agregar_tarea(self, usuario_id, descripcion, categoria):
        """Agrega una nueva tarea para un usuario."""
        with conectar() as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO tareas (usuario_id, descripcion, categoria) VALUES (?, ?, ?)",
                           (usuario_id, descripcion, categoria))
            conn.commit()

    def obtener_tareas(self, usuario_id):
        """Obtiene todas las tareas de un usuario."""
        with conectar() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM tareas WHERE usuario_id = ?", (usuario_id,))
            return cursor.fetchall()

    def actualizar_tarea(self, tarea_id, estado):
        """Actualiza el estado de una tarea."""
        with conectar() as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE tareas SET estado = ? WHERE id = ?", (estado, tarea_id))
            conn.commit()

    def eliminar_tarea(self, tarea_id):
        """Elimina una tarea."""
        with conectar() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM tareas WHERE id = ?", (tarea_id,))
            conn.commit()
