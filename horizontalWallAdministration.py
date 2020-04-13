class HorizontalWallAdministration:
    horizontal_walls = []
    north_walls = []
    south_walls = []

    def get_all_walls_between_range(self, length):

        all_walls_between_range = []
        for i in range(len(self.horizontal_walls)):
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
