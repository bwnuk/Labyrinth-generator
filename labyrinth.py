from tkinter import *

# *** Labyrinth ***
# @param1, @param2 size of Labyrinth, @param3 root

class Labyrinth:
    def __init__(self, X, Y, master):
        self.X = X
        self.Y = Y
        self.L = [[Element(master, " ", w, r) for w in range(int(X))] for r in range(int(Y))]

    # Test Funcition
    def wypisz(self):
        print(self.L[0][0].get_value())
        for i in range(int(self.Y)):
            for j in range(int(self.X)):
                print(self.L[i][j].get_value())

    def rysuj(self):
        for i in range(int(self.Y)):
            for j in range(int(self.X)):
                self.L[i][j].get_button().grid(row=i + 4, column=2 + j, sticky=W)

    def wall_set(self, X, Y):
        self.L[X][Y].change_value(0)
        self.L[X][Y].change_color_bg("forest green")

    def road_set(self, X, Y):
        self.L[X][Y].change_value(1)
        self.L[X][Y].change_color_bg("sandy brown")

    def middle_clear(self, X, Y):
        self.L[X][Y].change_value(0)
        self.L[X][Y].change_color_bg("sandy brown")

    def middle_set(self, X, Y):
        self.L[X][Y].change_value(4)
        self.L[X][Y].change_color_bg("goldenrod2")

    def start_set(self, X, Y):
        self.L[X][Y].change_value(2)
        self.L[X][Y].change_color_bg("SteelBlue2")

    def end_set(self, X, Y):
        self.L[X][Y].change_value(3)
        self.L[X][Y].change_color_bg("violet")

    #@param1 rows, @param2 columns
    def get_value(self, X, Y):
        return self.L[X][Y].get_value()

    #First rows then columns
    def filling(self, L, k, w):
        for i in range(0, k):
            for j in range(0, w):
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

# *** Labyrinth's element ***
# @param1 root,  @param2 text, @param3 x position<column>, @param4 y position<row>
# Values 0-wall, 1-road, 2-entrance, 3-exit, 4-middle
# Colors 0-brown, 1-green, 2-blue, 3-red, 4-yellow

class Element:
    def __init__(self, master, textB, X, Y):
        self.pos_X = X
        self.pos_Y = Y

        self.value = 0

        self.clicked = False

        # self.button = Button(master, text=textB, fg="white", bg="green", command=lambda: self.click_function())
        self.button = Button(master, text=textB, fg="white", bg="PaleTurquoise2")
        self.button.bind("<Button-1>", self.click_function)

        # Test position
        # self.button.bind("<Button-1>", self.print_position)

    def change_color_fg(self, color):
        self.button.config(fg=color)

    def change_color_bg(self, color):
        self.button.config(bg=color)

    def change_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def change_text(self, textC):
        self.button.config(text=textC)

    def get_button(self):
        return self.button

    def get_position(self):
        return [self.pos_X, self.pos_Y]

    # Test position
    def print_position(self, event):
        print(self.get_position())

    # Koniec wybieramy przez dwa klikniecia

    def click_function(self, event):
        pass
