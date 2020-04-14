from verticalWallAdministration import VerticalWallAdministration
from horizontalWallAdministration import HorizontalWallAdministration


class WallAdministration:

    walls = None
    horizontalWallAdministration = HorizontalWallAdministration()
    verticalWallAdministration = VerticalWallAdministration()

    def __init__(self, walls):
        self.walls = walls

    def split_horizontal_and_vertical_walls(self):
        for i in range(len(self.walls)):
            if self.walls[i].get_coordinate1()[0] == self.walls[i].get_coordinate2()[0]:
                self.verticalWallAdministration.append_vertical_wall(
                    self.walls[i])
            else:
                self.horizontalWallAdministration.append_horizontal_wall(
                    self.walls[i])
        self.setup()

    def setup(self):
        self.horizontalWallAdministration.set_start_ranges()
        self.horizontalWallAdministration.find_all_definitely_north_walls()
        self.horizontalWallAdministration.find_all_definitely_south_walls()
        self.verticalWallAdministration.set_start_ranges()
        self.verticalWallAdministration.find_all_definitely_east_walls()
        self.verticalWallAdministration.find_all_definitely_west_walls()

    def get_definite_walls(self):
        self.split_horizontal_and_vertical_walls()

        for i in range(len(self.horizontalWallAdministration.get_south_walls())):
            self.horizontalWallAdministration.check_wall(
                self.horizontalWallAdministration.get_south_walls()[i])
            print(self.horizontalWallAdministration.get_south_walls()
                  [i].get_range())
            print(self.horizontalWallAdministration.get_south_walls()
                  [i].get_new_range())

    # def get_south_partner_wall(self):
    #     rectangle_north = {}
    #     for i in range(len(self.horizontalWallAdministration.get_north_walls())):
    #         print(self.horizontalWallAdministration.get_north_walls()
    #               [i].get_range())

    def north_search(self):
        pass

    def south_search(self):
        pass

    def east_search(self):
        pass

    def west_search(self):
        pass
