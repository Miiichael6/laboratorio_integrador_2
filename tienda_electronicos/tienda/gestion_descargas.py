# ========================================================================
# DESCARGAS (DESCARGAS)
# ========================================================================
from typing import TYPE_CHECKING
from tabulate import tabulate
import pandas as pd

if TYPE_CHECKING:
    from .tienda_electronicos_gestor import ElectronicosGestion

class TiendaGestionDescargas:

    def descargar_catalogo_csv(self: "ElectronicosGestion"):
        try:
            productos = self.productos_repository.find_all()  # lista de dicts
            df = pd.DataFrame(productos)
            df.to_csv("tienda_electronicos/download/productos.csv", index=False)
            print("📁 Catálogo exportado.")
        except Exception as e:
            print(f"❌ Error descargar_catalogo_csv: {e}")

    def descargar_ventas_csv(self: "ElectronicosGestion"):
        try:
            ventas = self.ventas_repository.find_all()  # lista de dicts
            df = pd.DataFrame(ventas)
            df.to_csv("tienda_electronicos/download/ventas.csv", index=False)
            print("📁 Ventas exportadas.")
        except Exception as e:
            print(f"❌ Error descargar_ventas_csv: {e}")

    def mostrar_contenido_reportes(self: "ElectronicosGestion"):
        try:
            productos = pd.read_csv("tienda_electronicos/download/productos.csv").head()
            ventas = pd.read_csv("tienda_electronicos/download/ventas.csv").head()

            print("\n========================== Productos ==========================")
            print(tabulate(productos, headers="keys", tablefmt="fancy_grid", showindex=False))

            print("\n========================== Ventas ===========================")
            print(tabulate(ventas, headers="keys", tablefmt="fancy_grid", showindex=False))

            print("\n" + "-"*70)

        except Exception as e:
            print(f"❌ Error mostrar_contenido_reportes: {e}")
