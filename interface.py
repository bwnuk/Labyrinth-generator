from tkinter import *

# *** Top interface ***
class TopInterface:
    def __init__(self, master):
        self.topFrame = Frame(master)
        self.topFrame.pack(side=TOP)
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
        self.size_N = int(self.entry_N.get())
        self.size_M = int(self.entry_M.get())
        print(self.size_M, self.size_N)