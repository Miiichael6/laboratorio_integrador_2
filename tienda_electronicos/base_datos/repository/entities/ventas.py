from typing import TypedDict

class Venta(TypedDict):
    id: int
    fecha: str
    cliente_id: int
    cliente_nombre: str
    subtotal: float
    descuento_pct: float
    total: float
