# from asyncore import read
import json
import linecache
import time
from converter import CsvConverter
# from average_year import AverageYear
# from average_month import AverageMonth

class Reader:

    def __init__(self, file="dSST.csv"):
        self._observers = set()

        self.file = file
        self.header = linecache.getline(file, 1).rstrip('\n').split(',')
        self.csv_converter = CsvConverter(self.header)

        self.current_line = 2

    def get_line(self, n:int=5) -> list:
        """
        Get n lines of a csv file and return it in json format. 

        :parameters
        -----------
        n - int
            Number of lines
        
        :returns
        --------
        json_content - list
            Data in json format
        """
        lines = []
        for _ in range(n):
            line = linecache.getline(self.file, self.current_line)
            if line == '':
                return ''
            lines.append(line)
            self.current_line += 1
            
        self.json_content = self.csv_converter.csv_to_json(lines)
        time.sleep(5)
        self.notify_observers()

    def get_json_content(self):
         return self.json_content
        

    def add_observer(self, obs):
        self._observers.add(obs)

    def remove_observer(self, obs):
        try:
            self._observers.remove(obs)
        except KeyError as e:
            print(f"Observer:{obs} does not exists and can't be removed.")

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self)


class AverageYear:

    def __init__(self):
        self.reader = Reader()


    def get_avg_year(self, data):

        # flag = True
        # avg_temp_all = []
        # while flag:
        #     data = self.reader.get_line()
        #     if data == "":
        #         flag = False
        #     else:
        avg_temp_years = []
        for line in data:
            sum_temp = 0.0
            temps = list(line.values())[1:13] # Get the temperatures
            # Sum the different temps
            for temp in temps:
                sum_temp += float(temp)
            
            avg_temp = sum_temp / len(temps) # Create average
            avg_temp_years.append(avg_temp)
            # Add to total list
            # avg_temp_all += avg_temp_years

        return avg_temp_years


    def update(self, other):
        if other.__class__.__name__ == "Reader":
            json_content = other.get_json_content()
            avg_temp_all = self.get_avg_year(json_content)
            print(f"Average temperature all years: {avg_temp_all}")




class AverageMonth:

    def __init__(self):
        self.reader = Reader()


    def get_avg_months(self, data):
        # data = self.reader.get_line()

        flag = True
        sum_temp_months = {}
        n_years = 0
        # while flag:
        #     data = self.reader.get_line()
        #     if data == "":
        #         flag = False
        #     else:
        for line in data:
            n_years += 1

            for month, temp in list(line.items())[1:13]:
                if month not in sum_temp_months:
                    sum_temp_months[month] = float(temp)
                else:
                    sum_temp_months[month] = float(temp)

        # Calculate the average temp for each month over all years
        avg_temp_months = {key: value / n_years for key, value in sum_temp_months.items()}

        return avg_temp_months

    def update(self, other):
        if other.__class__.__name__ == "Reader":
            json_content = other.get_json_content()
            avg_temp_months = self.get_avg_months(json_content)
            print(f"Average temperature all months: {avg_temp_months}")

if __name__ == "__main__":
    reader = Reader()

    cons1 = AverageYear()
    cons2 = AverageMonth()
    reader.add_observer(cons1)
    reader.add_observer(cons2)

    reader.get_line()
    #print(json_content_1)