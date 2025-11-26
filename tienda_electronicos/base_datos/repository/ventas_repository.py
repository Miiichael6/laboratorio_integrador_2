from tienda_electronicos.base_datos.repository.base_repository import BaseRepository
class VentasRepository(BaseRepository):
    def __init__(self, gestor):
        super().__init__(gestor, table="ventas", id_column="id")
