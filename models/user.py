from config.database_config import STORAGE
from core.db_connection import DatabaseConnection
from core.file_manager import FileManager


class User:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email

    @staticmethod
    def get_all():
        if STORAGE == "mysql":
            db = DatabaseConnection().get_connection()
            cursor = db.cursor(dictionary=True)
            cursor.execute("SELECT id, name, email FROM users")

            users = []
            for r in cursor.fetchall():
                users.append(User(r["id"], r["name"], r["email"]))
            return users

        rows = FileManager().read_csv("data/users.csv")
        users = []
        for r in rows:
            users.append(User(int(r["id"]), r["name"], r["email"]))
        return users

    @staticmethod
    def get_by_id(id):
        if STORAGE == "mysql":
            db = DatabaseConnection().get_connection()
            cursor = db.cursor(dictionary=True)
            cursor.execute("SELECT id, name, email FROM users WHERE id=%s", (id,))

            r = cursor.fetchone()
            if r:
                return User(r["id"], r["name"], r["email"])
            return None

        rows = FileManager().read_csv("data/users.csv")
        for r in rows:
            if int(r["id"]) == id:
                return User(int(r["id"]), r["name"], r["email"])
        return None
