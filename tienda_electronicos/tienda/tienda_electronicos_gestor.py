from tienda_electronicos.tienda.gestion_descargas import TiendaGestionDescargas
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
        TiendaGestionDescargas
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

        # data
        self.clientes = [
            {"id": 1, "nombre": "María González", "tipo": "regular"},
            {"id": 2, "nombre": "Carlos Ruiz", "tipo": "premium"},
            {"id": 3, "nombre": "Ana Torres", "tipo": "regular"},
            {"id": 4, "nombre": "José Martínez", "tipo": "regular"},
            {"id": 5, "nombre": "Lucía Fernández", "tipo": "premium"},
            {"id": 6, "nombre": "Pedro Sánchez", "tipo": "regular"},
            {"id": 7, "nombre": "Valeria Campos", "tipo": "regular"},
            {"id": 8, "nombre": "Diego Rivas", "tipo": "premium"},
            {"id": 9, "nombre": "Soledad Castro", "tipo": "regular"},
            {"id": 10, "nombre": "Javier Molina", "tipo": "regular"},
            {"id": 11, "nombre": "Patricia León", "tipo": "premium"},
            {"id": 12, "nombre": "Héctor Salazar", "tipo": "regular"},
            {"id": 13, "nombre": "Daniela Paredes", "tipo": "regular"},
            {"id": 14, "nombre": "Rodrigo Vera", "tipo": "premium"},
            {"id": 15, "nombre": "Carmen Castillo", "tipo": "regular"},
            {"id": 16, "nombre": "Luis Benavides", "tipo": "regular"},
            {"id": 17, "nombre": "Natalia Bravo", "tipo": "premium"},
            {"id": 18, "nombre": "Esteban Aguirre", "tipo": "regular"},
            {"id": 19, "nombre": "Rocío Medina", "tipo": "regular"},
            {"id": 20, "nombre": "Andrés Cáceres", "tipo": "premium"}
        ]
        
        self.catalogo = [
            ("Laptop Básica 14", 1500.0, 25, "Computadoras"),
            ("Mouse Inalámbrico", 45.0, 80, "Accesorios"),
            ("Monitor 24 FHD", 520.0, 40, "Pantallas"),
            ("Teclado Mecánico RGB", 260.0, 35, "Accesorios"),
            ("Audífonos Bluetooth", 180.0, 50, "Audio"),
            ("Router WiFi 6", 310.0, 30, "Redes"),
            ("SSD 1TB NVMe", 420.0, 45, "Almacenamiento"),
            ("Impresora Multifuncional", 680.0, 20, "Periféricos"),
            ("Cargador Rápido 30W", 70.0, 60, "Accesorios"),
            ("Webcam Full HD", 110.0, 25, "Periféricos")
        ]
    
        
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
        print("✅ Carpetas creadas correctamente")
