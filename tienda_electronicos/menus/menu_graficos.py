from tienda_electronicos.tienda import ElectronicosGestion
def menu_graficos(elect: ElectronicosGestion):
    """Menú para ver historial de compras."""
    while True:
        print("\n" + "="*50)
        print("📊 HISTORIAL DE COMPRAS")
        print("="*50)
        print("1. Ver Historial de Ventas")
        print("2. Ver Grafico de Ventas Diarias")
        print("3. Ver Grafico de Productos más vendidos")
        print("4. Ver Grafico de Categorías")
        print("5. Ver Grafico de Clientes")
        print("6. Ver Grafico de Precios")
        print("0. Atrás")
        print("="*50)

        try:
            opcion = input("Selecciona una opción: ").strip()

            if opcion == "1":
                elect.mostrar_historial()

            elif opcion == "2":
                elect.generar_grafico_ventas_diarias()

            elif opcion == "3":
                elect.generar_grafico_productos_vendidos()

            elif opcion == "4":
                elect.generar_grafico_categorias()

            elif opcion == "5":
                elect.generar_grafico_clientes()

            elif opcion == "6":
                elect.generar_grafico_precios()

            elif opcion == "0":
                break
            else:
                print("❌ Opción inválida")

        except Exception as e:
            print(f"❌ Error: {e}")
