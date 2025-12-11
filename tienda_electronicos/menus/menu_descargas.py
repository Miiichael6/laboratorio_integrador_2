from tienda_electronicos.tienda import ElectronicosGestion
def menu_descargas(elect: ElectronicosGestion):
    """Menú para descargar archivos."""
    while True:
        print("\n" + "="*50)
        print("📥 DESCARGAR REPORTES Y ARCHIVOS")
        print("="*50)
        print("1. Descargar Catálogo (CSV)")
        print("2. Descargar Historial de Ventas (CSV)")
        print("3. Listar archivos disponibles")
        print("0. Atrás")
        print("="*50)

        try:
            opcion = input("Selecciona una opción: ").strip()

            if opcion == "1":
                elect.descargar_catalogo_csv()
                
            elif opcion == "2":
                elect.descargar_ventas_csv()

            elif opcion == "3":
                elect.mostrar_contenido_reportes()

            elif opcion == "0":
                break
            else:
                print("❌ Opción inválida")

        except Exception as e:
            print(f"❌ Error: {e}")
