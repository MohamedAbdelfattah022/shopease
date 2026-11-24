import csv

class FileManager:
    def read_csv(self, path):
        with open(path) as f:
            return list(csv.DictReader(f))
