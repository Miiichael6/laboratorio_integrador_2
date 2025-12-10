# ========================================================================
# GRÁFICOS Y REPORTES (LÍDER DE INTEGRACIÓN)
# ========================================================================
import matplotlib.pyplot as plt
from typing import TYPE_CHECKING
from datetime import datetime
if TYPE_CHECKING:
    from .tienda_electronicos_gestor import ElectronicosGestion

class TiendaGestionGraficosYReportes:

    def generar_grafico_ventas_diarias(self: "ElectronicosGestion"):
        ventas = self.ventas_repository.find_all()
        if not ventas:
            print("❌ No hay ventas para graficar")
            return

        try:
            fechas = [
                datetime.fromisoformat(v['fecha']).date()
                for v in ventas
            ]
            totales = [v['total'] for v in ventas]

            plt.figure(figsize=(10, 6))
            plt.plot(fechas, totales, marker='o', linewidth=2)
            plt.title('Ventas Diarias - Electronicos', fontsize=14, fontweight='bold')
            plt.xlabel('Fecha')
            plt.ylabel('Total (S/)')
            plt.xticks(rotation=45)
            plt.grid(True, alpha=0.3)
            plt.tight_layout()

            plt.show()  # ← la ventana aparece aquí

            plt.savefig('tienda_electronicos/reportes/ventas_diarias.png')
            plt.close()

            print("✓ Gráfico de ventas generado y mostrado\n")

        except Exception as e:
            print(f"❌ Error generar_grafico_ventas_diarias: {e}")

    def generar_grafico_productos_vendidos(self: "ElectronicosGestion"):
        """Genera gráfico de productos más vendidos."""
        try:
            result = self.db.select('''
                SELECT producto_nombre, SUM(cantidad) as total
                FROM detalle_ventas
                GROUP BY producto_nombre
                ORDER BY total DESC
                LIMIT 10
            ''')

            if not result:
                print("❌ No hay datos")
                return

            productos = [r["producto_nombre"][:15] for r in result]
            cantidades = [r["total"] for r in result]

            plt.figure(figsize=(10, 6))
            plt.barh(productos, cantidades, color='green')
            plt.title('Productos Más Vendidos', fontsize=14, fontweight='bold')
            plt.xlabel('Cantidad Vendida')
            plt.tight_layout()
            plt.savefig('reportes/productos_vendidos.png')
            plt.close()
            print("✓ Gráfico de productos generado\n")

        except Exception as e:
            print(f"❌ Error generar_grafico_productos_vendidos: {e}")

    def generar_grafico_categorias(self: "ElectronicosGestion"):
        """Genera gráfico de ventas por categoría."""
        try:
            result = self.db.select('''
                SELECT
                    p.categoria,
                    SUM(dv.subtotal) as ingresos
                FROM detalle_ventas dv
                JOIN productos p ON dv.producto_nombre = p.nombre
                GROUP BY p.categoria
            ''')

            if not result:
                print("❌ No hay datos")
                return

            categorias = [r["categoria"] for r in result]
            ingresos = [r["ingresos"] for r in result]

            plt.figure(figsize=(10, 6))
            plt.pie(ingresos, labels=categorias, autopct='%1.1f%%', startangle=90)
            plt.title('Ingresos por Categoría', fontsize=14, fontweight='bold')
            plt.tight_layout()
            plt.savefig('reportes/categorias.png')
            plt.close()
            print("✓ Gráfico de categorías generado\n")

        except Exception as e:
            print(f"❌ Error generar_grafico_categorias: {e}")

    def generar_grafico_clientes(self: "ElectronicosGestion"):
        """Genera gráfico de clientes más frecuentes."""
        try:
            result = self.db.select('''
                SELECT cliente_nombre, COUNT(*) as compras
                FROM ventas
                GROUP BY cliente_nombre
                ORDER BY compras DESC
                LIMIT 10
            ''')

            if not result:
                print("❌ No hay datos")
                return

            clientes = [r["cliente_nombre"] for r in result]
            compras = [r["compras"] for r in result]

            plt.figure(figsize=(10, 6))
            plt.bar(clientes, compras, color='orange')
            plt.title('Clientes Más Frecuentes', fontsize=14, fontweight='bold')
            plt.ylabel('Número de Compras')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.savefig('tienda_electronicos/reportes/clientes.png')
            plt.close()
            print("✓ Gráfico de clientes generado\n")

        except Exception as e:
            print(f"❌ Error generar_grafico_clientes: {e}")

    def generar_grafico_precios(self: "ElectronicosGestion"):
        """Genera histograma de precios."""
        try:
            productos = self.productos_repository.find_all()
            precios = [p["precio"] for p in productos]

            plt.figure(figsize=(10, 6))
            plt.hist(precios, bins=10, color='purple', edgecolor='black')
            plt.title('Distribución de Precios', fontsize=14, fontweight='bold')
            plt.xlabel('Precio (S/)')
            plt.ylabel('Cantidad de Productos')
            plt.tight_layout()
            plt.savefig('reportes/precios.png')
            plt.close()
            print("✓ Gráfico de precios generado\n")

        except Exception as e:
            print(f"❌ Error generar_grafico_precios: {e}")
