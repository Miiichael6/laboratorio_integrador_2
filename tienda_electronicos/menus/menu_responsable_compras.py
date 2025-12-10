from tienda_electronicos.tienda import ElectronicosGestion

def menu_responsable_compras(elect: ElectronicosGestion):
    """Menú para el Responsable de Compras."""
    while True:
        print("\n" + "="*50)
        print("🛒 RESPONSABLE DE COMPRAS")
        print("="*50)
        print("1. Mostrar Catálogo")
        print("2. Agregar al Carrito")
        print("3. Mostrar Carrito")
        print("4. Finalizar Compra")
        print("0. Cambiar de Rol")
        print("="*50)

        try:
            opcion = input("Selecciona una opción: ").strip()

            if opcion == "1":
                elect.mostrar_catalogo()

            elif opcion == "2":
                elect.opcion_agregar_al_carrito()

            elif opcion == "3":
                elect.mostrar_carrito()
                
            elif opcion == "4":
                elect.opcion_finalizar_compra()

            elif opcion == "0":
                break

            else:
                print("❌ Opción inválida")

        except Exception as e:
            print(f"❌ Error: {e}")
