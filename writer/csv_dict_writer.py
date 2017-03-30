import csv
import os.path
from .csv_writer import CSVWriter

class CSVDictWriter(CSVWriter):

    def write(self, data):
        new_file = False

        if not os.path.isfile(self.out_file_path):
            new_file = True

        with open(self.out_file_path, 'a') as f:
            fields = list(data.keys()).sort()
            writer = csv.DictWriter(f, fieldnames=fields)

            if new_file:
                writer.writeheader()

            writer.writerow(data)