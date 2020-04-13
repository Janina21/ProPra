from view import View
from wall import Wall
from wallFactory import WallFactory
from wallAdministration import WallAdministration


class Room:
    coordinates = None
    wallFactory = WallFactory()
    wallAdministration = None
    walls = None

    def __init__(self, coordinates: list):

        self.coordinates = coordinates

    def draw(self):
        self.get_all_walls()
        view = View()
        view.draw_line(self.wallFactory.set_all_x_and_y_values_in_right_order()[
            0], self.wallFactory.set_all_x_and_y_values_in_right_order()[1])

    def get_all_walls(self):
        self.walls = self.wallFactory.create_all_walls(self.coordinates)
        self.wallAdministration = WallAdministration(self.walls)
