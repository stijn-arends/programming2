
class CsvConverter:

    def __init__(self, header):
        self.header = header.split(',')

    def csv_to_json(self, lines):
        """
        Takes lines in CSV format and turns into json format. 
        """
        json = []
        for line in lines:
            vals = line.split(',')
            json_dict = {}
            assert len(vals) == len(self.header)
            for item, header in zip(vals, self.header):
                json_dict[header] = float(item)

            json.append(json_dict)

        return json


# print(f"Name of the file: {__name__}")


if __name__ == "__main__":
    csv_line = "a,b,c,d,e,f,g,f,a,s,g,h"
    print(f"CSV line: {csv_line}")
    print(f"Split: {csv_line.split(',')}")
    print(len(csv_line.split(',')))


