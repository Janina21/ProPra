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
        self.verticalWallAdministration.set_start_ranges()
        while len(self.horizontalWallAdministration.horizontal_walls) > 0:
            self.horizontalWallAdministration.separate_north_and_south_walls()
        # for i in range(len(self.horizontalWallAdministration.get_north_walls())):
        #     print(self.horizontalWallAdministration.get_north_walls()
        #           [i].get_range())
        # print("--------------------------------------------------------------------")
        while len(self.verticalWallAdministration.vertical_walls) > 0:
            self.verticalWallAdministration.separate_west_and_east_walls()
        # for i in range(len(self.verticalWallAdministration.get_east_walls())):
        #     print(self.verticalWallAdministration.get_east_walls()
        #           [i].get_range())
        self.horizontalWallAdministration.set_new_ranges_for_north_walls()
        for i in range(len(self.horizontalWallAdministration.get_north_walls())):
            print(self.horizontalWallAdministration.get_north_walls()
                  [i].get_range())
            print(self.horizontalWallAdministration.get_north_walls()
                  [i].get_new_range())
            print(
                "-------------------------------------------------------------------------")

    def north_search(self):
        pass

    def south_search(self):
        pass

    def east_search(self):
        pass

    def west_search(self):
        pass
