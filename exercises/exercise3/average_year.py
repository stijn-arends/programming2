
from reader import Reader

class AverageYear:

    def __init__(self):
        self.reader = Reader()


    def get_avg_year(self):

        flag = True
        avg_temp_all = []
        while flag:
            data = self.reader.get_line()
            if data == "":
                flag = False
            else:
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
                    avg_temp_all += avg_temp_years

        return avg_temp_all


if __name__ == "__main__":
    # reader = Reader()
    average_year = AverageYear()
    avg_temp_all = average_year.get_avg_year()
    print(f"Average temperature all years: {avg_temp_all}")
