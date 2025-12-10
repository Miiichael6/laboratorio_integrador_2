from tienda_electronicos.tienda import ElectronicosGestion

def menu_gestor_productos(elect: ElectronicosGestion):
    """Menú para el Gestor de Productos."""
    while True:
        print("\n" + "="*50)
        print("🛍️ GESTOR DE PRODUCTOS")
        print("="*50)
        print("1. Mostrar Catálogo")
        print("2. Buscar Producto")
        print("3. Actualizar Precio de Producto")
        print("4. Agregar Nuevo Producto")
        print("5. Agregar más stock a un Producto") # agregado
        print("0. Cambiar de Rol")
        print("="*50)

        try:
            opcion = input("Selecciona una opción: ").strip()

            if opcion == "1":
                elect.mostrar_catalogo()

            elif opcion == "2":
                nombre = input("Nombre del producto a buscar: ").strip()
                producto = elect.buscar_producto(nombre)
                if producto:
                    print(f"\n✓ Producto encontrado:")
                    print(f"  Nombre: {producto['nombre']}")
                    print(f"  Precio: S/{producto['precio']:.2f}")
                    print(f"  Stock: {producto['stock']}")
                    print(f"  Categoría: {producto['categoria']}")
                else:
                    print(f"❌ Producto '{nombre}' no encontrado")

            elif opcion == "3":
                print("\n" + "="*50)
                print("💰 ACTUALIZAR PRECIO")
                print("="*50)
                elect.mostrar_catalogo()
                nombre = input("\nNombre del producto: ").strip()
                try:
                    nuevo_precio = float(input("Nuevo precio (S/): "))
                    if nuevo_precio > 0:
                        elect.actualizar_precio_producto(nombre, nuevo_precio)
                    else:
                        print("❌ El precio debe ser mayor a 0")
                except ValueError:
                    print("❌ Precio inválido")

            elif opcion == "4":
                print("\n" + "="*50)
                print("➕ AGREGAR NUEVO PRODUCTO")
                print("="*50)
                nombre = input("Nombre del producto: ").strip()
                try:
                    precio = float(input("Precio (S/): "))
                    stock = int(input("Stock inicial: "))
                    categoria = input("Categoría: ").strip()

                    if precio > 0 and stock >= 0:
                        elect.agregar_nuevo_producto(nombre, precio, stock, categoria)
                    else:
                        print("❌ Datos inválidos")
                except ValueError:
                    print("❌ Datos inválidos")

            elif opcion == "5":
                print("\n" + "="*50)
                print("➕ AGREGAR STOCK A UN PRODUCTO")
                print("="*50)
                elect.mostrar_catalogo()
                try:
                    nombre = input("Nombre del producto: ").strip()
                    stock = int(input("Stock a agregar: "))

                    if stock >= 1:
                        elect.agregar_stock_producto(nombre, stock)
                    else:
                        print("❌ Stock inválido")
                except ValueError:
                    print("❌ Datos inválidos")

            elif opcion == "0":
                break

            else:
                print("❌ Opción inválida")

        except Exception as e:
            print(f"❌ Error: {e}")
