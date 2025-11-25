from ..database_gestor import DatabaseGestor

class BaseRepository:
    def __init__(self, gestor: DatabaseGestor, table: str, id_column="id"):
        self.db = gestor
        self.table = table
        self.id_column = id_column

    def create(self, data: dict):
        return self.db.insert(self.table, data)

    def find_all(self):
        return self.db.find_all(self.table)

    def find_by_id(self, id_value):
        return self.db.find_by_id(self.table, id_value, self.id_column)

    def update(self, id_value, data: dict):
        return self.db.update(self.table, id_value, data, self.id_column)

    def delete(self, id_value):
        return self.db.delete(self.table, id_value, self.id_column)
