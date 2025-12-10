# ========================================================================
# GESTIÓN DE COMPRAS (RESPONSABLE DE COMPRAS)
# ========================================================================
import datetime
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .tienda_electronicos_gestor import ElectronicosGestion

class TiendaGestionCompras:
    def agregar_al_carrito(self: "ElectronicosGestion", nombre, cantidad):
        """Agrega un producto al carrito."""
        producto = self.buscar_producto(nombre)

        if not producto:
            print(f"❌ Producto '{nombre}' no encontrado")
            return False
        
        id = producto["id"]
        nombre_prod = producto["nombre"]
        precio = producto["precio"]
        stock = producto["stock"]
        categoria = producto["categoria"]

        if stock < cantidad:
            print(f"❌ Stock insuficiente. Disponible: {stock}, Solicitado: {cantidad}")
            return False

        for item in self.carrito:
            if item["id"] == id:
                nueva_cantidad = item["cantidad"] + cantidad
                if stock < nueva_cantidad:
                    print(f"❌ Stock insuficiente para agregar más")
                    return False

                item["cantidad"] = nueva_cantidad
                print(f"✓ Cantidad actualizada: {nombre_prod} x{nueva_cantidad}")
                return True

        self.carrito.append({
            "id": id,
            "nombre": nombre_prod,
            "precio": precio,
            "cantidad": cantidad,
            "categoria": categoria
        })

        print(f"✓ Agregado al carrito: {nombre_prod} x{cantidad}")
        return True

    def mostrar_carrito(self: "ElectronicosGestion"):
        """Muestra el contenido del carrito."""
        if not self.carrito:
            print("🛒 El carrito está vacío\n")
            return

        print("\n" + "="*50)
        print("🛒 CARRITO DE COMPRAS")
        print("="*50)

        total = 0
        for item in self.carrito:
            nombre = item["nombre"]
            precio = item["precio"]
            cantidad = item["cantidad"]
            subtotal = precio * cantidad
            total += subtotal
            print(f"• {nombre:<25} S/{precio:>6.2f} x {cantidad} = S/{subtotal:>8.2f}")

        print("-" * 50)
        print(f"TOTAL: S/{total:.2f}\n")

    def aplicar_descuento(self: "ElectronicosGestion", total, tipo_cliente):
        """Aplica descuento según tipo de cliente."""
        descuentos = {"premium": 0.15, "regular": 0.05} # segun tipo de cliente
        porcentaje = descuentos.get(tipo_cliente, 0)
        descuento_aplicado = total * porcentaje
        total_final = total - descuento_aplicado
        return total_final, porcentaje * 100

    def finalizar_compra(self: "ElectronicosGestion", cliente_id):
        clientes = self.clientes_repository.find_all()
        productos = self.productos_repository.find_all()

        """Procesa la compra final."""
        if not self.carrito:
            print("❌ El carrito está vacío")
            return False

        cliente = None
        for c in clientes:
            if c["id"] == cliente_id:
                cliente = c
                break

        if not cliente:
            print(f"❌ Cliente con ID {cliente_id} no encontrado")
            return False

        # Calcular totales
        subtotal = sum(item["precio"] * item["cantidad"] for item in self.carrito)
        total_final, descuento_pct = self.aplicar_descuento(subtotal, cliente["tipo"])

        # Actualizar stock
        for item_carrito in self.carrito:
            nombre_carrito = item_carrito["nombre"]
            cantidad_carrito = item_carrito["cantidad"]

            for item in productos:
                if item["nombre"] == nombre_carrito:
                    nuevo_stock = item["stock"] - cantidad_carrito
                    producto_updated = { 
                        "id": item["id"],
                        "nombre": item["nombre"],
                        "precio": item["precio"],
                        "stock": nuevo_stock,
                        "categoria": item["categoria"]
                    }
                    self.actualizar_stock_producto(producto_updated)
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

    def registrar_venta(self: "ElectronicosGestion", venta: dict):
        """Registra una venta."""
        self.insertar_venta_bd(venta)
        self.guardar_venta_archivo(venta)

    def mostrar_ticket_venta(self: "ElectronicosGestion", venta: dict):
        """Muestra el ticket de venta."""
        print("\n" + "="*60)
        print(" Electronicos Tecsup Plus - TICKET DE VENTA")
        print("="*60)
        print(f"Fecha: {venta['fecha'].strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Cliente: {venta['cliente']}")
        print("-" * 60)

        for item in venta["items"]:
            nombre = item["nombre"]
            precio = item["precio"]
            cantidad = item["cantidad"]
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

    def agregar_cliente(self: "ElectronicosGestion", nombre: str, tipo: str):
        """Agrega un nuevo cliente."""
        # Normalizar nombre (capitalizar correctamente)
        clientes = self.clientes_repository.find_all()
        nombre = nombre.strip().title()

        # Verificar si ya existe
        for cliente in clientes:
            if cliente["nombre"].lower() == nombre.lower():
                print(f"❌ El cliente '{nombre}' ya existe")
                return False

        # Guardar en BD SQLite
        try:
            nuevo_cliente = { "nombre": nombre, "tipo": tipo}
            cliente_nuevo = self.clientes_repository.create(nuevo_cliente)
        except Exception as e:
            print(f"⚠️ Aviso BD: {e}")

        print(f"\n✅ Cliente agregado: {cliente_nuevo['nombre']}")
        print(f"   ID: {cliente_nuevo['id']}")
        print(f"   Tipo: {cliente_nuevo['tipo']}")
        return True
