from typing import TypedDict

class DetalleVenta(TypedDict):
    id: int
    venta_id: int
    producto_nombre: str
    precio_unitario: float
    cantidad: int
    subtotal: float
