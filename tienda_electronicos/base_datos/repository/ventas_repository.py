from tienda_electronicos.base_datos.repository.base_repository import BaseRepository
from tienda_electronicos.base_datos.repository.entities.ventas import Venta
class VentasRepository(BaseRepository[Venta]):
    def __init__(self, gestor):
        super().__init__(gestor, table="ventas", id_column="id")
