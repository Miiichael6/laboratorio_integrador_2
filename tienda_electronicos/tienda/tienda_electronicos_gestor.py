from tienda_electronicos.tienda.gestor_database_init import TiendaGestorDatabase
from tienda_electronicos.tienda.gestion_compras import TiendaGestionCompras
from tienda_electronicos.tienda.gestion_productos import TiendaGestionProductos
from tienda_electronicos.tienda.gestion_reporte_y_analisis import TiendaGestionReporteYAnalisis
from tienda_electronicos.tienda.gestion_graficos_y_reportes import TiendaGestionGraficosYReportes
from tienda_electronicos.base_datos.database_gestor import DatabaseGestor
from tienda_electronicos.base_datos.repository import ProductosRepository, ClientesRepository, VentasRepository, DetalleVentasRepository
import os

class ElectronicosGestion(
        TiendaGestionProductos,
        TiendaGestionGraficosYReportes,
        TiendaGestionReporteYAnalisis,
        TiendaGestionCompras,
        TiendaGestorDatabase,
    ):
    """Sistema de gestión para una tienda de Electrónicos con roles diferenciados."""

    def __init__(
            self,
            db: DatabaseGestor,
            productos_repo: ProductosRepository,
            clientes_repo: ClientesRepository,
            ventas_repo: VentasRepository,
            detalle_ventas_repo: DetalleVentasRepository
        ):
        super().__init__()
        # Llamar al __init__ de TiendaGestorDatabase que es la clase base principal
        self.db=db
        self.productos_repository=productos_repo
        self.clientes_repository=clientes_repo
        self.ventas_repository=ventas_repo
        self.detalle_ventas_repository=detalle_ventas_repo
        
        # Carrito y ventas
        self.carrito = []
        self.ventas = []

        # Crear carpetas
        self.crear_directorios()
        self.inicializar_base_datos()

    def crear_directorios(self):
        """Crea las carpetas necesarias."""
        carpetas = ['datos', 'base_datos', 'reportes']
        for carpeta in carpetas:
            os.makedirs(f"tienda_electronicos/{carpeta}", exist_ok=True)
        print("✅ Carpetas creadas correctamente\n")
