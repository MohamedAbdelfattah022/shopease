from config.database_config import STORAGE
from repositories.user_repository import MySQLUserRepository, CSVUserRepository


class RepositoryFactory:

    @staticmethod
    def get_repository(entity_type):
        if entity_type == "user":
            if STORAGE == "mysql":
                return MySQLUserRepository()

            return CSVUserRepository()

        raise ValueError("Unknown repository type")
