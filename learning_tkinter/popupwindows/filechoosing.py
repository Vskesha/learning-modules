from tkinter import Tk, Frame, Text, Menu, BOTH, END
from tkinter import filedialog


class Example(Frame):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title('Window for file choose')
        self.pack(fill=BOTH, expand=1)

        menubar = Menu(self.master)
        self.master.config(menu=menubar)

        fileMenu = Menu(menubar)
        fileMenu.add_command(label='Open file', command=self.onOpen)
        menubar.add_cascade(label='File', menu=fileMenu)

        self.txt = Text(self)
        self.txt.pack(fill=BOTH, expand=1)

    def onOpen(self):
        ftypes = [('Python files', '*.py'), ('All files', '*')]
        dlg = filedialog.Open(self, filetypes=ftypes)
        fl = dlg.show()

        if fl != '':
            text = self.readFile(fl)
            self.txt.insert(END, text)

    def readFile(self, filename):
        with open(filename, 'r') as f:
            text = f.read()
        return text


def main():
    window = Tk()
    window.geometry('300x250+300+300')
    ex = Example()
    window.mainloop()


if __name__ == '__main__':
    main()