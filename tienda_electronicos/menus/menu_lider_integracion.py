from tienda_electronicos.tienda import ElectronicosGestion
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
        print("12. Ver Historial de Compras")
        print("\n0. Cambiar de Rol")
        print("="*50)

        try:
            opcion = input("Selecciona una opción: ").strip()

            if opcion == "1":
                elect.mostrar_catalogo()
            elif opcion == "2":
                nombre = input("Producto a buscar: ").strip()
                producto = elect.buscar_producto(nombre)
                if producto:
                    print(f"\n✓ {producto[0]} - S/{producto[1]:.2f} (Stock: {producto[2]})")
                else:
                    print("❌ No encontrado")
            elif opcion == "3":
                elect.mostrar_catalogo()
                nombre = input("\nProducto: ").strip()
                try:
                    precio = float(input("Nuevo precio: "))
                    elect.actualizar_precio_producto(nombre, precio)
                except ValueError:
                    print("❌ Inválido")
            elif opcion == "4":
                nombre = input("Producto: ").strip()
                try:
                    precio = float(input("Precio: "))
                    stock = int(input("Stock: "))
                    categoria = input("Categoría: ").strip()
                    elect.agregar_nuevo_producto(nombre, precio, stock, categoria)
                except ValueError:
                    print("❌ Inválido")
            elif opcion == "4b":
                nombre = input("Nombre del cliente: ").strip()
                tipo = input("Tipo (regular/premium): ").strip().lower()
                if tipo in ["regular", "premium"]:
                    elect.agregar_cliente(nombre, tipo)
                else:
                    print("❌ Tipo debe ser 'regular' o 'premium'")
            elif opcion == "5":
                nombre = input("Producto: ").strip()
                try:
                    cantidad = int(input("Cantidad: "))
                    elect.agregar_al_carrito(nombre, cantidad)
                except ValueError:
                    print("❌ Inválido")
            elif opcion == "6":
                elect.mostrar_carrito()
            elif opcion == "7":
                print("Clientes:")
                for c in elect.clientes:
                    print(f"  {c['id']}: {c['nombre']}")
                try:
                    cliente_id = int(input("ID cliente: "))
                    elect.finalizar_compra(cliente_id)
                except ValueError:
                    print("❌ Inválido")
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
            elif opcion == "0":
                break
            else:
                print("❌ Inválido")

        except Exception as e:
            print(f"❌ Error: {e}")
