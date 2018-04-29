from labyrinth import *
import time

# M = X
# N = Y

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

        self.start_X = 0
        self.start_Y = 0

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
        L = Labyrinth(self.size_N, self.size_M, master)
        #L.wypisz()
        L.rysuj()
        self.create_start()

    def create_start(self):
        self.label_info.grid(row=4+self.size_M, column=0, sticky=W)

        self.label_start.grid(row=5+self.size_M, column=0, sticky=E)
        self.entry_startX.grid(row=6+self.size_M, column=0, sticky=E)
        self.entry_startY.grid(row=6+self.size_M, column=1, sticky=W)

        self.label_end.grid(row=7+self.size_M, column=0, sticky=E)
        self.entry_endX.grid(row=8+self.size_M, column=0, sticky=E)
        self.entry_endY.grid(row=8+self.size_M, column=1, sticky=W)

        self.button_confirm1.grid(row=4+self.size_M, column=self.size_N+1, sticky=E)
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
                self.label_error_input.grid_forget()
                self.setting_start()
        except:
            if self.counter:
                pass
            else:
                self.label_error_input.config(text="Musisz podac wartosc!")
                self.label_error_input.grid(row=9 + self.size_M, column=0, sticky=W)

    def setting_start(self):
        self.reconfig_entry_start()

    def reconfig_entry_start(self):
        self.label_start.config(text="Start X - Y: "+str(self.start_X )+" - "+str(self.start_Y))
        self.label_end.config(text="Koniec X - Y: "+str(self.end_X )+" - "+str(self.end_Y))

        self.entry_startY.grid_forget()
        self.entry_startX.grid_forget()
        self.entry_endX.grid_forget()
        self.entry_endY.grid_forget()

        self.button_confirm1.grid_forget()
