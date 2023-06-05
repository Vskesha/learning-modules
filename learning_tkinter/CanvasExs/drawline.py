from tkinter import Tk, Frame, Canvas


class Example(Frame):

    def __init__(self):
        super().__init__()
        self.init_user_interface()

    def init_user_interface(self):
        self.master.title('Draw Lines')
        self.pack(fill='both', expand=1)

        canvas = Canvas(self)
        canvas.create_line(15, 25, 200, 25)
        canvas.create_line(300, 35, 300, 200, dash=(4, 2))
        canvas.create_line(55, 85, 155, 85, 105, 180, 55, 85)
        canvas.pack(fill='both', expand=1)


def main():
    root = Tk()
    root.geometry('400x250+300+300')
    Example()
    root.mainloop()


if __name__ == '__main__':
    main()
