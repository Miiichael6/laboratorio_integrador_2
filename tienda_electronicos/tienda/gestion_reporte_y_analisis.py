from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .tienda_electronicos_gestor import ElectronicosGestion
class TiendaGestionReporteYAnalisis:
    
    def mostrar_historial(self: "ElectronicosGestion"):
        """Muestra el historial de ventas."""
        if not self.ventas:
            print("📊 No hay ventas registradas\n")
            return

        print("\n" + "="*80)
        print("📊 HISTORIAL DE VENTAS")
        print("="*80)

        total_ventas = 0
        for i, venta in enumerate(self.ventas, 1):
            fecha_str = venta["fecha"].strftime('%d/%m/%Y %H:%M')
            print(f"{i:>3}. {fecha_str} | {venta['cliente']:<20} | S/{venta['total']:>8.2f}")
            total_ventas += venta['total']

        print("-" * 80)
        print(f"Total de ventas: {len(self.ventas)} | Monto total: S/{total_ventas:.2f}\n")

    def productos_mas_vendidos(self: "ElectronicosGestion", limite=5):
        """Muestra los productos más vendidos."""
        try:

            resultados = self.db.select('''
                SELECT
                    dv.producto_nombre,
                    SUM(dv.cantidad) as total_vendido,
                    SUM(dv.subtotal) as ingresos_total
                FROM detalle_ventas dv
                JOIN ventas v ON dv.venta_id = v.id
                GROUP BY dv.producto_nombre
                ORDER BY total_vendido DESC
                LIMIT ?
            ''', (limite,))

            print(f"\n🏆 TOP {limite} PRODUCTOS MÁS VENDIDOS")
            print("="*70)
            print(f"{'Producto':<25} {'Cantidad':<10} {'Ingresos'}")
            print("-"*70)

            for producto, cantidad, ingresos in resultados:
                print(f"{producto:<25} {cantidad:<10} S/{ingresos:<10.2f}")

        except Exception as e:
            print(f"❌ Error: {e}")

    def ventas_por_cliente(self: "ElectronicosGestion"):
        """Muestra ventas agrupadas por cliente."""
        try:
            resultados = self.db.select('''
                SELECT
                    c.nombre,
                    c.tipo,
                    COUNT(v.id) as total_compras,
                    SUM(v.total) as monto_total
                FROM clientes c
                LEFT JOIN ventas v ON c.id = v.cliente_id
                GROUP BY c.id
                ORDER BY monto_total DESC
            ''')

            print("\n👥 VENTAS POR CLIENTE")
            print("="*75)
            print(f"{'Cliente':<20} {'Tipo':<10} {'Compras':<8} {'Total'}")
            print("-"*75)

            for nombre, tipo, compras, total in resultados:
                total_str = f"S/{total:.2f}" if total else "S/0.00"
                print(f"{nombre:<20} {tipo:<10} {compras or 0:<8} {total_str}")

        except Exception as e:
            print(f"❌ Error: {e}")

    def productos_stock_bajo(self: "ElectronicosGestion", limite_stock=10):
        """Muestra productos con stock bajo."""
        try:

            resultados = self.db.select('''
                SELECT nombre, stock, categoria, precio
                FROM productos
                WHERE stock <= ?
                ORDER BY stock ASC
            ''', (limite_stock,))

            print(f"\n⚠️ PRODUCTOS CON STOCK BAJO (≤ {limite_stock})")
            print("="*60)
            print(f"{'Producto':<25} {'Stock':<8} {'Categoría':<15} {'Precio'}")
            print("-"*60)

            for nombre, stock, categoria, precio in resultados:
                alerta = "🔴" if stock == 0 else "🟡"
                print(f"{alerta} {nombre:<23} {stock:<8} {categoria:<15} S/{precio:.2f}")

        except Exception as e:
            print(f"❌ Error: {e}")
