from room import Room


class Main:
    input = [(1, 1), (1, 3), (1.5, 3), (1.5, 2), (2, 2), (2, 5), (1, 5), (1, 6), (2.5, 6), (2.5, 5.5),
             (7, 5.5), (7, 3.5), (6, 3.5), (6, 4), (5, 4), (5, 2), (6, 2), (6, 0.5), (4, 0.5), (4, 1.5), (3, 1.5), (3, 1)]
    room = None

    def __init__(self):

        self.room = Room(self.input)
        self.showRoom()
        self.test()

    def showRoom(self):
        return self.room.draw()

    def test(self):
        self.room.wallAdministration.split_horizontal_and_vertical_walls()
        self.room.wallAdministration.find_all_definitely_north_walls()
        self.room.wallAdministration.find_all_definitely_south_walls()
        for i in range(len(self.room.wallAdministration.horizontalWallAdministration.north_walls)):
            print(
                self.room.wallAdministration.horizontalWallAdministration.north_walls[i].get_range())
        print("----------------------------------------------------------------")
        # for j in range(len(self.room.wallAdministration.south_walls)):
        #     print(self.room.wallAdministration.south_walls[j].get_range())
        # adjacent_walls = self.room.wallAdministration.find_adjacent_walls(
        #     self.room.wallAdministration.north_walls, self.room.wallAdministration.horizontal_walls)

        # for key in range(len(adjacent_walls)):
        #     print(key)


m = Main()
print(m)
