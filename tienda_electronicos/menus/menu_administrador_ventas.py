from tienda_electronicos.tienda import ElectronicosGestion
def menu_administrador_ventas(elect: ElectronicosGestion):
    """Menú para el Administrador de Ventas."""
    while True:
        print("\n" + "="*50)
        print("📊 ADMINISTRADOR DE VENTAS")
        print("="*50)
        print("1. Mostrar Historial de Ventas")
        print("2. Productos Más Vendidos")
        print("3. Ventas por Cliente")
        print("4. Productos con Stock Bajo")
        print("5. Agregar Nuevo Cliente")
        print("0. Cambiar de Rol")
        print("="*50)

        try:
            opcion = input("Selecciona una opción: ").strip()

            if opcion == "1":
                elect.mostrar_historial()

            elif opcion == "2":
                elect.productos_mas_vendidos()

            elif opcion == "3":
                elect.ventas_por_cliente()

            elif opcion == "4":
                elect.productos_stock_bajo()

            elif opcion == "5":
                elect.opcion_agregar_cliente()

            elif opcion == "0":
                break

            else:
                print("❌ Opción inválida")

        except Exception as e:
            print(f"❌ Error: {e}")
