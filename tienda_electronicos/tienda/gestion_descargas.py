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
           def cargar(ruta):
               if not os.path.exists(ruta) or os.path.getsize(ruta) == 0:
                   return None
               df = pd.read_csv(ruta)
               return df if not df.empty else None

           productos = cargar("tienda_electronicos/download/productos.csv")
           ventas = cargar("tienda_electronicos/download/ventas.csv")

           if productos is not None:
               print("\n========================== Productos ==========================")
               print(tabulate(productos.head(), headers="keys", tablefmt="fancy_grid", showindex=False))
           else:
               print("\n⚠ No hay productos.")

           if ventas is not None:
               print("\n========================== Ventas ===========================")
               print(tabulate(ventas.head(), headers="keys", tablefmt="fancy_grid", showindex=False))
           else:
               print("\n⚠ No hay ventas.")

           print("\n" + "-"*70)

       except Exception as e:
           print(f"❌ Error mostrar_contenido_reportes: {e}")
