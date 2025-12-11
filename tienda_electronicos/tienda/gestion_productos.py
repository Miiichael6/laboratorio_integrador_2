from typing import TYPE_CHECKING
import pandas as pd
import os

if TYPE_CHECKING:
    from .tienda_electronicos_gestor import ElectronicosGestion

class TiendaGestionProductos:
    # REGION DE OPCIONES
    def opcion_buscar_producto(self: "ElectronicosGestion"): 
        nombre = input("Nombre del producto a buscar: ").strip()
        producto = self.buscar_producto(nombre)
        if producto:
            print(f"\n✓ Producto encontrado:")
            print(f"  Nombre: {producto['nombre']}")
            print(f"  Precio: S/{producto['precio']:.2f}")
            print(f"  Stock: {producto['stock']}")
            print(f"  Categoría: {producto['categoria']}")
        else:
            print(f"❌ Producto '{nombre}' no encontrado")
    
    def opcion_actualizar_precio_producto(self: "ElectronicosGestion"):
        print("\n" + "="*50)
        print("💰 ACTUALIZAR PRECIO")
        print("="*50)
        self.mostrar_catalogo()
        nombre = input("\nNombre del producto: ").strip()
        try:
            nuevo_precio = float(input("Nuevo precio (S/): "))
            if nuevo_precio > 0:
                self.actualizar_precio_producto(nombre, nuevo_precio)
            else:
                print("❌ El precio debe ser mayor a 0")
        except ValueError:
            print("❌ Precio inválido")

    def opcion_agregar_nuevo_producto(self: "ElectronicosGestion"):
        print("\n" + "="*50)
        print("➕ AGREGAR NUEVO PRODUCTO")
        print("="*50)
        nombre = input("Nombre del producto: ").strip()
        try:
            precio = float(input("Precio (S/): "))
            stock = int(input("Stock inicial: "))
            categoria = input("Categoría: ").strip()
            if precio > 0 and stock >= 0:
                self.agregar_nuevo_producto(nombre, precio, stock, categoria)
            else:
                print("❌ Datos inválidos")
        except ValueError:
            print("❌ Datos inválidos")
    
    def opcion_agregar_mas_stock_producto(self: "ElectronicosGestion"):
        print("\n" + "="*50)
        print("➕ AGREGAR STOCK A UN PRODUCTO")
        print("="*50)
        self.mostrar_catalogo()
        try:
            nombre = input("Nombre del producto: ").strip()
            stock = int(input("Stock a agregar: "))

            if stock >= 1:
                self.agregar_stock_producto(nombre, stock)
            else:
                print("❌ Stock inválido")
        except ValueError:
            print("❌ Datos inválidos")


    # REGION DE FUNCIONES VITALES 
    def mostrar_catalogo(self: "ElectronicosGestion"):
        """Muestra todos los productos por categoría."""
        print("\n" + "="*60)
        print("CATÁLOGO DE SERVICIOS Y PRODUCTOS")
        print("="*60)

        productos = self.productos_repository.find_all()

        categorias = {}
        for producto in productos:
            if producto['categoria'] not in categorias:
                categorias[producto['categoria'].upper()] = []
            categorias[producto['categoria'].upper()].append((producto['nombre'], producto['precio'], producto['stock']))

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

    def cargar_productos(self: "ElectronicosGestion", ruta_csv: str = "tienda_electronicos/carga/productos.csv"):
        """Carga productos desde un CSV al catálogo, evitando duplicados y actualizando stock y precio."""
        if not os.path.exists(ruta_csv):
            print(f"❌ No se encontró el archivo CSV: {ruta_csv}")
            return

        df = pd.read_csv(ruta_csv)

        df['nombre'] = df['nombre'].astype(str).str.strip()
        df['categoria'] = df.get('categoria', 'General').astype(str).str.strip()
        df['precio'] = pd.to_numeric(df['precio'], errors='coerce')
        df['stock'] = pd.to_numeric(df['stock'], errors='coerce')

        df_validos = df[(df['nombre'] != "") & (df['precio'] > 0) & (df['stock'] >= 0)]

        for _, fila in df_validos.iterrows():
            self.agregar_nuevo_producto(fila['nombre'], fila['precio'], fila['stock'], fila['categoria'])

        print(f"\n✅ Productos cargados correctamente")
