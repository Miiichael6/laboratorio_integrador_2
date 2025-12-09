from typing import TYPE_CHECKING
import pprint
if TYPE_CHECKING:
    from .tienda_electronicos_gestor import ElectronicosGestion
    
class TiendaGestionProductos:
    def mostrar_catalogo(self: "ElectronicosGestion"):
        """Muestra todos los productos por categoría."""
        print("\n" + "="*60)
        print("CATÁLOGO DE SERVICIOS Y PRODUCTOS")
        print("="*60)

        productos = self.productos_repository.find_all()

        categorias = {}
        for producto in productos:
            if producto['categoria'] not in categorias:
                categorias[producto['categoria']] = []
            categorias[producto['categoria']].append((producto['nombre'], producto['precio'], producto['stock']))

        for categoria, items in categorias.items():
            print(f"\n📋 {categoria.upper()}")
            print("-" * 40)
            for nombre, precio, stock in items:
                estado = "✓ Disponible" if stock > 0 else "✗ Agotado"
                print(f"• {nombre:<25} S/{precio:>6.2f} | Stock: {stock:>3} {estado}")
        print(f"\n")

    def buscar_producto(self: "ElectronicosGestion", nombre: str) -> dict:
        """Busca un producto por nombre."""
        productos = self.productos_repository.find_all()
        nombre_lower = nombre.lower()
        for producto in productos:
            if nombre_lower in producto['nombre'].lower():
                return producto
        return None

    def actualizar_precio_producto(self: "ElectronicosGestion", nombre, nuevo_precio):
        """Actualiza el precio de un producto."""

        productos = self.productos_repository.find_all()
        for producto in productos:
            if producto['nombre'].lower() == nombre.lower():
                precio_anterior = producto['precio']
                self.productos_repository.update(producto['id'], { "precio": nuevo_precio })

                print(f"\n✅ Precio actualizado: {producto['nombre']}")
                print(f"   Precio anterior: S/{precio_anterior:.2f}")
                print(f"   Precio nuevo: S/{nuevo_precio:.2f}")
                return True

        print(f"❌ Producto '{nombre}' no encontrado")
        return False
    
    def actualizar_stock_producto(self: "ElectronicosGestion", producto: dict):
        self.productos_repository.update(producto['id'], { "stock": producto['stock'] })

    def agregar_stock_producto(self: "ElectronicosGestion", nombre: str, stock: int):
        """Agrega stock a un producto."""
        productos = self.productos_repository.find_all()

        for prod in productos:
            if prod['nombre'].lower() == nombre.lower():
                self.productos_repository.update(prod['id'], { "stock": prod['stock'] + stock })
                print(f"\n✅ Stock actualizado: {prod['nombre']}")
                print(f"   Stock anterior: {prod['stock']}")
                print(f"   Stock nuevo: {prod['stock'] + stock}")
                return True

        print(f"❌ Producto '{nombre}' no encontrado")
        return False

    def agregar_nuevo_producto(self: "ElectronicosGestion", nombre, precio, stock, categoria):
        """Agrega un nuevo producto al catálogo."""
        if self.buscar_producto(nombre):
            print(f"❌ El producto '{nombre}' ya existe")
            return False

        self.productos_repository.create({
            "nombre": nombre,
            "precio": precio,
            "stock": stock,
            "categoria": categoria
        })

        print(f"\n✅ Producto agregado: {nombre}")
        print(f"   Precio: S/{precio:.2f}")
        print(f"   Stock: {stock}")
        print(f"   Categoría: {categoria}")
        return True
