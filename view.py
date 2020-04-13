import matplotlib.pyplot as plt


class View:

    def draw_line(self, x_values, y_values):

        plt.plot(x_values, y_values)
        # plt.plot([2.5, 1, 1, 2.5, 2.5], [5, 5, 6, 6, 5])
        # plt.axis([x_min, x_max, y_min, y_max])
        plt.show()

    def draw_multiple_points(self, x_list, y_list):
        plt.scatter(x_list, y_list)
        plt.show()
