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
                print("else")
                self.horizontalWallAdministration.append_horizontal_wall(
                    self.walls[i])
        self.horizontalWallAdministration.set_start_ranges()
        self.verticalWallAdministration.set_start_ranges()

    def find_all_definitely_north_walls(self):

        self.horizontalWallAdministration.bring_all_ranges_in_right_order()

        for i in range(len(self.horizontalWallAdministration.get_walls())):
            north_wall = self.horizontalWallAdministration.horizontal_walls[i]
            horizontal_walls_in_same_range = self.horizontalWallAdministration.get_all_walls_between_range(
                self.horizontalWallAdministration.get_walls()[i].get_range())
            for j in range(len(horizontal_walls_in_same_range)):
                if horizontal_walls_in_same_range[j].get_coordinate1()[1] > north_wall.get_coordinate1()[1]:

                    north_wall = horizontal_walls_in_same_range[j]

            if north_wall not in self.horizontalWallAdministration.north_walls:
                self.horizontalWallAdministration.append_north_wall(north_wall)

    def find_all_definitely_south_walls(self):

        self.horizontalWallAdministration.bring_all_ranges_in_right_order()

        for i in range(len(self.horizontalWallAdministration.horizontal_walls)):
            south_wall = self.horizontalWallAdministration.horizontal_walls[i]
            horizontal_walls_in_same_range = self.horizontalWallAdministration.get_all_walls_between_range(
                self.horizontalWallAdministration.horizontal_walls[i].get_range())
            for j in range(len(horizontal_walls_in_same_range)):
                if horizontal_walls_in_same_range[j].get_coordinate1()[1] < south_wall.get_coordinate1()[1]:

                    south_wall = horizontal_walls_in_same_range[j]
            if south_wall not in self.horizontalWallAdministration.south_walls:
                self.horizontalWallAdministration.append_south_wall(south_wall)

    # def find_adjacent_walls(self, wall_list, list_of_walls):
    #     possible_adjacents = []
    #     adjacent_north_and_south_wall = {}

    #     for i in range(len(wall_list)):
    #         self.check_north_wall(wall_list[i])
    #         print(wall_list[i].get_range())
    #         print("+++++++++++++++++++++++++++++")
    #         possible_adjacents = self.get_all_walls_between_range(
    #             list_of_walls, wall_list[i].get_range())
    #         if not wall_list[i] == possible_adjacents[0]:
    #             adjacent = possible_adjacents[0]

    #         for j in range(len(possible_adjacents)):
    #             if (wall_list[i].get_coordinate1()[1] - possible_adjacents[j].get_coordinate1()[1]) < (wall_list[i].get_coordinate1()[1] - adjacent.get_coordinate1()[1]) and not wall_list[i] == possible_adjacents[j]:
    #                 print("if")
    #                 adjacent = possible_adjacents[j]
    #                 print(adjacent.get_range())
    #         adjacent_north_and_south_wall[wall_list[i]] = adjacent
    #     return adjacent_north_and_south_wall

    def check_north_wall(self, north_wall):
        height1 = north_wall.get_coordinate1()[1]
        height2 = north_wall.get_coordinate2()[1]
        print("function call")
        for i in range(len(self.verticalWallAdministration.vertical_walls)):
            print(".....................................................")
            print(
                self.verticalWallAdministration.vertical_walls[i].get_range())
            print(".....................................................")
            if self.verticalWallAdministration.vertical_walls[i].get_range()[0] < height1 < self.verticalWallAdministration.vertical_walls[i].get_range()[1]:
                print("if1")
                print(north_wall.get_range()[1])
                north_wall.set_range([self.verticalWallAdministration.vertical_walls[i].get_coordinate1()[
                                     0], north_wall.get_range()[1]])
                print(north_wall.get_range())

            if self.verticalWallAdministration.vertical_walls[i].get_range()[0] < height2 < self.verticalWallAdministration.vertical_walls[i].get_range()[1]:
                print("if2")
                north_wall.set_range(
                    [north_wall.get_range()[0], self.verticalWallAdministration.vertical_walls[i].get_coordinate2()[0]])
            print(north_wall.get_range())
            print("jklöööööööööööööööööööööööööööööööööööööööö")
