class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    @staticmethod
    def get_all():
        return [
            Product(1, "Laptop", 1200.0),
            Product(2, "Mouse", 25.0),
        ]
