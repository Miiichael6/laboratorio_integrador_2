from IPython.core.hooks import clipboard_get
import datetime
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .tienda_electronicos_gestor import ElectronicosGestion

class TiendaGestorDatabase:
    def inicializar_base_datos(self: "ElectronicosGestion"):
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
            print(f"❌ Error inicializar_base_datos: {e}")

    def insertar_datos_iniciales(self: "ElectronicosGestion"):
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

    def insertar_venta_bd(self: "ElectronicosGestion", venta: dict):
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

            venta_id = venta_creada["id"]
            
            for item in venta["items"]:
                subtotal_item = item["precio"] * item["cantidad"]

                self.detalle_ventas_repository.create({
                    "venta_id": venta_id,
                    "producto_nombre": item["nombre"],
                    "precio_unitario": item["precio"],
                    "cantidad": item["cantidad"],
                    "subtotal": subtotal_item
                })
        except Exception as e:
            print(f"❌ Error insertar_venta_bd: {e}")

    def guardar_venta_archivo(self: "ElectronicosGestion", venta: dict):
        """Guarda venta en archivo txt."""
        try:
            fecha_hoy = datetime.datetime.now().strftime('%Y%m%d')
            archivo = f"tienda_electronicos/datos/ventas_{fecha_hoy}.txt"

            with open(archivo, 'a', encoding='utf-8') as f:
                f.write(f"VENTA - {venta['fecha'].strftime('%d/%m/%Y %H:%M:%S')}\n")
                f.write(f"Cliente: {venta['cliente']} (ID: {venta['cliente_id']})\n")
                f.write("Items:\n")

                for item in venta["items"]:
                    nombre = item["nombre"]
                    precio = item["precio"]
                    cantidad = item["cantidad"]
                    categoria = item["categoria"]
                    f.write(f"{categoria} - {nombre} x{cantidad} @ S/{precio} = S/{precio*cantidad:.2f}\n")

                f.write(f"Subtotal: S/{venta['subtotal']:.2f}\n")
                f.write(f"Descuento: {venta['descuento_pct']:.1f}%\n")
                f.write(f"Total: S/{venta['total']:.2f}\n")
                f.write("-" * 50 + "\n\n")

        except Exception as e:
            print(f"❌ Error guardar_venta_archivo: {e}")
