from tkinter import Tk, Frame, Canvas, BOTH


class Rectangles(Frame):

    def __init__(self):
        super().__init__()
        self.init_user_interface()

    def init_user_interface(self):
        self.master.title('Coloured Rectangles')
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)
        canvas.create_rectangle(30, 10, 120, 90, outline='#fb0', fill='#fb0')
        canvas.create_rectangle(150, 10, 240, 90, outline='#f50', fill='#f50')
        canvas.create_rectangle(270, 10, 360, 90, outline='#05f', fill='#05f')

        canvas.pack(fill=BOTH, expand=1)


def main():
    root = Tk()
    root.geometry('400x100+300+300')
    Rectangles()
    root.mainloop()


if __name__ == '__main__':
    main()
