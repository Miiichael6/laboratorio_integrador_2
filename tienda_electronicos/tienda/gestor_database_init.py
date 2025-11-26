import datetime
from tienda_electronicos.base_datos.database_gestor import DatabaseGestor
from tienda_electronicos.base_datos.repository import ProductosRepository, VentasRepository, ClientesRepository, DetalleVentasRepository

class TiendaGestorDatabase:
    def __init__(
            self, 
            db: DatabaseGestor, 
            productos_repository: ProductosRepository,
            clientes_repository: ClientesRepository,
            ventas_repository: VentasRepository,
            detalle_ventas_repository: DetalleVentasRepository,
        ):
        self.db = db
        self.productos_repository = productos_repository
        self.clientes_repository = clientes_repository
        self.ventas_repository = ventas_repository
        self.detalle_ventas_repository = detalle_ventas_repository

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
    
    def inicializar_base_datos(self):
        """Crea las tablas en SQLite."""
        try:
            self.db.execute('''
                 CREATE TABLE IF NOT EXISTS productos (
                     id INTEGER PRIMARY KEY AUTOINCREMENT,
                     nombre TEXT NOT NULL,
                     precio REAL NOT NULL,
                     stock INTEGER NOT NULL,
                     categoria TEXT NOT NULL
                 );
            ''')

            self.db.execute('''
                CREATE TABLE IF NOT EXISTS clientes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    tipo TEXT NOT NULL
                );
            ''')

            self.db.execute('''
                CREATE TABLE IF NOT EXISTS ventas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    fecha DATETIME NOT NULL,
                    cliente_id INTEGER,
                    cliente_nombre TEXT,
                    subtotal REAL NOT NULL,
                    descuento_pct REAL DEFAULT 0,
                    total REAL NOT NULL
                );
            ''')

            self.db.execute('''
                CREATE TABLE IF NOT EXISTS detalle_ventas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    venta_id INTEGER,
                    producto_nombre TEXT NOT NULL,
                    precio_unitario REAL NOT NULL,
                    cantidad INTEGER NOT NULL,
                    subtotal REAL NOT NULL
                );
            ''')


            self.insertar_datos_iniciales()
            print("✅ Base de datos inicializada\n")

        except Exception as e:
            print(f"❌ Error: {e}")

    def insertar_datos_iniciales(self):
        """Inserta datos de prueba."""
        # productos = self.productos_repository.find_all()
        # clientes = self.clientes_repository.find_all()
        producto_cantidad = self.db.select_one("SELECT COUNT(*) FROM productos")
        clientes_cantidad = self.db.select_one("SELECT COUNT(*) FROM clientes")

        if producto_cantidad == 0:
            for nombre, precio, stock, categoria in self.catalogo:
                self.productos_repository.create({
                    "nombre": nombre,
                    "precio": precio,
                    "stock": stock,
                    "categoria": categoria
                })

        if clientes_cantidad == 0:
            for cliente in self.clientes:
                self.clientes_repository.create({
                    "nombre": cliente["nombre"],
                    "tipo": cliente["tipo"]
                })

    def insertar_venta_bd(self, venta):
        """Inserta una venta en la BD."""
        try:

            venta_creada = self.ventas_repository.create({
                "fecha": venta["fecha"],
                "cliente_id": venta["cliente_id"],
                "cliente_nombre": venta["cliente"],
                "subtotal": venta["subtotal"],
                "descuento_pct": venta["descuento_pct"],
                "total": venta["total"]
            })

            venta_id = venta_creada.lastrowid

            for nombre, precio, cantidad, _ in venta["items"]:
                subtotal_item = precio * cantidad

                self.detalle_ventas_repository.create({
                    "venta_id": venta_id,
                    "producto_nombre": nombre,
                    "precio_unitario": precio,
                    "cantidad": cantidad,
                    "subtotal": subtotal_item
                })
        except Exception as e:
            print(f"❌ Error: {e}")

    def guardar_venta_archivo(self, venta):
        """Guarda venta en archivo txt."""
        try:
            fecha_hoy = datetime.datetime.now().strftime('%Y%m%d')
            archivo = f"tienda_electronicos/datos/ventas_{fecha_hoy}.txt"

            with open(archivo, 'a', encoding='utf-8') as f:
                f.write(f"VENTA - {venta['fecha'].strftime('%d/%m/%Y %H:%M:%S')}\n")
                f.write(f"Cliente: {venta['cliente']} (ID: {venta['cliente_id']})\n")
                f.write("Items:\n")

                for nombre, precio, cantidad, categoria in venta["items"]:
                    f.write(f"{categoria} - {nombre} x{cantidad} @ S/{precio} = S/{precio*cantidad:.2f}\n")

                f.write(f"Subtotal: S/{venta['subtotal']:.2f}\n")
                f.write(f"Descuento: {venta['descuento_pct']:.1f}%\n")
                f.write(f"Total: S/{venta['total']:.2f}\n")
                f.write("-" * 50 + "\n\n")

        except Exception as e:
            print(f"❌ Error: {e}")
