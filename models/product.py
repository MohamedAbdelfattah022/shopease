from config.database_config import STORAGE
from core.db_connection import DatabaseConnection
from core.file_manager import FileManager


class Product:
    """
    NOTE: same problem as User -- the model is mixed up with
    SQL, CSV parsing and the storage switch. Copy-pasted logic.
    """

    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    @staticmethod
    def get_all():
        if STORAGE == "mysql":
            db = DatabaseConnection().get_connection()
            cursor = db.cursor(dictionary=True)
            cursor.execute("SELECT id, name, price FROM products")

            products = []
            for r in cursor.fetchall():
                products.append(Product(r["id"], r["name"], float(r["price"])))
            return products

        rows = FileManager().read_csv("data/products.csv")
        products = []
        for r in rows:
            products.append(Product(int(r["id"]), r["name"], float(r["price"])))
        return products

    @staticmethod
    def get_by_id(id):
        if STORAGE == "mysql":
            db = DatabaseConnection().get_connection()
            cursor = db.cursor(dictionary=True)
            cursor.execute("SELECT id, name, price FROM products WHERE id=%s", (id,))

            r = cursor.fetchone()
            if r:
                return Product(r["id"], r["name"], float(r["price"]))
            return None

        rows = FileManager().read_csv("data/products.csv")
        for r in rows:
            if int(r["id"]) == id:
                return Product(int(r["id"]), r["name"], float(r["price"]))
        return None
