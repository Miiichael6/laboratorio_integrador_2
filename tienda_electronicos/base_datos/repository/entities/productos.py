from typing import TypedDict

class Producto(TypedDict):
    id: int
    nombre: str
    precio: float
    stock: int
    categoria: str
