from tkinter import Tk, Frame, Canvas, BOTH, NW
from PIL import Image, ImageTk


class CanImage(Frame):

    def __init__(self):
        super().__init__()
        self.img = Image.open('tatras.jpg')
        self.tatr = ImageTk.PhotoImage(self.img)
        self.init_user_interface()

    def init_user_interface(self):
        self.master.title('Canvas Image')
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self, width=self.img.size[0] + 20, height=self.img.size[1] + 20)
        canvas.create_image(10, 10, anchor=NW, image=self.tatr)
        canvas.pack(fill=BOTH, expand=1)


def main():
    window = Tk()
    CanImage()
    window.mainloop()


if __name__ == '__main__':
    main()
