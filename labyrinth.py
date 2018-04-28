from tkinter import *

# *** Labyrinth ***
# @param1, @param2 size of Labyrinth, @param3 root


class Labyrinth:
    def __init__(self, X, Y, master):
        self.X = X
        self.Y = Y
        self.L = [[Element(master, "1", w, r) for w in range(int(X))] for r in range(int(Y))]


    #Test Funcition
    def wypisz(self):
        print(self.L[0][0].get_value())
        for i in range(int(self.Y)):
            for j in range(int(self.X)):
                print(self.L[i][j].get_value())

    def rysuj(self):
        for i in range(int(self.Y)):
            for j in range(int(self.X)):
                self.L[i][j].get_button().grid(row=i+4, column=2+j, sticky=W)


    def set_start(self):
        for i in range(int(self.Y)):
            for j in range(int(self.X)):
                if self.L[i][j].clicked_return():
                    print(self.L[i][j].get_value())


# *** Labyrinth's element ***
# @param1 root,  @param2 text, @param3 x position<column>, @param4 y position<row>
# Values 0-wall, 1-road, 2-entrance, 3-exit

class Element:
    def __init__(self, master, textB, X, Y):
        self.pos_X = X
        self.pos_Y = Y

        self.value = 0

        self.clicked = False

        #self.button = Button(master, text=textB, fg="white", bg="green", command=lambda: self.click_function())
        self.button = Button(master, text=textB, fg="white", bg="green")
        self.button.bind("<Button-1>", self.click_function)

        #Test position
        #self.button.bind("<Button-1>", self.print_position)

    def change_color(self, color):
        self.button.config(fg=color)

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

    #Test position
    def print_position(self, event):
        print(self.get_position())

#Koniec wybieramy przez dwa klikniecia

    def click_function(self, event):
        self.clicked = True
        if self.value == 0:
            self.value = 2
        else:
            self.value = 3
        print(self.pos_Y, self.pos_X)
        print(self.value)

    def clicked_return(self):
        return self.clicked