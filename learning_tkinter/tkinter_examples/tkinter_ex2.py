from tkinter import Tk, Frame, BOTH

class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background='lime')
        self.parent = parent
        self.parent.title('Вікно по центрі екрану'.upper())
        self.pack(fill=BOTH, expand=1)
        self.center_window()

    def center_window(self):
        width = 1100
        height = 600

        screen_width = self.parent.winfo_screenwidth()
        screen_height = self.parent.winfo_screenheight()

        x = (screen_width - width) / 2
        y = (screen_height - height) / 2
        print(width, height)
        print(screen_width, screen_height)
        print(x, y)
        self.parent.geometry('%dx%d+%d+%d' % (width, height, x, y))#f'{width}x{height}+{x}+{y}')


def main():
    window = Tk()
    frame = Example(window)
    window.mainloop()

if __name__ == '__main__':
    main()