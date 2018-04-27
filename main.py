from tkinter import *
from interface import *

def main():
    root = Tk()
    root.title("Labyrinth generator")
    t = TopInterface(root)

    root.mainloop()

if __name__ == "__main__":
    main()