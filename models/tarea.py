class Tarea:
    def __init__(self, id, usuario_id, descripcion, categoria, estado="Pendiente"):
        self.id = id
        self.usuario_id = usuario_id
        self.descripcion = descripcion
        self.categoria = categoria
        self.estado = estado
