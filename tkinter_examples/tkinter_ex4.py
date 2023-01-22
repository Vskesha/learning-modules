import tkinter as tk


window = tk.Tk()
greeting = tk.Label(
    text='Hello, Tkinter',
    foreground='white',
    background='black'
)
greeting.pack()
window.mainloop()
