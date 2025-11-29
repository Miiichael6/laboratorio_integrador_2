# ========================================================================
# GRÁFICOS Y REPORTES (LÍDER DE INTEGRACIÓN)
# ========================================================================
import matplotlib.pyplot as plt
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .tienda_electronicos_gestor import ElectronicosGestion

class TiendaGestionGraficosYReportes:

    def generar_grafico_ventas_diarias(self: "ElectronicosGestion"):
        """Genera gráfico de ventas por día."""
        if not self.ventas:
            print("❌ No hay ventas para graficar")
            return

        try:
            fechas = [v['fecha'].date() for v in self.ventas]
            totales = [v['total'] for v in self.ventas]

            plt.figure(figsize=(10, 6))
            plt.plot(fechas, totales, marker='o', color='blue', linewidth=2)
            plt.title('Ventas Diarias - Electronicos', fontsize=14, fontweight='bold')
            plt.xlabel('Fecha')
            plt.ylabel('Total (S/)')
            plt.xticks(rotation=45)
            plt.grid(True, alpha=0.3)
            plt.tight_layout()
            plt.savefig('reportes/ventas_diarias.png')
            plt.close()
            print("✓ Gráfico de ventas generado\n")

        except Exception as e:
            print(f"❌ Error: {e}")

    def generar_grafico_productos_vendidos(self: "ElectronicosGestion"):
        """Genera gráfico de productos más vendidos."""
        try:
            conn = sqlite3.connect('base_datos/negocio.db')
            cursor = conn.cursor()

            cursor.execute('''
            SELECT producto_nombre, SUM(cantidad) as total
            FROM detalle_ventas
            GROUP BY producto_nombre
            ORDER BY total DESC
            LIMIT 10
            ''')

            resultados = cursor.fetchall()
            conn.close()

            if not resultados:
                print("❌ No hay datos")
                return

            productos = [r[0][:15] for r in resultados]
            cantidades = [r[1] for r in resultados]

            plt.figure(figsize=(10, 6))
            plt.barh(productos, cantidades, color='green')
            plt.title('Productos Más Vendidos', fontsize=14, fontweight='bold')
            plt.xlabel('Cantidad Vendida')
            plt.tight_layout()
            plt.savefig('reportes/productos_vendidos.png')
            plt.close()
            print("✓ Gráfico de productos generado\n")

        except Exception as e:
            print(f"❌ Error: {e}")

    def generar_grafico_categorias(self: "ElectronicosGestion"):
        """Genera gráfico de ventas por categoría."""
        try:
            conn = sqlite3.connect('base_datos/negocio.db')
            cursor = conn.cursor()

            cursor.execute('''
            SELECT
                p.categoria,
                SUM(dv.subtotal) as ingresos
            FROM detalle_ventas dv
            JOIN productos p ON dv.producto_nombre = p.nombre
            GROUP BY p.categoria
            ''')

            resultados = cursor.fetchall()
            conn.close()

            if not resultados:
                print("❌ No hay datos")
                return

            categorias = [r[0] for r in resultados]
            ingresos = [r[1] for r in resultados]

            plt.figure(figsize=(10, 6))
            plt.pie(ingresos, labels=categorias, autopct='%1.1f%%', startangle=90)
            plt.title('Ingresos por Categoría', fontsize=14, fontweight='bold')
            plt.tight_layout()
            plt.savefig('reportes/categorias.png')
            plt.close()
            print("✓ Gráfico de categorías generado\n")

        except Exception as e:
            print(f"❌ Error: {e}")

    def generar_grafico_clientes(self: "ElectronicosGestion"):
        """Genera gráfico de clientes más frecuentes."""
        try:
            conn = sqlite3.connect('base_datos/negocio.db')
            cursor = conn.cursor()

            cursor.execute('''
            SELECT cliente_nombre, COUNT(*) as compras
            FROM ventas
            GROUP BY cliente_nombre
            ORDER BY compras DESC
            LIMIT 10
            ''')

            resultados = cursor.fetchall()
            conn.close()

            if not resultados:
                print("❌ No hay datos")
                return

            clientes = [r[0] for r in resultados]
            compras = [r[1] for r in resultados]

            plt.figure(figsize=(10, 6))
            plt.bar(clientes, compras, color='orange')
            plt.title('Clientes Más Frecuentes', fontsize=14, fontweight='bold')
            plt.ylabel('Número de Compras')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.savefig('reportes/clientes.png')
            plt.close()
            print("✓ Gráfico de clientes generado\n")

        except Exception as e:
            print(f"❌ Error: {e}")

    def generar_grafico_precios(self: "ElectronicosGestion"):
        """Genera histograma de precios."""
        try:
            precios = [precio for _, precio, _, _ in self.catalogo]

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
            print(f"❌ Error: {e}")
