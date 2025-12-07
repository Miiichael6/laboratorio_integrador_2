# ========================================================================
# DESCARGAS (DESCARGAS)
# ========================================================================
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .tienda_electronicos_gestor import ElectronicosGestion

class TiendaGestionDescargas:

    def descargar_catalogo_csv(self: "ElectronicosGestion"):
        try:
            pass
        except Exception as e:
            print(f"❌ Error descargar_catalogo_csv: {e}")

    def descargar_ventas_csv(self: "ElectronicosGestion"):
        try:
            pass
        except Exception as e:
            print(f"❌ Error descargar_ventas_csv: {e}")
    
    def mostrar_contenido_reportes(self: "ElectronicosGestion"):
        try:
            pass
        except Exception as e:
            print(f"❌ Error mostrar_contenido_reportes: {e}")

