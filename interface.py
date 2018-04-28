from tkinter import *


def work(master):
    Top = TopInterface(master)


# *** Top interface ***

class TopInterface:

    def __init__(self, master):
        self.counter = False

        self.size_N = 0
        self.size_M = 0

        self.topFrame = Frame(master)
        self.topFrame.pack(side=TOP)

        self.label_confirm = Label(self.topFrame, text="Juz zrobiono!", fg="red")
        self.label_error_value = Label(self.topFrame, text="Musisz podac wartosc!", fg="red")

        self.label_N = Label(self.topFrame, text="Rozmiar N:")
        self.label_M = Label(self.topFrame, text="Rozmiar M:")

        self.entry_N = Entry(self.topFrame)
        self.entry_M = Entry(self.topFrame)

        self.label_N.grid(row=0, sticky=W)
        self.label_M.grid(row=1, sticky=W)

        self.entry_N.grid(row=0, column=1)
        self.entry_M.grid(row=1, column=1)

        self.button_confirm = Button(self.topFrame, text="Zatwierdz", fg="blue")
        self.button_confirm.bind("<Button-1>", self.get_entry)
        self.button_confirm.grid(row=2, column=1, sticky=E)


    def get_entry(self, event):
        try:
            self.size_N = int(self.entry_N.get())
            self.size_M = int(self.entry_M.get())

            if self.size_N > 30 or self.size_N < 0 or self.size_M > 30 or self.size_M < 0:
                print("ERROR")
            else:
                if self.counter:
                    self.label_confirm.grid(row=3, sticky=E)
                    self.label_error_value.grid_forget()
                else:
                    L = Lab(self.size_N, self.size_M)
                    L.wypisz()
                    self.label_error_value.grid_forget()
                    self.counter = True
        except:
            self.label_error_value.grid(row=3, sticky=E)


    def get_size(self):
        return [self.size_N, self.size_M]


# *** Labyrinth ***

class Lab:
    def __init__(self, X, Y):
        self.L = [[2 for w in range(int(X))] for r in range(int(Y))]

    def wypisz(self):
        print(self.L)
