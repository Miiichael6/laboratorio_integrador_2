from tienda_electronicos.base_datos.repository.base_repository import BaseRepository
from tienda_electronicos.base_datos.repository.entities.productos import Producto
class ProductosRepository(BaseRepository[Producto]):
    def __init__(self, gestor):
        super().__init__(gestor, table="productos", id_column="id")
