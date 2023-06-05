from tkinter import Tk, LEFT, IntVar, BOTH
from tkinter.ttk import Scale, Frame, Label, Style


class Example(Frame):

    def __init__(self):
        super().__init__()
        self.init_user_interface()

    def init_user_interface(self):
        self.master.title('Scale Example')
        self.style = Style()
        self.style.theme_use('default')
        self.pack(fill=BOTH, expand=1)

        self.var = IntVar()
        scale = Scale(self, from_=0, to=100, command=self.onScale)
        scale.pack(side=LEFT, padx=15)

        label = Label(self, text=0, textvariable=self.var)
        label.pack(side=LEFT)

    def onScale(self, var):
        v = int(float(var))
        self.var.set(v)


def main():
    window = Tk()
    window.geometry('250x150+300+300')
    window.resizable(width=False, height=False)
    application = Example()
    window.mainloop()


if __name__ == '__main__':
    main()
