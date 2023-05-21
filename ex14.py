'''print('          Mercado')
print('='*30)
produto = str(input('Produto: '))
preço_do_quilo = float(input('Preço do quilo: '))
peso = float(input('Peso kg: '))
preço = preço_do_quilo * peso

print('='*30)
print(f'{produto}\n \npreço do quilo R$ {preço_do_quilo:.2f}\n \npeso {peso} kg')
print('='*30)
print(f'TOTAL R$ {preço:.2f}')'''


import tkinter as tk

def calcular_total():
    produto = produto_entry.get()
    preço_do_quilo = float(preco_entry.get())
    peso = float(peso_entry.get())
    preço = preço_do_quilo * peso

    resultado_label.config(text=f'{produto}\n \npreço do quilo R$ {preço_do_quilo:.2f}\n \npeso {peso} kg')
    total_label.config(text=f'TOTAL R$ {preço:.2f}')

root = tk.Tk()
root.geometry('500x500')
root.title('Mercado_Feira_Carnes')
titulo_label = tk.Label(root, text='Mercado', font=('Ariel', 16))
titulo_label.pack()

separador_label = tk.Label(root, text='_'*100)
separador_label.pack()

produto_label = tk.Label(root, text='Produto')
produto_label.pack()
produto_entry = tk.Entry(root)
produto_entry.pack()

preco_label = tk.Label(root, text='Preço do quilo')
preco_label.pack()
preco_entry = tk.Entry(root)
preco_entry.pack()

peso_label = tk.Label(root, text='Peso kg')
peso_label.pack()
peso_entry = tk.Entry(root)
peso_entry.pack()

calcular_button = tk.Button(root, text='Calcular', command=calcular_total)
calcular_button.pack()

resultado_label = tk.Label(root, text='')
resultado_label.pack()

separador_label = tk.Label(root, text='_'*100)
separador_label.pack()

total_label = tk.Label(root, text='')
total_label.pack()

produto_entry.pack(padx=10, pady= 10)
preco_entry.pack(padx=10, pady= 10)
peso_entry.pack(padx=10, pady= 10)
calcular_button.pack(padx=10, pady= 10)

root.mainloop()
