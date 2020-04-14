from verticalWallAdministration import VerticalWallAdministration


class HorizontalWallAdministration:
    horizontal_walls = []
    north_walls = []
    south_walls = []

    def get_all_walls_between_range(self, wall, length):

        all_walls_between_range = []
        for i in range(len(self.horizontal_walls)):
            if not self.horizontal_walls[i] == wall:
                if self.horizontal_walls[i].get_range()[0] < length[1] and self.horizontal_walls[i].get_range()[1] > length[0]:
                    all_walls_between_range.append(self.horizontal_walls[i])

        return all_walls_between_range

    def bring_all_ranges_in_right_order(self):

        for i in range(len(self.horizontal_walls)):

            if self.horizontal_walls[i].get_range()[0] > self.horizontal_walls[i].get_range()[1]:

                self.horizontal_walls[i].set_range([self.horizontal_walls[i].get_range()[
                    1], self.horizontal_walls[i].get_range()[0]])

    def set_start_ranges(self):
        for wall in self.horizontal_walls:

            length = [wall.get_coordinate1()[
                0], wall.get_coordinate2()[0]]

            wall.set_range(length)

    def separate_north_and_south_walls(self):
        self.find_all_definitely_north_walls()

        for i in range(len(self.north_walls)):
            self.find_fitting_south_wall(
                self.north_walls[i], self.north_walls[i].get_range())

    def find_fitting_south_wall(self, wall, search_range):
        walls_in_same_range = self.get_all_walls_between_range(
            wall, search_range)
        fitting_south_walls = []
        search_ranges = []
        south_wall = walls_in_same_range[0]

        for j in range(len(walls_in_same_range)):
            if (wall.get_coordinate1()[1] - walls_in_same_range[j].get_coordinate1()[1]) < (wall.get_coordinate1()[1] - south_wall.get_coordinate1()[1]):
                south_wall = walls_in_same_range[j]

        fitting_south_walls.append(south_wall)
        search_ranges.append(south_wall.get_range()[1], wall.get_range[1])
        search_ranges.append(wall.get_range[0], south_wall.get_range()[0])
        return search_ranges

    def find_all_definitely_north_walls(self):

        self.bring_all_ranges_in_right_order()

        for i in range(len(self.horizontal_walls)):
            north_wall = self.horizontal_walls[i]
            horizontal_walls_in_same_range = self.get_all_walls_between_range(self.get_walls()[i],
                                                                              self.get_walls()[i].get_range())
            for j in range(len(horizontal_walls_in_same_range)):
                if horizontal_walls_in_same_range[j].get_coordinate1()[1] > north_wall.get_coordinate1()[1]:

                    north_wall = horizontal_walls_in_same_range[j]

            if north_wall not in self.north_walls:
                self.append_north_wall(north_wall)

    def find_all_definitely_south_walls(self):

        self.bring_all_ranges_in_right_order()

        for i in range(len(self.horizontal_walls)):
            south_wall = self.horizontal_walls[i]
            horizontal_walls_in_same_range = self.get_all_walls_between_range(self.horizontal_walls[i],
                                                                              self.horizontal_walls[i].get_range())
            for j in range(len(horizontal_walls_in_same_range)):
                if horizontal_walls_in_same_range[j].get_coordinate1()[1] < south_wall.get_coordinate1()[1]:

                    south_wall = horizontal_walls_in_same_range[j]
            if south_wall not in self.south_walls:
                self.append_south_wall(south_wall)

    # def find_adjacent_walls(self, walls, orientation):
    #     possible_adjacents = []
    #     adjacent_walls = {}

    #     for i in range(len(walls)):
    #         self.check_wall(walls[i], orientation)

    #         possible_adjacents = self.horizontalWallAdministration.get_all_walls_between_range(
    #             walls[i].get_range())
    #         if not walls[i] == possible_adjacents[0]:
    #             adjacent = possible_adjacents[0]
    #         else:
    #             adjacent = possible_adjacents[1]

    #         for j in range(len(possible_adjacents)):
    #             if (walls[i].get_coordinate1()[1] - possible_adjacents[j].get_coordinate1()[1]) < (walls[i].get_coordinate1()[1] - adjacent.get_coordinate1()[1]) and not walls[i] == possible_adjacents[j]:

    #                 adjacent = possible_adjacents[j]

    #         adjacent_walls[walls[i]] = adjacent
    #     return adjacent_walls

    def check_wall(self, wall):

        height1 = wall.get_coordinate1()
        height2 = wall.get_coordinate2()
        vw = VerticalWallAdministration()
        wall_ok_height1 = False
        wall_ok_height2 = False

        for i in range(len(vw.get_walls())):

            if (height1[0] == vw.get_walls()[i].get_coordinate1()[0] and height1[1] == vw.get_walls()[i].get_coordinate1()[1]) or (height1[0] == vw.get_walls()[i].get_coordinate2()[0] and height1[1] == vw.get_walls()[i].get_coordinate2()[1]):
                wall_ok_height1 = True
                print("if1")
                print(vw.get_walls()[i].get_range())

            if (height2[0] == vw.get_walls()[i].get_coordinate1()[0] and height2[1] == vw.get_walls()[i].get_coordinate1()[1]) or (height2[0] == vw.get_walls()[i].get_coordinate2()[0] and height2[1] == vw.get_walls()[i].get_coordinate2()[1]):
                wall_ok_height2 = True
                print("if2")

        print(wall_ok_height1)
        if not wall_ok_height1:
            print("not ok height1")
            for i in range(len(self.get_walls())):
                if self.get_walls()[i].get_coordinate1()[0] < height1:

                    wall.set_new_range([self.get_walls()[i].get_coordinate1()[
                        0], wall.get_coordinate2()[0]])

                    wall.set_new_coordinate1(
                        self.get_walls()[i].get_coordinate1())

                    wall.set_new_coordinate2(wall.get_coordinate2())

        if not wall_ok_height2:
            print("not ok height2")

            for i in range(len(self.get_walls())):
                if self.get_walls()[i].get_coordinate2()[0] > height2:

                    wall.set_new_range(
                        [wall.get_coordinate1()[0], self.get_walls()[i].get_coordinate2()[0]])

                    wall.set_new_coordinate1(wall.get_coordinate1())

                    wall.set_new_coordinate2(
                        self.get_walls()[i].get_coordinate2())

    def get_walls(self):
        return self.horizontal_walls

    def get_north_walls(self):
        return self.north_walls

    def get_south_walls(self):
        return self.south_walls

    def append_horizontal_wall(self, wall):

        self.horizontal_walls.append(wall)

    def append_north_wall(self, wall):

        self.north_walls.append(wall)

    def append_south_wall(self, wall):

        self.south_walls.append(wall)
