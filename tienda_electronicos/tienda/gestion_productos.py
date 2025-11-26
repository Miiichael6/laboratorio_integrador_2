from tienda_electronicos.base_datos.repository import ProductosRepository, ClientesRepository

class TiendaGestionProductos:
    productos_repository: ProductosRepository
    clientes_repository: ClientesRepository
    
    def mostrar_catalogo(self):
        """Muestra todos los productos por categoría."""
        print("\n" + "="*60)
        print("CATÁLOGO DE SERVICIOS Y PRODUCTOS")
        print("="*60)

        productos = self.productos_repository.find_all()

        categorias = {}
        for (id, nombre, precio, stock, categoria) in productos:
            if categoria not in categorias:
                categorias[categoria] = []
            categorias[categoria].append((nombre, precio, stock))

        for categoria, items in categorias.items():
            print(f"\n📋 {categoria.upper()}")
            print("-" * 40)
            for nombre, precio, stock in items:
                estado = "✓ Disponible" if stock > 0 else "✗ Agotado"
                print(f"• {nombre:<25} S/{precio:>6.2f} | Stock: {stock:>3} {estado}")

    def buscar_producto(self, nombre):
        """Busca un producto por nombre."""
        productos = self.productos_repository.find_all()
        nombre_lower = nombre.lower()
        for (id, nom, precio, stock, categoria) in productos:
            if nombre_lower in nom.lower():
                return (id, nom, precio, stock, categoria)
        return None

    def actualizar_precio_producto(self, nombre, nuevo_precio):
        """Actualiza el precio de un producto."""

        productos = self.productos_repository.find_all()
        for (id, nom, precio, stock, categoria) in productos:
            if nom.lower() == nombre.lower():
                precio_anterior = precio
                self.productos_repository.update(id, { "precio": nuevo_precio })

                print(f"\n✅ Precio actualizado: {nom}")
                print(f"   Precio anterior: S/{precio_anterior:.2f}")
                print(f"   Precio nuevo: S/{nuevo_precio:.2f}")
                return True

        print(f"❌ Producto '{nombre}' no encontrado")
        return False

    def agregar_nuevo_producto(self, nombre, precio, stock, categoria):
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

    def agregar_cliente(self, nombre, tipo):
        """Agrega un nuevo cliente."""
        # Normalizar nombre (capitalizar correctamente)
        nombre = nombre.strip().title()

        # Verificar si ya existe
        for cliente in self.clientes:
            if cliente["nombre"].lower() == nombre.lower():
                print(f"❌ El cliente '{nombre}' ya existe")
                return False

        # Obtener nuevo ID
        nuevo_id = max([c["id"] for c in self.clientes]) + 1 if self.clientes else 1

        nuevo_cliente = {"id": nuevo_id, "nombre": nombre, "tipo": tipo}
        self.clientes.append(nuevo_cliente)

        # Guardar también en BD SQLite
        try:
            self.clientes_repository.create({
                "nombre": nombre,
                "tipo": tipo
            })
        except Exception as e:
            print(f"⚠️ Aviso BD: {e}")

        print(f"\n✅ Cliente agregado: {nombre}")
        print(f"   ID: {nuevo_id}")
        print(f"   Tipo: {tipo}")
        return True
