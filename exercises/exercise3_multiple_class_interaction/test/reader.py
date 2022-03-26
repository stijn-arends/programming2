from csv import reader
from converter import CsvConverter
import linecache


class Reader:

    def __init__(self, file="dSST.csv") -> None:
        self.file = file
        self.header = linecache.getline(self.file, 1)
        self.csv_converter = CsvConverter(self.header)
        self.count = 2

    def get_lines(self):
        
        lines = []
        for _ in range(5):
            line = linecache.getline(self.file, self.count)
            if line == "":
                return "" # use break instead
            lines.append(line)
            self.count += 1 

        json = self.csv_converter.csv_to_json(lines)
        return json


if __name__ == "__main__":
    reader = Reader()
    json_content = reader.get_lines()
    print(json_content)

        


