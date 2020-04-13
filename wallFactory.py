from wall import Wall

# mein Algorithmus, um alle partner auf der x- und y-Achse zu finden: Von deiner aktuellen Ecke, finde eine Ecke, die den gleichen x wert
# hat, gibt es davon mehrere wird der x-partner auf None gesetzt, weil er ambiguous ist, ansonsten haben wir den richtigen Partner gefunden
# mit dem y-partner wird genauso verfahren.


class WallFactory:
    wall_list = []
    values_with_same_y = {}
    values_with_same_x = {}
    x_and_y_partner = {}

    def create_all_walls(self, coordinates):
        all_walls = []

        self.values_with_same_y = self.get_elements_with_same_y(coordinates)
        self.values_with_same_x = self.get_elements_with_same_x(coordinates)

        for i in range(len(coordinates)):
            self.get_partners(coordinates[i])

        self.find_partners_of_ambiguous_values()

        for key in self.x_and_y_partner:
            all_walls.append([key, self.x_and_y_partner.get(key)[0]])
            all_walls.append([key, self.x_and_y_partner.get(key)[1]])
        return self.remove_duplicate_walls(all_walls)

    # -------------------------------------------------------------------------------------------------------------------------

    def remove_duplicate_walls(self, all_walls):
        clean_walls = [all_walls[0]]
        in_list = False

        for i in range(len(all_walls)):

            for j in range(len(clean_walls)):

                if all_walls[i][0] in clean_walls[j] and all_walls[i][1] in clean_walls[j]:

                    in_list = True

            if not in_list:
                clean_walls.append(all_walls[i])

            in_list = False

        for j in range(len(clean_walls)):
            self.wall_list.append(Wall(clean_walls[j][0], clean_walls[j][1]))

        return self.wall_list

    def get_elements_with_same_y(self, coordinates):
        same_y = []
        y_value = None

        for j in range(len(coordinates)):
            y_value = coordinates[j][1]
            if not(y_value in self.values_with_same_y):
                for i in range(len(coordinates)):

                    if y_value == coordinates[i][1]:

                        same_y.append(coordinates[i])

                self.values_with_same_y[y_value] = same_y
                same_y = []
        return self.values_with_same_y

    def closest(self, lst, K):

        return lst[min(range(len(lst)), key=lambda i: abs(lst[i]-K))]

    def get_elements_with_same_x(self, coordinates):
        same_x = []
        x_value = None

        for j in range(len(coordinates)):
            x_value = coordinates[j][0]

            if not(x_value in self.values_with_same_x):
                for i in range(len(coordinates)):

                    if x_value == coordinates[i][0]:

                        same_x.append(coordinates[i])

                self.values_with_same_x[x_value] = same_x
                same_x = []
        return self.values_with_same_x

    def get_partners(self, value: list):

        self.x_and_y_partner[value] = [self.get_x_axis_partner(
            self.values_with_same_x, value), self.get_y_axis_partner(self.values_with_same_y, value)]

    def get_x_axis_partner(self, values_with_same_x, value):

        possible_partners = []
        partner = None

        for i in range(len(values_with_same_x[value[0]])):
            if values_with_same_x[value[0]][i][0] == value[0] and not(values_with_same_x[value[0]][i] == value):

                possible_partners.append(values_with_same_x[value[0]][i])

        if len(possible_partners) > 1:

            partner = possible_partners[0]
            positive_negative = []
            for i in range(len(possible_partners)):

                positive_negative.append(possible_partners[i][1]-value[1])

                if abs(possible_partners[i][1]-value[1]) < abs(partner[1]-value[1]):
                    partner = possible_partners[i]

            if not (all(i > 0 for i in positive_negative) or all(i < 0 for i in positive_negative)):

                partner = None

        else:
            partner = possible_partners[0]

        return partner

    def get_y_axis_partner(self, values_with_same_y, value):

        possible_partners = []
        partner = None

        for i in range(len(values_with_same_y[value[1]])):

            if values_with_same_y[value[1]][i][1] == value[1] and not(values_with_same_y[value[1]][i] == value):

                possible_partners.append(values_with_same_y[value[1]][i])

        if len(possible_partners) > 1:

            partner = possible_partners[0]
            positive_negative = []

            for i in range(len(possible_partners)):

                if abs(possible_partners[i][0]-value[0]) < abs(partner[0]-value[0]):

                    partner = possible_partners[i]

            if not (all(i > 0 for i in positive_negative) or all(i < 0 for i in positive_negative)):

                partner = None
        else:

            partner = possible_partners[0]

        return partner

    def find_partners_of_ambiguous_values(self):
        # if None values are in our final dictionary x_and_y_partner, we save the key in ambiguous_values
        ambiguous_values = {}
        for key in self.x_and_y_partner:
            if not all(self.x_and_y_partner.get(key)):

                ambiguous_values[key] = [i for i, val in enumerate(
                    self.x_and_y_partner.get(key)) if val == None][0]
        self.replace_all_None_values(ambiguous_values)

    def replace_all_None_values(self, ambiguous_values):
        # we replace all None values with the right values
        for key1 in ambiguous_values:

            for key2 in self.x_and_y_partner:
                if key1 == self.x_and_y_partner.get(key2)[ambiguous_values.get(key1)]:

                    self.x_and_y_partner[key1][ambiguous_values.get(
                        key1)] = key2

    def set_all_x_and_y_values_in_right_order(self):
        x_values = []
        y_values = []
        # wir setzen alle x und y values in unsere finalen listen, damit draw_line den gewünschten input bekommt.
        # Zunächst setzten wir den x- und y-wert unseres ersten wertes der eingabe,
        # dann gehen wir zu unserem nächsten punkt. Unser nächster punkt befindet sich immer abwechselnd von unserem aktuellen punkt ausgehend
        # oberhalb bzw. unterhalb von unserem aktuellen punkt, (deswegen brauchen wir flip). Der pointer zeigt auf unseren aktuellen punkt
        pointer = list(self.x_and_y_partner.keys())[0]
        flip = False
        x_values.append(pointer[0])
        y_values.append(pointer[1])

        for i in range(len(self.x_and_y_partner)):

            if flip == False:
                x_values.append(self.x_and_y_partner.get(pointer)[0][0])
                y_values.append(self.x_and_y_partner.get(pointer)[0][1])
                pointer = self.x_and_y_partner.get(pointer)[0]
                flip = True
            else:
                x_values.append(self.x_and_y_partner.get(pointer)[1][0])
                y_values.append(self.x_and_y_partner.get(pointer)[1][1])
                pointer = self.x_and_y_partner.get(pointer)[1]
                flip = False
        return [x_values, y_values]
