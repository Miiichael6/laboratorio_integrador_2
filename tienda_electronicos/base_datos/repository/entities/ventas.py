from typing import TypedDict
class Venta(TypedDict):
    id: int               # ^ ID único de la venta
    fecha: str            # ^ Fecha de la transacción
    cliente_id: int       # ^ ID del cliente
    cliente_nombre: str   # ^ Nombre del cliente
    subtotal: float       # ^ Monto antes del descuento
    descuento_pct: float  # ^ Descuento aplicado (%)
    total: float          # ^ Monto final a pagar
