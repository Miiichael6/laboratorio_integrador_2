from .base_repository import BaseRepository
class ProductosRepository(BaseRepository):
    def __init__(self, gestor):
        super().__init__(gestor, table="productos", id_column="id")
