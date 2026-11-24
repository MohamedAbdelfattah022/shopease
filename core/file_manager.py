import csv

class FileManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance

    def read_csv(self, path):
        with open(path) as f:
            return list(csv.DictReader(f))
