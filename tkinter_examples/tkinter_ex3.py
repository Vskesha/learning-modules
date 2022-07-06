from tkinter import Tk, BOTH
from tkinter.ttk import Frame, Button, Style

class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.init_user_interface()

    def init_user_interface(self):
        self.parent.title('Кнопка виходу з програми')
        self.style = Style()
        self.style.theme_use('default')
        self.pack(fill=BOTH, expand=1)
        quit_button = Button(self, text='Закрити вікно', command=self.quit)
        quit_button.place(x=50, y=50)

def main():
    window = Tk()
    window.geometry('250x150+300+300')
    Example(window)
    window.mainloop()

if __name__ == '__main__':
    main()