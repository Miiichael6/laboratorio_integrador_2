import sqlite3
from pathlib import Path

class DatabaseGestor:
    def __init__(self, db_path="tienda_electronicos/base_datos/db/negocio.db"):
        self.db_path = Path(db_path)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)

    def connect(self):
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row 
        return conn

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
            rows = cur.fetchall()
            return [dict(row) for row in rows]
        finally:
            conn.close()

    def select_one(self, query, params=()):
        conn = self.connect()
        cur = conn.cursor()
        try:
            cur.execute(query, params)
            row = cur.fetchone()
            return dict(row) if row else None
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
            last_id = cur.lastrowid
            cur.execute(f"SELECT * FROM {table} WHERE id = ?", (last_id,))
            row = cur.fetchone()
            return dict(row)  # <- devolver dict
        finally:
            conn.close()

    def find_all(self, table):
        query = f"SELECT * FROM {table}"
        return self.select(query)

    def find_by_id(self, table, id_value, id_column="id"):
        query = f"SELECT * FROM {table} WHERE {id_column} = ?"
        rows = self.select(query, (id_value,))
        return rows[0] if rows else None

    def update(self, table, id_value, data: dict, id_column="id"):
        set_clause = ", ".join([f"{col} = ?" for col in data.keys()])
        values = tuple(data.values()) + (id_value,)
        query = f"UPDATE {table} SET {set_clause} WHERE {id_column} = ?"
        self.execute(query, values)

    def delete(self, table, id_value, id_column="id"):
        query = f"DELETE FROM {table} WHERE {id_column} = ?"
        self.execute(query, (id_value,))
