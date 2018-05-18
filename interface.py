from labyrinth import *
from algorithm import *

# N = X = Kolumna
# M = Y = Wiersz

# *** Button size ***

SIZE_X = 2
SIZE_Y = 1


# *** Interface ***

class StartInterface(Frame):
    def __init__(self, master):
        super(StartInterface, self).__init__(master)

        self.size_N = 0
        self.size_M = 0

        self.L_Interface = LabyrinthInterface(master)

        self.label_error_value = Label(self, text="Musisz podac wartosc!", fg="red")

        self.label_N = Label(self, text="Rozmiar N:")
        self.label_M = Label(self, text="Rozmiar M:")

        self.entry_N = Entry(self)
        self.entry_M = Entry(self)

        self.label_N.grid(row=0, sticky=W)
        self.label_M.grid(row=1, sticky=W)

        self.entry_N.grid(row=0, column=1)
        self.entry_M.grid(row=1, column=1)

        self.button_confirm = Button(self, text="Zatwierdz", fg="blue", command=lambda: self.get_entry())
        self.button_confirm.bind("<Button-1>")
        self.button_confirm.grid(row=2, column=1, sticky=E)
        self.grid()

    def get_entry(self):
        try:
            self.size_N = int(self.entry_N.get())
            self.size_M = int(self.entry_M.get())

            if self.size_N > 30 or self.size_N < 0 or self.size_M > 30 or self.size_M < 0:
                self.label_error_value.config(text="Przedzial rozmiarow (0:30)")
                self.label_error_value.grid(row=3, sticky=E)
            else:
                self.create()
                self.label_error_value.grid_forget()
        except:
            self.label_error_value.config(text="Musisz podac wartosc!")
            self.label_error_value.grid(row=3, sticky=E)

    def reconfigure_entry(self):
        self.label_N.config(text="Rozmiar N: " + str(self.size_N))
        self.label_M.config(text="Rozmiar M: " + str(self.size_M))

        self.entry_M.grid_forget()
        self.entry_N.grid_forget()

        self.button_confirm.grid_forget()

    def create(self):
        self.reconfigure_entry()
        self.L_Interface.change(self.size_N, self.size_M)
        self.L_Interface.rysuj()


# *** Interface ***
# @param1, @param2, @param3
#
# Button, @lambda, @list_comprehensions

class LabyrinthInterface(Frame):
    def __init__(self, master, X=0, Y=0):
        super(LabyrinthInterface, self).__init__(master)

        self.X = X
        self.Y = Y

        self.L = 0

        self.bool_start = False
        self.bool_end = False
        self.bool_mid = False

        self.button_generate = 0

        self.grid()

    def change(self, X, Y):
        self.X = X
        self.Y = Y

    # @Tablica
    # [Wiersz][Kolumna] = [Y] [X]
    def rysuj(self):
        self.L = []
        for w in range(int(self.Y)):
            self.L.append([Button(self.master, text="", fg="white", bg="PaleTurquoise2",
                                  command=lambda k=k, w=w: self.clicked(k, w)) for k in range(int(self.X))])
        for i in range(int(self.Y)):
            for j in range(int(self.X)):
                self.L[i][j].grid(row=i + 4, column=2 + j, sticky=W)

        self.button_generate = Button(self.master, text="Generuj", fg="blue", command=lambda: self.create())
        self.button_generate.bind("<Button-1>")
        self.button_generate.grid(row=int(self.Y)+4, column=int(self.X)+1, sticky=E)

    def button_change_color(self, color, X, Y):
        self.L[Y][X].config(bg=color)

    def set_start(self, k, w):
        if k >= 0 and w ==0 or k == 0 and w >= 0:
            self.button_change_color("SteelBlue2", k, w)
            return True
        else:
            return False

    def set_end(self, k, w):
        if w == self.Y - 1 and k >=0 or k == self.X -1 and w >=0:
            self.button_change_color("violet", k, w)
            return True
        else:
            return False

    # k = X = Kolumna
    # w = Y = Wiersz
    def clicked(self, k, w):
        print(k, w)
        if not self.bool_start:
            self.bool_start = self.set_start(k, w)
        elif not self.bool_end:
            self.bool_end = self.set_end(k, w)
        else:
            pass

    def create(self):
        pass

# *** Top interface ***
# @param root
