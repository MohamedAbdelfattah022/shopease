from core.db_connection import DatabaseConnection
from core.file_manager import FileManager


class MySQLUserRepository:
    def __init__(self):
        self.db = DatabaseConnection().get_connection()

    def get_all(self):
        cursor = self.db.cursor(dictionary=True)
        cursor.execute("SELECT id, name, email FROM users")

        return cursor.fetchall()

    def get_by_id(self, id):
        cursor = self.db.cursor(dictionary=True)
        cursor.execute("SELECT id, name, email FROM users WHERE id=%s", (id,))

        return cursor.fetchone()


class CSVUserRepository:
    def __init__(self):
        self.file = FileManager()

    def get_all(self):
        rows = self.file.read_csv("data/users.csv")
        users = []

        for r in rows:
            user = {
                "id": int(r["id"]),
                "name": r["name"],
                "email": r["email"]
            }

            users.append(user)

        return users

    def get_by_id(self, id):
        users = self.get_all()

        for row in users:
            if row["id"] == id:
                return row

        return None