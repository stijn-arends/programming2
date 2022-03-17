from asyncore import read
import linecache

from converter import CsvConverter

class Reader:

    def __init__(self, file="dSST.csv"):
        self.file = file
        self.csv_converter = CsvConverter(file)

        self.current_line = 1

    def get_line(self, n:int=5) -> list:
        """
        :parameters
        -----------
        n - int
            Number of lines
        
        :returns
        --------
        json_content - list
            Data in json format
        """
        # lines = [linecache.getline(self.file, self.current_line) for _ in n]
        lines = []
        for _ in range(n):
            line = linecache.getline(self.file, self.current_line)
            if line == '':
                return ''
            lines.append(line)
            self.current_line += 1
            
        json_content = self.csv_converter.csv_to_json(lines)
        return json_content
        


if __name__ == "__main__":
    reader = Reader()
    json_content_1 = reader.get_line()
    json_content_1 = reader.get_line()








