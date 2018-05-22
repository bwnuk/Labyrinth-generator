from tkinter import *
from labyrinth import *

# N = X = Kolumna
# M = Y = Wiersz

# *** Button size ***

SIZE_X = 2
SIZE_Y = 1


# *** Interface ***

class StartInterface(Frame):
    """
    Top interface, entry
    """
    def __init__(self, master):
        """
        :param master: root
        """
        super(StartInterface, self).__init__(master)

        self.__size_N = 0
        self.__size_M = 0

        self.__L_Interface = LabyrinthInterface(master)

        self.__label_error_value = Label(self, text="Musisz podac wartosc!", fg="red")

        self.__label_N = Label(self, text="Rozmiar N:")
        self.__label_M = Label(self, text="Rozmiar M:")

        self.__entry_N = Entry(self)
        self.__entry_M = Entry(self)

        self.__label_N.grid(row=0, sticky=W)
        self.__label_M.grid(row=1, sticky=W)

        self.__entry_N.grid(row=0, column=1)
        self.__entry_M.grid(row=1, column=1)

        self.__button_confirm = Button(self, text="Zatwierdz", fg="blue", command=lambda: self.get_entry())
        self.__button_confirm.bind("<Button-1>")
        self.__button_confirm.grid(row=2, column=1, sticky=E)
        self.grid()

    def get_entry(self):
        try:
            self.__size_N = int(self.__entry_N.get())
            self.__size_M = int(self.__entry_M.get())

            if self.__size_N > 30 or self.__size_N < 0 or self.__size_M > 30 or self.__size_M < 0:
                self.__label_error_value.config(text="Przedzial rozmiarow (0:30)")
                self.__label_error_value.grid(row=3, sticky=E)
            else:
                self.create()
                self.__label_error_value.grid_forget()
        except:
            self.__label_error_value.config(text="Musisz podac wartosc!")
            self.__label_error_value.grid(row=3, sticky=E)

    def reconfigure_entry(self):
        self.__label_N.config(text="Rozmiar N: " + str(self.__size_N))
        self.__label_M.config(text="Rozmiar M: " + str(self.__size_M))

        self.__entry_M.grid_forget()
        self.__entry_N.grid_forget()

        self.__button_confirm.grid_forget()

    def create(self):
        self.reconfigure_entry()
        self.__L_Interface.change(self.__size_N, self.__size_M)
        self.__L_Interface.rysuj()

# Button, @lambda, @list_comprehensions

class LabyrinthInterface(Frame):
    """
    Labyrinth Interface
    """
    def __init__(self, master, X=0, Y=0):
        """
        :param master: root
        :param X: columns
        :param Y: rows
        """
        super(LabyrinthInterface, self).__init__(master)

        self.__X = X
        self.__Y = Y

        self.__L = 0
        self.__lab = 0

        self.__S = [0, 0]
        self.__K = [0, 0]
        self.__M = [0, 0]

        self.__bool_start = False
        self.__bool_end = False
        self.__bool_mid = False

        self.__button_generate = 0

        self.__error_generate = Label(self.master, text="Musisz dodac start i koniec", fg="red")

        self.grid()

    def change(self, X, Y):
        self.__X = X
        self.__Y = Y
        self.__lab = Labyrinth(self.__X, self.__Y)

    # @Tablica
    # [Wiersz][Kolumna] = [Y] [X]
    def rysuj(self):
        self.__L = []
        for w in range(int(self.__Y)):
            self.__L.append([Button(self.master, text="", fg="white", bg="PaleTurquoise2",
                                    command=lambda k=k, w=w: self.clicked(k, w)) for k in range(int(self.__X))])
        for i in range(int(self.__Y)):
            for j in range(int(self.__X)):
                self.__L[i][j].grid(row=i + 4, column=2 + j, sticky=W)

        self.__button_generate = Button(self.master, text="Generuj", fg="blue", command=lambda: self.create())
        self.__button_generate.bind("<Button-1>")
        self.__button_generate.grid(row=int(self.__Y) + 4, column=int(self.__X) + 1, sticky=E)

    def button_change_color(self, color, X, Y):
        self.__L[Y][X].config(bg=color)

    def set_start(self, k, w):
        if k >= 0 and w == 0 or k == 0 and w >= 0:
            self.button_change_color("SteelBlue2", k, w)
            self.__lab.start_set(w, k)
            return True
        else:
            return False

    def set_end(self, k, w):
        if w == self.__Y - 1 and k >= 0 or k == self.__X - 1 and w >= 0:
            self.button_change_color("violet", k, w)
            self.__lab.end_set(w, k)
            return True
        else:
            return False

    def set_mid(self, k, w):
        if w == int(self.__lab.start_get()[1]) and k == int(self.__lab.start_get()[0]) or w == int(self.__lab.end_get()[1]) and k == int(self.__lab.end_get()[0]):
            pass
        else:
            self.button_change_color("goldenrod2", k, w)

            if self.__bool_mid:
                self.button_change_color("PaleTurquoise2", self.__lab.mid_get()[1], self.__lab.mid_get()[0])
                self.__lab.mid_clear(self.__lab.mid_get()[1], self.__lab.mid_get()[0])

            self.__lab.mid_set(w, k)
            self.__bool_mid = True

            return True

    # k = X = Kolumna
    # w = Y = Wiersz
    def clicked(self, k, w):
        #print(k, w)
        if not self.__bool_start:
            self.__bool_start = self.set_start(k, w)
        elif not self.__bool_end:
            self.__bool_end = self.set_end(k, w)
        else:
            self.set_mid(k, w)

    def koloruj(self):
        L = self.__lab.generate()
        for i in range(0, int(self.__X)):
            for j in range(0, int(self.__Y)):
                if L[j][i] == 0:
                    self.button_change_color("forest green", i, j)
                elif L[j][i] == 1:
                    self.button_change_color("sandy brown", i, j)
                elif L[j][i] == 2:
                    self.button_change_color("SteelBlue2", i, j)
                elif L[j][i] == 3:
                    self.button_change_color("violet", i, j)
                elif L[j][i] == 4:
                    self.button_change_color("goldenrod2", i, j)

    def create(self):
        if self.__bool_start and self.__bool_end:
            self.__error_generate.grid_forget()

            self.__lab.wypisz()
            self.koloruj()
        else:
            self.__error_generate.grid(row=int(self.__Y) + 5, column=0, sticky=E)
