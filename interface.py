from labyrinth import *
import time
from algorithm import *

# M = X = Wysokość
# N = Y = Szerokość

# *** Button size ***
SIZE_X = 2
SIZE_Y = 1

# *** Top interface ***
# @param root

class TopInterface:
    def __init__(self, master):
        self.L = 0
        self.counter = False
        self.counter_middle = False

        self.size_N = 0
        self.size_M = 0

        self.start_X = 0
        self.start_Y = 0

        self.mid_X = 0
        self.mid_Y = 0

        self.end_X = 0
        self.end_Y = 0

        self.topFrame = Frame(master)
        self.topFrame.pack(side=TOP)

        self.label_error_value = Label(self.topFrame, text="Musisz podac wartosc!", fg="red")
        self.label_info = Label(self.topFrame, text="Wpisz start i koniec", fg="blue")
        self.label_error_input = Label(self.topFrame, text="Musisz podac wszystkie wartosci", fg="red")

        self.label_start = Label(self.topFrame, text="Start X - Y:")
        self.entry_startX = Entry(self.topFrame, width=2)
        self.entry_startY = Entry(self.topFrame, width=2)

        self.label_end = Label(self.topFrame, text="Koniec X - Y:")
        self.entry_endX = Entry(self.topFrame, width=2)
        self.entry_endY = Entry(self.topFrame, width=2)

        self.label_middle = Label(self.topFrame, text="Punkt posredni X - Y:")
        self.entry_midX = Entry(self.topFrame, width=2)
        self.entry_midY = Entry(self.topFrame, width=2)

        self.label_N = Label(self.topFrame, text="Rozmiar N:")
        self.label_M = Label(self.topFrame, text="Rozmiar M:")

        self.entry_N = Entry(self.topFrame)
        self.entry_M = Entry(self.topFrame)

        self.label_N.grid(row=0, sticky=W)
        self.label_M.grid(row=1, sticky=W)

        self.entry_N.grid(row=0, column=1)
        self.entry_M.grid(row=1, column=1)

        self.button_confirm = Button(self.topFrame, text="Zatwierdz", fg="blue", command=lambda: self.get_entry(self.topFrame))
        self.button_confirm.bind("<Button-1>")
        self.button_confirm.grid(row=2, column=1, sticky=E)

        self.button_confirm1 = Button(self.topFrame, text="Zatwierdz", fg="blue", command=lambda: self.get_entry_start(self.topFrame))
        self.button_confirm1.bind("<Button-1>")

        self.button_generate = Button(self.topFrame, text="Generuj", fg="blue", command=lambda: self.generate(self.topFrame))
        self.button_confirm1.bind("<Button-1>")

        self.button_mid = Button(self.topFrame, text="Zatwierdz", fg="blue", command=lambda: self.get_middle(self.topFrame))
        self.button_mid.bind("<Button-1>")

    def get_entry(self, master):
        try:
            self.size_N = int(self.entry_N.get())
            self.size_M = int(self.entry_M.get())

            if self.size_N > 30 or self.size_N < 0 or self.size_M > 30 or self.size_M < 0:
                self.label_error_value.config(text="Przedzial rozmiarow (0:30)")
                self.label_error_value.grid(row=3, sticky=E)
            else:
                self.create(master)
                self.label_error_value.grid_forget()
        except:
            if self.counter:
                pass
            else:
                self.label_error_value.config(text="Musisz podac wartosc!")
                self.label_error_value.grid(row=3, sticky=E)

    def get_size(self):
        return [self.size_N, self.size_M]

    def create(self, master):
        temp = Labyrinth(self.size_N, self.size_M, master)
        self.L = temp
        #L.wypisz()
        self.L.rysuj()
        self.create_start()

    def create_start(self):
        self.label_info.grid(row=4+self.size_M, column=0, sticky=W)

        self.label_start.grid(row=5+self.size_M, column=0, sticky=W)
        self.entry_startX.grid(row=6+self.size_M, column=0, sticky=E)
        self.entry_startY.grid(row=6+self.size_M, column=1, sticky=W)

        self.label_end.grid(row=7+self.size_M, column=0, sticky=W)
        self.entry_endX.grid(row=8+self.size_M, column=0, sticky=E)
        self.entry_endY.grid(row=8+self.size_M, column=1, sticky=W)

        self.button_confirm1.grid(row=8+self.size_M, column=self.size_N+1, sticky=E)
        self.button_generate.grid(row=4+self.size_M, column=self.size_N+1, sticky=E)
        self.reconfig_entry()

    def reconfig_entry(self):
        self.label_N.config(text="Rozmiar N: "+str(self.size_N))
        self.label_M.config(text="Rozmiar M: " + str(self.size_M))

        self.entry_M.grid_forget()
        self.entry_N.grid_forget()

        self.button_confirm.grid_forget()

    def get_entry_start(self, master):
        try:
            self.start_X = int(self.entry_startX.get())
            self.start_Y = int(self.entry_startY.get())

            self.end_X = int(self.entry_endX.get())
            self.end_Y = int(self.entry_endY.get())

            if self.start_X > self.size_M-1 or self.start_X < 0 or self.start_Y > self.size_N-1 or self.start_Y < 0 or self.end_X > self.size_M-1 or self.end_X < 0 or self.end_Y > self.size_N-1 or self.end_Y < 0:
                self.label_error_input.config(text="Przedzial rozmiarow (0:30)")
                self.label_error_input.grid(row=9+self.size_M, column=0, sticky=W)
            else:
                if self.case_start():
                    self.label_error_input.grid_forget()
                    self.label_info.grid_forget()
                    self.reconfig_entry_start()
                else:
                    self.label_error_input.config(text="Musisz podac PKT na zewnetrrznych scianach")
                    self.label_error_input.grid(row=9 + self.size_M, column=0, sticky=W)
        except:
            if self.counter:
                pass
            else:
                self.label_error_input.config(text="Musisz podac wartosc!")
                self.label_error_input.grid(row=9 + self.size_M, column=0, sticky=W)

    def reconfig_entry_start(self):
        self.label_start.config(text="Start X - Y: "+str(self.start_X )+" - "+str(self.start_Y))
        self.label_end.config(text="Koniec X - Y: "+str(self.end_X )+" - "+str(self.end_Y))

        self.entry_startY.grid_forget()
        self.entry_startX.grid_forget()
        self.entry_endX.grid_forget()
        self.entry_endY.grid_forget()

        self.button_confirm1.grid_forget()
        self.set_middle()

    def case_start(self):
        if self.start_Y == self.end_Y and self.start_X == self.end_X:
            return False
        else:
            if self.start_X in [0, self.size_M-1]:
                if self.end_X in [0, self.size_M-1]:
                    return True
                else:
                    if self.end_Y in [0, self.size_N-1]:
                        return True
                    else:
                        return False
            else:
                if self.start_Y in [0, self.size_N-1]:
                    return True
                else:
                    return False

    def get_middle(self, master):
        try:
            if self.counter_middle:
                self.L.middle_clear(self.mid_X, self.mid_Y)
            self.mid_X = int(self.entry_midX.get())
            self.mid_Y = int(self.entry_midY.get())

            self.counter_middle = True

            if  self.mid_X > self.size_N or self.mid_X < 0 or self.mid_Y > self.size_M or self.mid_Y < 0:
                self.label_error_value.config(text="Przedzial taki jak rozmiar labiryntu")
                self.label_error_value.grid(row=11+self.size_M, column=0, sticky=W)
            else:
                if (self.mid_X == self.start_X and self.mid_Y == self.start_Y) or (self.mid_X == self.end_X and self.mid_Y == self.end_Y):
                    self.label_error_value.config(text="Nie moze byc taki jak start, lub koniec")
                    self.label_error_value.grid(row=11 + self.size_M, column=0, sticky=W)
                else:
                    self.label_error_value.grid_forget()
                    self.middle()
        except:
            if self.counter:
                pass
            else:
                self.label_error_value.config(text="Musisz podac wartosc!")
                self.label_error_value.grid(row=11+self.size_M, column=0, sticky=W)

    def set_middle(self):
        self.label_middle.grid(row=9+self.size_M, column=0, sticky=W)
        self.entry_midX.grid(row=10+self.size_M, column=0, sticky=E)
        self.entry_midY.grid(row=10+self.size_M, column=1, sticky=W)

        self.button_mid.grid(row=10+self.size_M, column=self.size_N+1, sticky=E)

    def middle(self):
        self.label_middle.config(text="Punkt posredni X - Y: "+str(self.mid_X)+" - "+str(self.mid_Y))

    def generate(self, master):
        self.L.start_set(self.start_X, self.start_Y)
        self.L.end_set(self.end_X, self.end_Y)

        if self.counter_middle:
            self.L.middle_set(self.mid_X, self.mid_Y)
        self.default_lab()

    #TEST
    def default_lab(self):
        L = [[2, 0, 0, 1, 0],
             [1, 1, 4, 1, 0],
             [0, 1, 0, 1, 0],
             [0, 1, 0, 1, 1],
             [1, 1, 0, 1, 0],
             [0, 0, 0, 1, 3]]
        self.L.filling(L,6, 5)

        if Bot(self.L, self.size_N, self.size_M, self.start_X, self.start_Y):
            print("A")
        else:
            print("B")
