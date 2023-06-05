from tkinter import Tk, Text, BOTH, E, W, N, S
from tkinter.ttk import Style, Label, Frame, Button


class DialogWindow(Frame):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title('Dialog window in Tkinter')
        self.pack(fill=BOTH, expand=True)

        self.columnconfigure(1, weight=1)
        self.columnconfigure(3, pad=7)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(5, pad=7)

        lbl = Label(self, text='Windows')
        lbl.grid(sticky=W, pady=4, padx=5)

        area = Text(self)
        area.grid(row=1, column=0, columnspan=2, rowspan=4, padx=5, sticky=E+W+S+N)

        abtn = Button(self, text='Activate')
        abtn.grid(row=1, column=3)

        cbtn = Button(self, text='Close')
        cbtn.grid(row=2, column=3, pady=4)

        hbtn = Button(self, text='Help')
        hbtn.grid(row=5, column=0, padx=5)

        obtn = Button(self, text='OK')
        obtn.grid(row=5, column=3)


def main():
    window = Tk()
    window.geometry('350x300+300+300')
    app = DialogWindow()
    window.mainloop()


if __name__ == '__main__':
    main()
