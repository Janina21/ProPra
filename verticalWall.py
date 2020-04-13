from wall import Wall


class VerticalWall(Wall):

    coordinate1 = (0, 0)
    coordinate2 = (0, 0)
    length = None

    def __init__(self, coordinate1, coordinate2, length):
        self.coordinate1 = coordinate1
        self.coordinate2 = coordinate2
        self.length = length

    def get_walls(self):
        return self.vertical_walls
