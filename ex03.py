from tkinter import *

root = Tk()
root.geometry('350x200')

root.title('Login')


Label(root, text='Usuario').place(x=60, y=40)
Label(root, text='Senha').place(x=60, y=70)
Button(root, text='Entra').place(x=150, y=100)
Entry(root).place(x=120, y=40)
Entry(root).place(x=120, y=70)

root.mainloop()