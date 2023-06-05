from tkinter import Tk, W, E
from tkinter.ttk import Frame, Button, Entry, Style


class Calculator(Frame):

    def __init__(self):
        super().__init__()
        self.init_user_interface()

    def init_user_interface(self):
        self.master.title('Calculator')

        Style().configure('TButton', padding=(0, 5, 0, 5), font='serif 10')

        self.columnconfigure(0, pad=3)
        self.columnconfigure(1, pad=3)
        self.columnconfigure(2, pad=3)
        #self.columnconfigure(3, pad=3)

        self.rowconfigure(0, pad=3)
        self.rowconfigure(1, pad=3)
        self.rowconfigure(2, pad=3)
        self.rowconfigure(3, pad=3)
        self.rowconfigure(4, pad=3)

        entry = Entry(font='serif 20 bold', width=10)
        entry.grid(row=0, columnspan=4, sticky=W+E)

        cls = Button(self, text='Clear')
        cls.grid(row=1, column=0)
        bck = Button(self, text='Delete')
        bck.grid(row=1, column=1)
        lbl = Button(self)
        lbl.grid(row=1, column=2)
        clo = Button(self, text='Close')
        clo.grid(row=1, column=3)

        sev = Button(self, text='7')
        sev.grid(row=2, column=0)
        eig = Button(self, text='8')
        eig.grid(row=2, column=1)
        nin = Button(self, text='9')
        nin.grid(row=2, column=2)
        div = Button(self, text='/')
        div.grid(row=2, column=3)

        fou = Button(self, text='4')
        fou.grid(row=3, column=0)
        fiv = Button(self, text='5')
        fiv.grid(row=3, column=1)
        six = Button(self, text='6')
        six.grid(row=3, column=2)
        mul = Button(self, text='*')
        mul.grid(row=3, column=3)

        one = Button(self, text='1')
        one.grid(row=4, column=0)
        two = Button(self, text='2')
        two.grid(row=4, column=1)
        thr = Button(self, text='3')
        thr.grid(row=4, column=2)
        sub = Button(self, text='-')
        sub.grid(row=4, column=3)

        zer = Button(self, text='0')
        zer.grid(row=5, column=0)
        dot = Button(self, text='.')
        dot.grid(row=5, column=1)
        equ = Button(self, text='=')
        equ.grid(row=5, column=2)
        pls = Button(self, text='+')
        pls.grid(row=5, column=3)

        self.grid()

def main():
    window = Tk()
    app = Calculator()
    window.mainloop()


if __name__ == '__main__':
    main()
