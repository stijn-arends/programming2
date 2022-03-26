"""
Converting CSV files into json format.
"""
import linecache
import json


class CsvConverter:
    """
    Convert CSV to json format
    """

    def __init__(self, header):
        self.header = header  # linecache.getline(file_name, 1).rstrip('\n').split(',')

    def csv_to_json(self, lines):
        """
        Convert CSV lines into json format.

        :parameters
        -----------
        lines - list
            List of CSV lines

        :returns
        --------
        json - list
            CSV data in json format
        """
        json_content = []
        test = []
        for line in lines:
            assert len(line.split(",")) == len(self.header)

            line_content = dict(zip(self.header, line.split(",")))
            json_content.append(line_content)
            test.append(line_content)

        # check = json.dumps(test)
        # check2 = json.loads(check)
        # print(check, '\n')
        # print(f"Check json dumps and laods: {check2}")
        # print(type(check2))

        return json_content


def main():
    """
    main func
    """
    # file_name = "dSST.csv"
    # header = linecache.getline(file_name, 1).rstrip("\n").split(",")
    # content = []
    # count = 0
    # with open(file_name, "r") as fh:
    #     for line in fh:
    #         if count != 0:
    #             content.append(line)
    #         count += 1

    # # print(content)

    # csv_converter = CsvConverter(header)
    # json = csv_converter.csv_to_json(content)



if __name__ == "__main__":
    main()
