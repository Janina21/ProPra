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

     def separate_north_and_south_walls(self):

        west_wall = self.get_west_wall()
        # print(west_wall.get_range())
        rest = self.find_east_walls(west_wall, west_wall.get_range())
        if not rest == None and len(rest) > 0:
            for i in range(len(rest)):
                self.find_east_walls(west_wall, rest[i])

    def find_east_walls(self, wall, search_range):
        search_ranges = []
        walls_in_same_range = self.get_all_walls_between_range(
            wall, search_range)
        if len(walls_in_same_range) > 0:
            east_wall = walls_in_same_range[0]

            for j in range(len(walls_in_same_range)):
                if (walls_in_same_range[j].get_coordinate1()[0] - wall.get_coordinate1()[0]) < (east_wall.get_coordinate1()[0] - wall.get_coordinate1()[0]):
                    east_wall = walls_in_same_range[j]
            if not east_wall in self.east_walls:
                self.east_walls.append(east_wall)
            self.vertical_walls.remove(east_wall)

            # wenn die Ostwand noch nicht die komplette range der Westwand abdeckt, dann gibt es noch mehr Ostwände in der range
            if east_wall.get_range()[0] > wall.get_range()[0] or east_wall.get_range()[1] < wall.get_range()[1]:

                if east_wall.get_range()[0] > wall.get_range()[0]:
                    search_ranges.append(
                        [wall.get_range()[0], east_wall.get_range()[0]])

                if east_wall.get_range()[1] < wall.get_range()[1]:
                    search_ranges.append(
                        [east_wall.get_range()[1], wall.get_range()[1]])
            return search_ranges

    def get_west_wall(self):

        self.bring_all_ranges_in_right_order()

        west_wall = self.vertical_walls[0]

        for j in range(len(self.vertical_walls)):
            if self.vertical_walls[j].get_coordinate1()[0] < west_wall.get_coordinate1()[0]:

                west_wall = self.vertical_walls[j]

        self.vertical_walls.remove(west_wall)
        return west_wall

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
