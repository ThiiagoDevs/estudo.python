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

'''import random
import string

def gerar_senha(tamanho):
    senha = ''
    for _ in range(tamanho):
        senha += random.choice(string.ascii_letters + string.digits)
    return senha 
    
print('\n     Gerador de senhas ')
print('>'*30)
tamanho = int(input('Qual tamanho da sua senha: '))    
print('>'*30)

senha = gerar_senha(tamanho)
print(f'Sua senha é {senha}')'''