# from asyncore import read
import json
import linecache
import time

# from average_year import AverageYear
import average_year  # this will avoid the import loop error. You can also import this function inside of the __init__ function
from converter import CsvConverter
from plot import PlotView

# from average_month import AverageMonth

# Exercise: https://www.bartbarnard.nl/programming2/exercise3.html

__author__ = "Stijn Arends"
__date__ = "17-3-2022"
__version__ = "v.01"


class Reader:
    """
    Class to read a CSV file
    """

    def __init__(self, file="dSST.csv"):
        self._observers = set()

        self.file = file
        self.header = linecache.getline(file, 1).rstrip("\n").split(",")
        self.csv_converter = CsvConverter(self.header)

        self.current_line = 2

    def get_line(self, n_lines: int = 5) -> None:
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
        for _ in range(n_lines):
            line = linecache.getline(self.file, self.current_line)
            if line == "":
                return ""
            lines.append(line)
            self.current_line += 1

        self.json_content = self.csv_converter.csv_to_json(lines)
        time.sleep(5)
        self.notify_observers()

    def get_json_content(self):
        """
        Get the json content that is available

        :returns
        --------
        json_content - list
            CSV data in json format
        """
        return self.json_content

    def add_observer(self, obs) -> None:
        """
        Add new observer to the set

        :parameters
        -----------
        obs - class
            A class that needs to be notified
        """
        self._observers.add(obs)

    def remove_observer(self, obs) -> None:
        """
        Remove an observer from the set.

        :parameters
        -----------
        obs - class
            A class that does not need to be notified anymore
        """
        try:
            self._observers.remove(obs)
        except KeyError:
            print(f"Observer:{obs} does not exists and can't be removed.")

    def notify_observers(self) -> None:
        """
        Notify the observers that something has changed/ is ready.
        """
        for observer in self._observers:
            observer.update(self)


class AverageYear:
    """
    Class to calculate the average temperature per year
    """

    def __init__(self):
        self.reader = Reader()
        self.plot_view = PlotView()

    def get_avg_year(self, data):
        """
        Get the average temperature for each year.

        :parameters
        -----------
        data - list
            List of json data containing the temps for each month for several years

        :returns
        --------
        avg_temp_years - dict
            The average temperature per year
        """

        # flag = True
        # avg_temp_all = []
        # while flag:
        #     data = self.reader.get_line()
        #     if data == "":
        #         flag = False
        #     else:
        avg_temp_year = dict()
        for line in data:
            sum_temp = 0.0
            temps = list(line.values())[1:13]  # Get the temperatures
            # Sum the different temps
            year = list(line.values())[0]
            for temp in temps:
                sum_temp += float(temp)

            avg_temp = sum_temp / len(temps)  # Create average
            avg_temp_year[year] = avg_temp

        return avg_temp_year

    def update(self, other):
        """
        Update stuff
        """
        if other.__class__.__name__ == "Reader":
            json_content = other.get_json_content()
            avg_temp_all = self.get_avg_year(json_content)
            print(f"Average temperature all years: {avg_temp_all}")
            self.plot_view.draw(list(avg_temp_all.keys()), list(avg_temp_all.values()))


class AverageMonth:
    """
    Class to calculate the average temperature per month over several years
    """

    def __init__(self):
        self.reader = Reader()
        self.plot_view = PlotView()

    def get_avg_months(self, data):
        """
        Get teh average temp per month
        """
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
        avg_temp_months = {
            key: value / n_years for key, value in sum_temp_months.items()
        }

        return avg_temp_months

    def update(self, other):
        """
        Update stuff
        """
        if other.__class__.__name__ == "Reader":
            json_content = other.get_json_content()
            avg_temp_months = self.get_avg_months(json_content)
            print(f"Average temperature all months: {avg_temp_months}")
            self.plot_view.draw(
                list(avg_temp_months.keys()), list(avg_temp_months.values())
            )


if __name__ == "__main__":
    reader = Reader()

    cons1 = AverageYear()
    cons2 = AverageMonth()
    reader.add_observer(cons1)
    reader.add_observer(cons2)

    reader.get_line()
    # print(json_content_1)
