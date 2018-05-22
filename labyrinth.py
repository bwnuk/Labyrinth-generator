from algorithm import *


class Labyrinth:
    def __init__(self, X, Y):
        """
        :param X: columns
        :param Y: rows
        """
        self.__X = X
        self.__Y = Y

        self.__S = [0, 0]
        self.__K = [0, 0]
        self.__M = [0, 0]

        self.__bool_mid = False
        self.__L = [[0 for w in range(int(X))] for r in range(int(Y))]

    # Test Funcition
    def wypisz(self):
        for i in range(int(self.__Y)):
            for j in range(int(self.__X)):
                print(self.__L[i][j], end=" ")
            print("")

    def wall_set(self, X, Y):
        self.__L[X][Y] = 0
        # self.L[X][Y].change_color_bg("forest green")

    def road_set(self, X, Y):
        self.__L[X][Y] = 1
        # self.L[X][Y].change_color_bg("sandy brown")

    def mid_clear(self, X, Y):
        if self.__bool_mid:
            self.__L[Y][X] = 0
            self.__M[0] = 0
            self.__M[1] = 0
        # self.L[X][Y].change_color_bg("sandy brown")

    def mid_set(self, X, Y):
        self.__M[0] = X
        self.__M[1] = Y

        self.__L[X][Y] = 4
        self.__bool_mid = True
        # self.L[X][Y].change_color_bg("goldenrod2")

    def mid_get(self):
        return self.__M

    def start_set(self, X, Y):
        self.__S[0] = X
        self.__S[1] = Y

        self.__L[X][Y] = 2
        # self.L[X][Y].change_color_bg("SteelBlue2")

    def start_get(self):
        return self.__S

    def end_set(self, X, Y):
        self.__K[0] = X
        self.__K[1] = Y

        self.__L[X][Y] = 3
        # self.L[X][Y].change_color_bg("violet")

    def end_get(self):
        return self.__K

    # @param1 rows, @param2 columns
    def get_value(self, X, Y):
        return self.__L[X][Y]

    def generate(self):
        """
        Function generating labyrinth
        :return: Created labyrinth, need to be tested
        """
        L = [[2, 0, 0, 1, 0],
             [1, 1, 1, 1, 0],
             [0, 1, 0, 1, 0],
             [0, 1, 0, 1, 1],
             [1, 1, 0, 1, 0],
             [0, 0, 0, 1, 3]]
        # self.__L = L
        # self.__L = generator(self.__S[0], self.__S[1], self.__K[0], self.__K[1], self.__Y, self.__X, self.__bool_mid)
        self.__L = generator(self.__S[0], self.__S[1], self.__K[0], self.__K[1], self.__Y, self.__X, self.__bool_mid,
                             self.__M[0], self.__M[1], )
        return self.__L

    # First rows then columns
    def filling(self, L, k, w):
        for i in range(0, w):
            for j in range(0, k):
                if L[i][j] == 0:
                    self.wall_set(i, j)
                elif L[i][j] == 1:
                    self.road_set(i, j)
                elif L[i][j] == 2:
                    self.start_set(i, j)
                elif L[i][j] == 3:
                    self.end_set(i, j)
                elif L[i][j] == 4:
                    self.mid_set(i, j)

# Values 0-wall, 1-road, 2-entrance, 3-exit, 4-middle
# Colors 0-brown, 1-green, 2-blue, 3-red, 4-yellow
