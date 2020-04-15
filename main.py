from room import Room


class Main:
    input = [(1, 1), (1, 3), (1.5, 3), (1.5, 2), (2, 2), (2, 5), (1, 5), (1, 6), (2.5, 6), (2.5, 5.5),
             (7, 5.5), (7, 3.5), (6, 3.5), (6, 4), (5, 4), (5, 2), (6, 2), (6, 0.5), (4, 0.5), (4, 1.5), (3, 1.5), (3, 1)]
    room = None

    def __init__(self):

        self.room = Room(self.input)

        self.showRoom()
        self.show_sub_rectangles()

    def showRoom(self):
        return self.room.draw()

    def show_sub_rectangles(self):
        self.room.wallAdministration.split_horizontal_and_vertical_walls()
        self.room.wallAdministration.north_search()
        self.room.wallAdministration.south_search()
        self.room.wallAdministration.east_search()
        self.room.wallAdministration.west_search()


m = Main()
print(m)
