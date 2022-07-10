from tkinter import Tk, Frame, Checkbutton, BOTH, BooleanVar


class Example(Frame):

    def __init__(self):
        super().__init__()
        self.init_user_interface()

    def init_user_interface(self):
        self.master.title('Flags')
        self.pack(fill=BOTH, expand=True)
        self.var = BooleanVar()

        cb = Checkbutton(self, text='Show title', variable=self.var, command=self.onclick)
        cb.select()
        cb.place(x=50, y=50)

    def onclick(self):
        if self.var.get():
            self.master.title('Flags')
        else:
            self.master.title('')


def main():
    root = Tk()
    root.geometry('250x150+300+300')
    app = Example()
    root.mainloop()


if __name__ == '__main__':
    main()
