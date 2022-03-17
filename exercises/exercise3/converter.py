
import linecache

class CsvConverter:

    def __init__(self, header):
        self.header = header # linecache.getline(file_name, 1).rstrip('\n').split(',')

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
        json = []
        for line in lines:
            assert len(line.split(',')) == len(self.header)

            # line_content = {head: val for head, val in zip(self.header, line.split(','))}
            line_content = dict(zip(self.header, line.split(',')))
            json.append(line_content)

        return json





def main():
    file_name = "dSST.csv"
    header = linecache.getline(file_name, 1).rstrip('\n').split(',')
    content = []
    count = 0
    with open(file_name) as fh:
        for line in fh:
            if count != 0:
                content.append(line)
            count += 1

    # print(content)

    csv_converter = CsvConverter(header)
    json = csv_converter.csv_to_json(content)


    # print(linecache.getline(file_name, 1).rstrip('\n').split(','))

if __name__ == "__main__":
    main()