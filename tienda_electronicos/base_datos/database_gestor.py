import sqlite3
from pathlib import Path

class DatabaseGestor:
    def __init__(self, db_path="tienda_electronicos/base_datos/db/negocio.db"):
        self.db_path = Path(db_path)             # ruta del archivo
        self.db_path.parent.mkdir(parents=True, exist_ok=True)  # crea carpetas
        self.connect()  # opcional: solo para probar que se puede conectar

    def connect(self):
        return sqlite3.connect(self.db_path)


    def execute(self, query, params=()):
        conn = self.connect()
        cur = conn.cursor()
        try:
            cur.execute(query, params)
            conn.commit()
            return cur
        finally:
            conn.close()

    def select(self, query, params=()):
        conn = self.connect()
        cur = conn.cursor()
        try:
            cur.execute(query, params)
            return cur.fetchall()
        finally:
            conn.close()

    def select_one(self, query, params=()):
        """Ejecuta SELECT y devuelve una sola fila"""
        conn = self.connect()
        cur = conn.cursor()
        try:
            cur.execute(query, params)
            return cur.fetchone()[0]
        finally:
            conn.close()

    def insert(self, table, data: dict):
        columns = ", ".join(data.keys())
        placeholders = ", ".join(["?"] * len(data))
        values = tuple(data.values())

        query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
        conn = self.connect()
        cur = conn.cursor()
        try:
            cur.execute(query, values)
            conn.commit()
            last_id = cur.lastrowid  # obtiene el ID del registro insertado
            # devuelve la fila completa recién creada
            cur.execute(f"SELECT * FROM {table} WHERE id = ?", (last_id,))
            return cur.fetchone()
        finally:
            conn.close()

    def find_all(self, table):
        query = f"SELECT * FROM {table}"
        return self.select(query)

    def find_by_id(self, table, id_value, id_column="id"):
        query = f"SELECT * FROM {table} WHERE {id_column} = ?"
        return self.select(query, (id_value,))

    def update(self, table, id_value, data: dict, id_column="id"):
        set_clause = ", ".join([f"{col} = ?" for col in data.keys()])
        values = tuple(data.values()) + (id_value,)

        query = f"UPDATE {table} SET {set_clause} WHERE {id_column} = ?"
        self.execute(query, values)

    def delete(self, table, id_value, id_column="id"):
        query = f"DELETE FROM {table} WHERE {id_column} = ?"
        self.execute(query, (id_value,))
