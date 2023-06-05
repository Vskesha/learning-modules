from PIL import Image, ImageTk
from tkinter import Tk
from tkinter.ttk import Label, Frame
import sys


class ImageLabel(Frame):

    def __init__(self):
        super().__init__()
        self.loadingImage()
        self.initUI()

    def loadingImage(self):
        try:
            self.image = Image.open('tatras.jpg')
        except IOError:
            print('no such file')
            sys.exit(1)

    def initUI(self):
        self.master.title('Tatras')
        tatra = ImageTk.PhotoImage(self.image)
        lbl = Label(self, image=tatra)
        lbl.image = tatra

        lbl.pack()
        self.pack()

    def set_geometry(self):
        w, h = self.image.size
        self.master.geometry(f'{w}x{h}+300+300')


def main():
    window = Tk()
    app = ImageLabel()
    app.set_geometry()
    window.mainloop()


if __name__ == '__main__':
    main()
