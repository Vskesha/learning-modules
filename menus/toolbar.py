from PIL import Image, ImageTk
from tkinter import Tk, Frame, Button, Menu
from tkinter import LEFT, TOP, X, FLAT, RAISED


class Example(Frame):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title('Instrumental Panel')

        menubar = Menu(self.master)
        self.fileMenu = Menu(self.master, tearoff=0)
        self.fileMenu.add_command(label='Exit', command=self.onExit)
        menubar.add_cascade(label='File', menu=self.fileMenu)

        toolbar = Frame(self.master, bd=1, relief=RAISED)

        self.img = Image.open('exit.png')
        eimg = ImageTk.PhotoImage(self.img)

        exitButton = Button(toolbar, image=eimg, relief=FLAT, command=self.onExit)
        exitButton.image = eimg

        exitButton.pack(side=LEFT, padx=2, pady=2)

        toolbar.pack(side=TOP, fill=X)
        self.master.config(menu=menubar)
        self.pack()

    def onExit(self):
        self.quit()


def main():
    root = Tk()
    root.geometry('250x150+300+300')
    app = Example()
    root.mainloop()


if __name__ == '__main__':
    main()
