from typing import TypedDict
class Cliente(TypedDict):
    id: int      # ^ ID único del cliente
    nombre: str  # ^ Nombre del cliente
    tipo: str    # ^ Tipo de cliente (regular / premium)
