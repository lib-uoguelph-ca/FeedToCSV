import csv
import os.path
from .csv_writer import CSVWriter

class CSVDictWriter(CSVWriter):

    def write(self, data):
        new_file = False

        if not os.path.isfile(self.out_file_path):
            new_file = True

        with open(self.out_file_path, 'wb') as f:
            fields = data.keys()
            writer = csv.DictWriter(f, fieldnames=fields)

            if new_file:
                writer.writeheader()

            writer.writerows(data)