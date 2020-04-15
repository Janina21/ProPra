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

        north_wall = self.get_north_wall()
        # print(north_wall.get_range())
        rest = self.find_south_walls(north_wall, north_wall.get_range())
        if not rest == None and len(rest) > 0:
            for i in range(len(rest)):
                self.find_south_walls(north_wall, rest[i])

    def find_south_walls(self, wall, search_range):
        search_ranges = []
        walls_in_same_range = self.get_all_walls_between_range(
            wall, search_range)
        if len(walls_in_same_range) > 0:
            south_wall = walls_in_same_range[0]

            for j in range(len(walls_in_same_range)):
                if (wall.get_coordinate1()[1] - walls_in_same_range[j].get_coordinate1()[1]) < (wall.get_coordinate1()[1] - south_wall.get_coordinate1()[1]):
                    south_wall = walls_in_same_range[j]
            if not south_wall in self.south_walls:
                self.south_walls.append(south_wall)
            self.horizontal_walls.remove(south_wall)

            # wenn die Südwand noch nicht die komplette range der Nordwand abdeckt, dann gibt es noch mehr südwände in der range
            if south_wall.get_range()[0] > wall.get_range()[0] or south_wall.get_range()[1] < wall.get_range()[1]:
                # es gibt mehr zu entdecken!!

                if south_wall.get_range()[0] > wall.get_range()[0]:
                    search_ranges.append(
                        [wall.get_range()[0], south_wall.get_range()[0]])

                if south_wall.get_range()[1] < wall.get_range()[1]:
                    search_ranges.append(
                        [south_wall.get_range()[1], wall.get_range()[1]])
            return search_ranges

    def get_north_wall(self):

        self.bring_all_ranges_in_right_order()

        north_wall = self.horizontal_walls[0]

        for j in range(len(self.horizontal_walls)):
            if self.horizontal_walls[j].get_coordinate1()[1] > north_wall.get_coordinate1()[1]:

                north_wall = self.horizontal_walls[j]

        self.horizontal_walls.remove(north_wall)
        return north_wall

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
