from typing import Generic, TypeVar, List, Optional, Dict, Any
from tienda_electronicos.base_datos.database_gestor import DatabaseGestor

T = TypeVar("T", bound=Dict[str, Any])  # un diccionario con claves string

class BaseRepository(Generic[T]):
    def __init__(self, gestor: DatabaseGestor, table: str, id_column: str = "id"):
        self.db = gestor
        self.table = table
        self.id_column = id_column

    def create(self, data: dict) -> T:
        return self.db.insert(self.table, data)

    def find_all(self) -> List[T]:
        return self.db.find_all(self.table)

    def find_by_id(self, id_value) -> Optional[T]:
        rows = self.db.find_by_id(self.table, id_value, self.id_column)
        return rows[0] if rows else None

    def update(self, id_value, data: dict) -> None:
        self.db.update(self.table, id_value, data, self.id_column)

    def delete(self, id_value) -> None:
        self.db.delete(self.table, id_value, self.id_column)
