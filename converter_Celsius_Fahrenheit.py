from tkinter_examples import *

def convertF():
	try:
		c = float(e.get())
		f = round(c * 9 / 5 + 32, 2)
		lb2['text'] = 'Температура в °F: '
		converted['text'] = f'{c}°C = {f}°F'
		converted['fg'] = 'lime'
	except ValueError:
		converted['text'] = 'Вводь тільки число'
		converted['fg'] = 'red'

def convertC():
	try:
		f = float(e.get())
		c = round((f - 32) * 5 / 9, 2)
		lb2['text'] = 'Температура в °C: '
		converted['text'] = f'{f}°F = {c}°C'
		converted['fg'] = 'lime'
	except ValueError:
		converted['text'] = 'Вводь тільки число'		
		converted['fg'] = 'red'

root = Tk()
root.title('Ковертер температури'.upper())
root.resizable(width=False, height=False)
root.geometry('400x250')
root['bg'] = 'black'

lb = Label(root, text='Введи температуру: ', font=('Arial', 12, 'bold'), fg='lime', bg='black')
lb.pack(pady=10)

e = Entry(root, font='Arial 16 bold', bg='lime', width=5)
e.pack()

btn1 = Button(root, text='Перевести в °F', font='Arial 10 bold', pady=5, padx=5, bg='lime', command=convertF)
btn1.pack(pady=10)

btn2 = Button(root, text='Перевести в °C', font='Arial 10 bold', pady=5, padx=5, bg='lime', command=convertC)
btn2.pack()

lb2 = Label(root, text='', font='Arial 12 bold', fg='lime', bg='black')
lb2.pack(pady=10)

converted = Label(root, text='', font='Arial 25 bold', bg='black', fg='lime')
converted.pack()

root.mainloop()