from tienda_electronicos.base_datos.repository.base_repository import BaseRepository
from tienda_electronicos.base_datos.repository.entities.detalle_ventas import DetalleVenta
class DetalleVentasRepository(BaseRepository[DetalleVenta]):
    def __init__(self, gestor):
        super().__init__(gestor, table="detalle_ventas", id_column="id")
