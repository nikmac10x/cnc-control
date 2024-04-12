from typing import List, Optional
import psycopg
from psycopg.rows import dict_row


from app.schemas.motors import Motor
from app.config import get_settings


class MotorRepository:
    def get_conn(self):
        return psycopg.connect(get_settings().psql_uri_db, row_factory=dict_row)

    def get_list(self):
        with self.get_conn() as conn:
            with conn.cursor() as cur:
                cur.execute('SELECT * FROM motors')
                return cur.fetchall()

    def get(self, id: int):
        try:
            with self.get_conn() as conn:
                with conn.cursor() as cur:
                    cur.execute("SELECT * FROM motors WHERE id = %s", [id])
                    return cur.fetchone()
        except Exception as e:
            return None

    def save(self, model):
        fields = []
        positions = []
        values = []

        for field in model.model_fields.keys():
            if not hasattr(model, field) or getattr(model, field) is None:
                continue
            fields.append(field)
            positions.append("%s")
            values.append(getattr(model, field))

        query = f"INSERT INTO motors"
        query += " (" + ", ".join(fields) + ") VALUES (" + ", ".join(positions) + ") RETURNING id"
        with self.get_conn() as conn:
            with conn.cursor() as cur:
                cur.execute(query, values)
                return cur.fetchone()

    def drop(self, id: int):
        with self.get_conn() as conn:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM motors WHERE id = %s", [id])