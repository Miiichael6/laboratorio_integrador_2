from typing import TypedDict
class DetalleVenta(TypedDict):
    id: int                 # ^ ID único del detalle
    venta_id: int           # ^ ID de la venta asociada
    producto_nombre: str    # ^ Nombre del producto
    precio_unitario: float  # ^ Precio por unidad
    cantidad: int           # ^ Unidades vendidas
    subtotal: float         # ^ Total (precio_unitario * cantidad)
