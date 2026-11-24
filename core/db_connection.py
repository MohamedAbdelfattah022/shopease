import mysql.connector
from config.database_config import MYSQL_CONFIG


class DatabaseConnection:

    def __init__(self):
        self.connection = mysql.connector.connect(**MYSQL_CONFIG)
        # self.connection = mysql.connector.connect(
        #     host=MYSQL_CONFIG["host"],
        #     user=MYSQL_CONFIG["user"],
        #     password=MYSQL_CONFIG["password"],
        #     database=MYSQL_CONFIG["database"]
        # )

    def get_connection(self):
        return self.connection
