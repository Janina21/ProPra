class VerticalWallAdministration:
    vertical_walls = []
    east_walls = []
    west_walls = []

    def get_all_walls_between_range(self, length):

        all_walls_between_range = []
        for i in range(len(self.vertical_walls)):
            if self.vertical_walls[i].get_range()[0] < length[1] and self.vertical_walls[i].get_range()[1] > length[0]:
                all_walls_between_range.append(self.vertical_walls[i])

        return all_walls_between_range

    def bring_all_ranges_in_right_order(self):

        for i in range(len(self.vertical_walls)):
            if self.vertical_walls[i].get_range()[0] > self.vertical_walls[i].get_range()[1]:
                self.vertical_walls[i].set_range([self.vertical_walls[i].get_range()[
                    1], self.vertical_walls[i].get_range()[0]])

    def set_start_ranges(self):

        for wall in self.vertical_walls:

            length = [wall.get_coordinate1()[1],
                      wall.get_coordinate2()[1]]
            wall.set_range(length)

    def find_all_definitely_east_walls(self):

        self.bring_all_ranges_in_right_order()

        for i in range(len(self.vertical_walls)):
            east_wall = self.vertical_walls[i]
            vertical_walls_in_same_range = self.get_all_walls_between_range(
                self.get_walls()[i].get_range())
            for j in range(len(vertical_walls_in_same_range)):
                if vertical_walls_in_same_range[j].get_coordinate1()[0] > east_wall.get_coordinate1()[0]:

                    east_wall = vertical_walls_in_same_range[j]

            if east_wall not in self.east_walls:
                self.append_east_wall(east_wall)

    def find_all_definitely_west_walls(self):

        self.bring_all_ranges_in_right_order()

        for i in range(len(self.vertical_walls)):
            south_wall = self.vertical_walls[i]
            vertical_walls_in_same_range = self.get_all_walls_between_range(
                self.vertical_walls[i].get_range())
            for j in range(len(vertical_walls_in_same_range)):
                if vertical_walls_in_same_range[j].get_coordinate1()[1] < south_wall.get_coordinate1()[1]:

                    south_wall = vertical_walls_in_same_range[j]
            if south_wall not in self.west_walls:
                self.append_west_wall(south_wall)

    def get_walls(self):
        return self.vertical_walls

    def get_east_walls(self):
        return self.east_walls

    def get_west_walls(self):
        return self.west_walls

    def append_vertical_wall(self, wall):

        self.vertical_walls.append(wall)

    def append_east_wall(self, wall):

        self.east_walls.append(wall)

    def append_west_wall(self, wall):

        self.west_walls.append(wall)
