from typing import TypedDict
class Producto(TypedDict):
    id: int         # ^ ID único del producto
    nombre: str     # ^ Nombre del producto
    precio: float   # ^ Precio unitario
    stock: int      # ^ Cantidad disponible
    categoria: str  # ^ Categoría del producto
