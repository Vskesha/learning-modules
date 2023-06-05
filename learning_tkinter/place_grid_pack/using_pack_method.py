from tkinter import Tk, BOTH, RIGHT, RAISED
from tkinter.ttk import Frame, Button, Style


class Example(Frame):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title('Кнопки в Tkinter')
        self.style = Style()
        self.style.theme_use('default')

        frame = Frame(self, relief=RAISED, borderwidth=1)
        frame.pack(fill=BOTH, expand=True)

        self.pack(fill=BOTH, expand=True)

        close_button = Button(self, text='Close', command=self.quit)
        close_button.pack(side=RIGHT, padx=5, pady=5)
        ok_button = Button(self, text='OK')
        ok_button.pack(side=RIGHT)


def main():
    window = Tk()
    window.geometry('300x200+300+300')
    app = Example()
    window.mainloop()

if __name__ == '__main__':
    main()
