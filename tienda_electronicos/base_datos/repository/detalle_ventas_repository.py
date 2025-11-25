from .base_repository import BaseRepository
class DetalleVentasRepository(BaseRepository):
    def __init__(self, gestor):
        super().__init__(gestor, table="detalle_ventas", id_column="id")
