from tkinter import *


# *** Labyrinth ***
# @param1, @param2 size of Labyrinth, @param3 root

class Labyrinth:
    def __init__(self, X, Y):
        # rozmiar
        self.X = X
        self.Y = Y

        self.L = [[0 for w in range(int(X))] for r in range(int(Y))]

    # Test Funcition
    def wypisz(self):
        for i in range(int(self.Y)):
            for j in range(int(self.X)):
                print(self.L[i][j], end=" ")
            print("")

    def wall_set(self, X, Y):
        self.L[X][Y] = 0
        # self.L[X][Y].change_color_bg("forest green")

    def road_set(self, X, Y):
        self.L[X][Y] = 1
        # self.L[X][Y].change_color_bg("sandy brown")

    def middle_clear(self, X, Y):
        self.L[X][Y] = 0
        # self.L[X][Y].change_color_bg("sandy brown")

    def middle_set(self, X, Y):
        self.L[X][Y] = 4
        # self.L[X][Y].change_color_bg("goldenrod2")

    def start_set(self, X, Y):
        self.L[X][Y] = 2
        # self.L[X][Y].change_color_bg("SteelBlue2")

    def end_set(self, X, Y):
        self.L[X][Y] = 3
        # self.L[X][Y].change_color_bg("violet")

    # @param1 rows, @param2 columns
    def get_value(self, X, Y):
        return self.L[X][Y]

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
                    self.middle_set(i, j)

# Values 0-wall, 1-road, 2-entrance, 3-exit, 4-middle
# Colors 0-brown, 1-green, 2-blue, 3-red, 4-yellow
