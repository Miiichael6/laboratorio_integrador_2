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
        print("4. Agregar cliente")
        print("5. Finalizar Compra")
        print("0. Cambiar de Rol")
        print("="*50)

        try:
            opcion = input("Selecciona una opción: ").strip()

            if opcion == "1":
                elect.mostrar_catalogo()

            elif opcion == "2":
                nombre = input("Nombre del producto: ").strip()
                try:
                    cantidad = int(input("Cantidad: ").strip())
                    if cantidad > 0:
                        elect.agregar_al_carrito(nombre, cantidad)
                    else:
                        print("❌ Cantidad debe ser mayor a 0")
                except ValueError:
                    print("❌ Cantidad inválida")

            elif opcion == "3":
                elect.mostrar_carrito()
            elif opcion == "4":
                try:
                    nombre = input("Ingrese el nombre del nuevo cliente: ").strip()
                    tipo = input("Ingrese el tipo del nuevo cliente (regular/premium): ").strip()
                    elect.agregar_cliente(nombre, tipo)
                except ValueError:
                    print("❌ ID inválido")

            elif opcion == "5":
                print("\nClientes disponibles:")
                clientes = elect.clientes_repository.find_all()
                for cliente in clientes:
                    print(f"  ID: {cliente['id']} - {cliente['nombre']} ({cliente['tipo']})")
                try:
                    cliente_id = int(input("ID del cliente: ").strip())
                    elect.finalizar_compra(cliente_id)
                except ValueError:
                    print("❌ ID inválido")

            elif opcion == "0":
                break

            else:
                print("❌ Opción inválida")

        except Exception as e:
            print(f"❌ Error: {e}")
