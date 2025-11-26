from tienda_electronicos.base_datos.database_gestor import DatabaseGestor
from tienda_electronicos.base_datos.repository import ProductosRepository, ClientesRepository, VentasRepository, DetalleVentasRepository
from tienda_electronicos.tienda.tienda_electronicos_gestor import TiendaGestorDatabase

database = DatabaseGestor()

productos_repo = ProductosRepository(database)
clientes_repo = ClientesRepository(database)
ventas_repo = VentasRepository(database)
detalle_ventas_repo = DetalleVentasRepository(database)