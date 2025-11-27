from tienda_electronicos.tienda import ElectronicosGestion
def menu_graficos(elect: ElectronicosGestion):
    """Menú para ver historial de compras."""
    while True:
        print("\n" + "="*50)
        print("📊 HISTORIAL DE COMPRAS")
        print("="*50)
        print("1. Ver Historial de Ventas")
        print("0. Atrás")
        print("="*50)

        try:
            opcion = input("Selecciona una opción: ").strip()

            if opcion == "1":
                elect.mostrar_historial()
            elif opcion == "0":
                break
            else:
                print("❌ Opción inválida")

        except Exception as e:
            print(f"❌ Error: {e}")
