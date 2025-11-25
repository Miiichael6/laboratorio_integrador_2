from .base_repository import BaseRepository
class ClientesRepository(BaseRepository):
    def __init__(self, gestor):
        super().__init__(gestor, table="clientes", id_column="id")
