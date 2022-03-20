from reader import Reader

class AverageMonth:

    def __init__(self):
        self.reader = Reader()


    def get_avg_months(self):
        data = self.reader.get_line()

        flag = True
        sum_temp_months = {}
        n_years = 0
        while flag:
            data = self.reader.get_line()
            if data == "":
                flag = False
            else:
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


if __name__ == "__main__":
    # reader = Reader()
    average_month = AverageMonth()
    avg_temp_months = average_month.get_avg_months()
    print(f"Average temperature each month: {avg_temp_months}")