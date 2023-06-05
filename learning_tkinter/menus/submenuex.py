from tkinter import Tk, Frame, Menu


class Example(Frame):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title('add list_a submenu')

        menubar = Menu(self.master)
        self.master.config(menu=menubar)

        filemenu = Menu(menubar)
        submenu = Menu(filemenu)
        submenu.add_command(label='New source')
        submenu.add_command(label='Bookmark')
        submenu.add_command(label='Mail')
        filemenu.add_cascade(label='Import', menu=submenu, underline=0)
        filemenu.add_separator()
        filemenu.add_command(label='Exit', underline=0, command=self.onExit)
        menubar.add_cascade(label='File', underline=0, menu=filemenu)

    def onExit(self):
        self.quit()


def main():
    window = Tk()
    window.geometry('250x150+300+300')
    application = Example()
    window.mainloop()


if __name__ == '__main__':
    main()
