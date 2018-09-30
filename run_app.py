from utils.app import Application
from tkinter import Tk


if __name__ == '__main__':
    root = Tk()
    root.geometry("600x500+600+600")
    app = Application(root)
    root.mainloop()