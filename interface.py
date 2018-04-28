from labyrinth import *

# *** Button size ***
SIZE_X = 2
SIZE_Y = 1

# *** Top interface ***
# @param root

class TopInterface:
    def __init__(self, master):

        self.counter = False

        self.size_N = 0
        self.size_M = 0

        self.topFrame = Frame(master)
        self.topFrame.pack(side=TOP)

        self.label_confirm = Label(self.topFrame, text="Juz zrobiono!", fg="red")
        self.label_error_value = Label(self.topFrame, text="Musisz podac wartosc!", fg="red")
        self.label_start = Label(self.topFrame, text="Zaznacz poczatek i koniec", fg="blue")
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

    def get_entry(self, master):
        #try:
            self.size_N = int(self.entry_N.get())
            self.size_M = int(self.entry_M.get())

            if self.size_N > 30 or self.size_N < 0 or self.size_M > 30 or self.size_M < 0:
                print("ERROR")
            else:
                if self.counter:
                    self.label_confirm.grid(row=3, sticky=E)
                    self.label_error_value.grid_forget()
                else:
                    self.create(master)
                    self.label_error_value.grid_forget()
                    self.counter = True
        #except:
            if self.counter:
                pass
            else:
                self.label_error_value.grid(row=3, sticky=E)

    def get_size(self):
        return [self.size_N, self.size_M]

    def create(self, master):
        L = Labyrinth(self.size_N, self.size_M, master)
        #L.wypisz()
        L.rysuj()
        self.create_start(L)


    def create_start(self, L):
        self.label_start.grid(row=4+self.size_M, column=0, sticky=W)
        while not(L.set_start()):
            pass
