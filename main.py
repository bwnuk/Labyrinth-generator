from interface import *

def main():
    root = Tk()
    root.title("Labyrinth generator")

    Top = TopInterface(root)

    root.mainloop()

if __name__ == "__main__":
    main()