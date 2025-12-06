from tienda_electronicos.base_datos.repository.base_repository import BaseRepository
from tienda_electronicos.base_datos.repository.entities.cliente import Cliente
class ClientesRepository(BaseRepository[Cliente]):
    def __init__(self, gestor):
        super().__init__(gestor, table="clientes", id_column="id")
