import matplotlib.pyplot as plt
import random

class GraphTemp:
    def __init__(self, start_time=None, end_time=None):
        self._start_time = start_time
        self._end_time = end_time
        self.x = []
        self.y = []

    def create(self, x, y):
        # x axis values
        self.x = x
        # corresponding y axis values
        self.y = y

        # plotting the points
        plt.plot(self.x, self.y)

        # naming the x axis
        plt.xlabel('x - axis')
        # naming the y axis
        plt.ylabel('y - axis')

        # giving a title to my graph
        plt.title('Graph of temperature!')

        # function to show the plot
        # plt.show()
        graph_name = 'temp_graph'+str(random.randint(1,50000))+'.png'
        plt.savefig('static/graph/'+graph_name, bbox_inches='tight')
        return graph_name