from tienda_electronicos.tienda import ElectronicosGestion
from .menu_descargas import menu_descargas
from .menu_graficos import menu_graficos

def menu_lider_integracion(elect: ElectronicosGestion):
    """Menú para el Líder de Integración - VE Y HACE TODO."""
    while True:
        print("\n" + "="*50)
        print("👨‍💼 LÍDER DE INTEGRACIÓN - VISTA COMPLETA")
        print("="*50)
        print("\n📋 GESTIÓN DE PRODUCTOS")
        print("1. Mostrar Catálogo")
        print("2. Buscar Producto")
        print("3. Actualizar Precio")
        print("4. Agregar Nuevo Producto")
        print("\n👥 GESTIÓN DE CLIENTES")
        print("4b. Agregar Nuevo Cliente")
        print("\n🛒 GESTIÓN DE COMPRAS")
        print("5. Agregar al Carrito")
        print("6. Mostrar Carrito")
        print("7. Finalizar Compra")
        print("\n📊 REPORTES Y ANÁLISIS")
        print("8. Historial de Ventas")
        print("9. Productos Más Vendidos")
        print("10. Ventas por Cliente")
        print("11. Stock Bajo")
        print("12. Graficos")
        print("13. Descargas")
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

            elif opcion == "4b":
                elect.opcion_agregar_cliente()

            elif opcion == "5":
                elect.opcion_agregar_al_carrito()

            elif opcion == "6":
                elect.mostrar_carrito()

            elif opcion == "7":
                elect.opcion_finalizar_compra()

            elif opcion == "8":
                elect.mostrar_historial()

            elif opcion == "9":
                elect.productos_mas_vendidos()

            elif opcion == "10":
                elect.ventas_por_cliente()

            elif opcion == "11":
                elect.productos_stock_bajo()

            elif opcion == "12":
                menu_graficos(elect)
            
            elif opcion == "13":
                menu_descargas(elect)
                
            elif opcion == "0":
                break
            else:
                print("❌ Inválido")

        except Exception as e:
            print(f"❌ Error: {e}")
