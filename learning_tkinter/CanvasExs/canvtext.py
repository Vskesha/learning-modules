from tkinter import Tk, Frame, Canvas, BOTH, W


class Example(Frame):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title('Text and Font in Tkinter Canvas')
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)
        canvas.create_text(20, 30, anchor=W, font='DejavuSansLight', text='The red sun is burning down')
        canvas.create_text(20, 60, anchor=W, font='Arial', text='A shadow falls on the burning city')
        canvas.create_text(20, 130, anchor=W, font='TimesNewRoman', text='Changes!!!')
        canvas.create_text(20, 160, anchor=W, font='ComicSans', text='Our hearts demand')
        canvas.create_text(20, 190, anchor=W, font='FreeSerif', text='Changes!!!')
        canvas.create_text(20, 220, anchor=W, font='LatoThin', text='Our eyes demand')
        canvas.pack(fill=BOTH, expand=1)


def main():
    root = Tk()
    root.geometry('420x250+300+300')
    app = Example()
    root.mainloop()


if __name__ == '__main__':
    main()
