import matplotlib.pyplot as plt
import random

class GraphTemp:
    def createTemperature(self, x, y):
        plt.clf()
        # x axis values
        self.x = x
        # corresponding y axis values
        self.y = y

        # plotting the points
        plt.plot(self.x, self.y)

        # naming the x axis
        plt.xlabel('x - Time')
        # naming the y axis
        plt.ylabel('y - Temperature [C*]')

        # giving a title to my graph
        plt.title('Graph of temperature!')

        # function to show the plot
        # plt.show()
        file_name = 'temperature_graph'+str(random.randint(1,50000))+'.png'
        plt.savefig('static/graph/'+file_name, bbox_inches='tight')
        return file_name

    def createHumidity(self, x, y):
        plt.clf()
        # x axis values
        self.x = x
        # corresponding y axis values
        self.y = y

        # plotting the points
        plt.plot(self.x, self.y)

        # naming the x axis
        plt.xlabel('x - Time')
        # naming the y axis
        plt.ylabel('y - Humidity [%]')

        # giving a title to my graph
        plt.title('Graph of humidity!')

        # function to show the plot
        # plt.show()
        file_name = 'humidity_graph'+str(random.randint(1, 50000)) + '.png'
        plt.savefig('static/graph/' + file_name, bbox_inches='tight')
        return file_name
