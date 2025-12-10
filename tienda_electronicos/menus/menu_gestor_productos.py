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
                elect.opcion_buscar_producto()

            elif opcion == "3":
                elect.opcion_actualizar_precio_producto()

            elif opcion == "4":
                elect.opcion_agregar_nuevo_producto()

            elif opcion == "5":
                elect.opcion_agregar_mas_stock_producto()

            elif opcion == "0":
                break

            else:
                print("❌ Opción inválida")

        except Exception as e:
            print(f"❌ Error: {e}")
