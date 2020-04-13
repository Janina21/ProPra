class Wall:

    coordinate1 = (0, 0)
    coordinate2 = (0, 0)
    length = None
    neighbour1 = None
    neighbour2 = None

    def __init__(self, coordinate1, coordinate2):
        self.coordinate1 = coordinate1
        self.coordinate2 = coordinate2

    def get_coordinates(self):
        return [self.coordinate1, self.coordinate2]

    # def get_orientation(self):
    #     return self.orientation

    # def set_orientation(self, value):
    #     self.orientation = value

    def get_coordinate1(self):
        return self.coordinate1

    def get_coordinate2(self):
        return self.coordinate2

    def set_range(self, length):

        self.length = length

    def get_range(self):
        return self.length
