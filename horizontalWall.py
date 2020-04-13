from wall import Wall


class HorizontalWall(Wall):
    coordinate1 = (0, 0)
    coordinate2 = (0, 0)
    length = None
    is_south = False
    is_north = False

    def __init__(self, coordinate1, coordinate2, length):
        self.coordinate1 = coordinate1
        self.coordinate2 = coordinate2
        self.length = length

    def wall_is_south(self):
        return self.is_south

    def wall_is_noth(self):
        return self.is_north

    def set_south(self):
        is_south = True

    def set_north(self):
        is_north = True
