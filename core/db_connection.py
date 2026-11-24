import mysql.connector
from config.database_config import MYSQL_CONFIG


class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.connection = mysql.connector.connect(**MYSQL_CONFIG)

        return cls._instance

    def get_connection(self):
        return self.connection
