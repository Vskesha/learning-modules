from tkinter import Tk, BOTH
from tkinter.ttk import Frame, Button
from tkinter import messagebox as mbox


class Example(Frame):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title('Pop-up message windows')
        self.pack()

        error = Button(self, text='Error', command=self.onError)
        error.grid(padx=5, pady=5)
        warning = Button(self, text='Warning', command=self.onWarn)
        warning.grid(column=0, row=1)
        question = Button(self, text='Question', command=self.onQuest)
        question.grid(column=1, row=0)
        information = Button(self, text='Information', command=self.onInfo)
        information.grid(column=1, row=1)

    def onError(self):
        mbox.showerror('Error', 'Can not open the file')

    def onWarn(self):
        mbox.showwarning('Warning', 'Deprecated function call')

    def onQuest(self):
        mbox.askquestion('Question', 'Are you sure you want to exit?')

    def onInfo(self):
        mbox.showinfo('Information', 'Downloading complete')


def main():
    window = Tk()
    window.geometry('300x150+300+300')
    app = Example()
    window.mainloop()

if __name__ == '__main__':
    main()