import matplotlib.pyplot as plt

class GraphTemp:
    def __init__(self, start_time=None, end_time=None):
        self._start_time = start_time
        self._end_time = end_time

    def create(self):
        # x axis values
        x = [1, 2, 3]
        # corresponding y axis values
        y = [2, 4, 1]

        # plotting the points
        plt.plot(x, y)

        # naming the x axis
        plt.xlabel('x - axis')
        # naming the y axis
        plt.ylabel('y - axis')

        # giving a title to my graph
        plt.title('My first graph!')

        # function to show the plot
        # plt.show()
        plt.savefig('graph.png', bbox_inches='tight')

