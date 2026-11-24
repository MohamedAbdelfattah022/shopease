from config.database_config import STORAGE
from repositories.user_repository import MySQLUserRepository, CSVUserRepository


class User:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email

    @staticmethod
    def _repo():
        if STORAGE == "mysql":
            return MySQLUserRepository()

        return CSVUserRepository()

    @staticmethod
    def get_all():
        rows = User._repo().get_all()
        users = []

        for row in rows:
            user = User(
                row["id"],
                row["name"],
                row["email"]
            )

            users.append(user)

        return users

    @staticmethod
    def get_by_id(id):
        row = User._repo().get_by_id(id)

        if row:
            user = User(
                row["id"],
                row["name"],
                row["email"]
            )

            return user

        return None