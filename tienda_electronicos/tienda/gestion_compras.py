# ========================================================================
# GESTIÓN DE COMPRAS (RESPONSABLE DE COMPRAS)
# ========================================================================
from tienda_electronicos.tienda.gestion_productos import TiendaGestionProductos
import datetime

class TiendaGestionCompras(TiendaGestionProductos): 
    carrito: list

    def agregar_al_carrito(self, nombre, cantidad):
        """Agrega un producto al carrito."""
        producto = self.buscar_producto(nombre)

        if not producto:
            print(f"❌ Producto '{nombre}' no encontrado")
            return False

        nombre_prod, precio, stock, categoria = producto

        if stock < cantidad:
            print(f"❌ Stock insuficiente. Disponible: {stock}, Solicitado: {cantidad}")
            return False

        for i, item in enumerate(self.carrito):
            if item[0] == nombre_prod:
                nueva_cantidad = item[2] + cantidad
                if stock < nueva_cantidad:
                    print(f"❌ Stock insuficiente para agregar más")
                    return False
                self.carrito[i] = (nombre_prod, precio, nueva_cantidad, categoria)
                print(f"✓ Cantidad actualizada: {nombre_prod} x{nueva_cantidad}")
                return True

        # el carrito es algo que se guarda en memoria
        self.carrito.append((nombre_prod, precio, cantidad, categoria))

        print(f"✓ Agregado al carrito: {nombre_prod} x{cantidad}")
        return True

    def mostrar_carrito(self):
        """Muestra el contenido del carrito."""
        if not self.carrito:
            print("🛒 El carrito está vacío\n")
            return

        print("\n" + "="*50)
        print("🛒 CARRITO DE COMPRAS")
        print("="*50)

        total = 0
        for nombre, precio, cantidad, categoria in self.carrito:
            subtotal = precio * cantidad
            total += subtotal
            print(f"• {nombre:<25} S/{precio:>6.2f} x {cantidad} = S/{subtotal:>8.2f}")

        print("-" * 50)
        print(f"TOTAL: S/{total:.2f}\n")

    def aplicar_descuento(self, total, tipo_cliente):
        """Aplica descuento según tipo de cliente."""
        descuentos = {"premium": 0.15, "regular": 0.05} # segun tipo de cliente
        porcentaje = descuentos.get(tipo_cliente, 0)
        descuento_aplicado = total * porcentaje
        total_final = total - descuento_aplicado
        return total_final, porcentaje * 100

    def finalizar_compra(self, cliente_id):
        """Procesa la compra final."""
        if not self.carrito:
            print("❌ El carrito está vacío")
            return False

        cliente = None
        for c in self.clientes:
            if c["id"] == cliente_id:
                cliente = c
                break

        if not cliente:
            print(f"❌ Cliente con ID {cliente_id} no encontrado")
            return False

        # Calcular totales
        subtotal = sum(precio * cantidad for _, precio, cantidad, _ in self.carrito)
        total_final, descuento_pct = self.aplicar_descuento(subtotal, cliente["tipo"])

        # Actualizar stock
        for item_carrito in self.carrito:
            nombre_carrito = item_carrito[0]
            cantidad_carrito = item_carrito[2]

            for i, item_catalogo in enumerate(self.catalogo):
                if item_catalogo[0] == nombre_carrito:
                    nombre, precio, stock, categoria = item_catalogo
                    nuevo_stock = stock - cantidad_carrito
                    self.catalogo[i] = (nombre, precio, nuevo_stock, categoria)
                    break

        # Registrar venta
        venta = {
            "fecha": datetime.datetime.now(),
            "cliente": cliente["nombre"],
            "cliente_id": cliente_id,
            "items": self.carrito.copy(),
            "subtotal": subtotal,
            "descuento_pct": descuento_pct,
            "total": total_final
        }

        self.registrar_venta(venta)
        self.mostrar_ticket_venta(venta)
        self.carrito.clear() # limpiamos el carro para el siguiente cliente
        return True

    def registrar_venta(self, venta):
        """Registra una venta."""
        self.ventas.append(venta)
        self.insertar_venta_bd(venta)
        self.guardar_venta_archivo(venta)

    def mostrar_ticket_venta(self, venta):
        """Muestra el ticket de venta."""
        print("\n" + "="*60)
        print(" Electronicos HUELLITAS - TICKET DE VENTA")
        print("="*60)
        print(f"Fecha: {venta['fecha'].strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Cliente: {venta['cliente']}")
        print("-" * 60)

        for nombre, precio, cantidad, _ in venta["items"]:
            subtotal = precio * cantidad
            print(f"{nombre:<35} {cantidad:>3} x S/{precio:>6.2f} = S/{subtotal:>8.2f}")

        print("-" * 60)
        print(f"Subtotal: {venta['subtotal']:>46.2f}")
        if venta['descuento_pct'] > 0:
            descuento_monto = venta['subtotal'] - venta['total']
            print(f"Descuento ({venta['descuento_pct']:.0f}%): {descuento_monto:>38.2f}")
        print(f"TOTAL: S/{venta['total']:>45.2f}")
        print("="*60)
        print("¡Gracias por confiar en nosotros! \n")
