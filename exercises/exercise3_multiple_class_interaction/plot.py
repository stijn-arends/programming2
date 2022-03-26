import matplotlib.pyplot as plt


class PlotView:

    def __init__(self):
        pass

    def draw(self, x, y) -> None:
        plt.plot(x, y)
        plt.show()