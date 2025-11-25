from .gestor_database_init import TiendaGestorDatabase
import matplotlib.pyplot as plt
import os
import warnings

class ElectronicosGestion:
    """Sistema de gestión para una tienda de Electrónicos con roles diferenciados."""

    def __init__(
            self,
            tienda_gestor_db: TiendaGestorDatabase
        ):
        self.tienda_gestor_db = tienda_gestor_db
        """Inicializa el sistema con datos básicos."""
        # Catálogo de productos y servicios
        # Carrito y ventas
        self.carrito = []
        self.ventas = []

        # Crear carpetas
        self.crear_directorios()
        self.tienda_gestor_db.inicializar_base_datos()
        print("execute creacion database tablas")

    def crear_directorios(self):
        """Crea las carpetas necesarias."""
        carpetas = ['datos', 'base_datos', 'reportes']
        for carpeta in carpetas:
            print(carpeta)
            os.makedirs(f"tienda_electronicos/{carpeta}", exist_ok=True)
        print("✅ Carpetas creadas correctamente\n")
