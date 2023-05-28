import tkinter as tk
from tkinter import font


def calculate_imc():
    nome = name_entry.get().strip()
    idade = int(age_entry.get())
    peso = float(weight_entry.get())
    altura = float(height_entry.get())
    imc = peso / (altura * altura)

    result_label.config(text=f'IMC: {imc:.2f}')

    if imc < 18.5:
        message = f'Atenção {nome}, seu peso está abaixo do peso normal'
        fg_color = '#FFD700'
    elif imc < 25:
        message = f'{nome}, seu peso está normal'
        fg_color = '#50fa7b'
    elif imc < 30:
        message = f'Atenção {nome}, sobrepeso risco de obesidade'
        fg_color = '#FFD700'
    elif imc < 40:
        message = f'Atenção {nome}, você está com obesidade\nprocure um médico especialista'
        fg_color = '#ff8c00'
    else:
        message = f'Atenção {nome}, você está com obesidade mórbida\nprocure um médico especialista'
        fg_color = '#ff0000'

    category_label.config(text=message, fg=fg_color)


def create_label_and_entry(parent, text, row, column):
    label = tk.Label(parent, text=text, font=font_label, bg='#44475a', fg='white')
    label.grid(row=row, column=column, padx=5, pady=5, sticky='w')
    entry = tk.Entry(parent, font=font_entry, width=20)
    entry.grid(row=row, column=column+1, padx=5, pady=5)
    return entry


window = tk.Tk()
window.geometry('500x400')
#window.title('Calculadora IMC')
window.configure(bg='#44475a')


font_label = font.Font(family='Arial', size=12, weight='bold')
font_entry = font.Font(family='Arial', size=12)
font_button = font.Font(family='Arial', size=12, weight='bold')

input_frame = tk.Frame(window, borderwidth=5, bg='#44475a')
input_frame.pack(pady=10)

button_frame = tk.Frame(window, highlightthickness=0, bg='#44475a')
button_frame.pack(pady=10)

name_entry = create_label_and_entry(input_frame, 'Nome:', 0, 0)
age_entry = create_label_and_entry(input_frame, 'Idade:', 1, 0)
weight_entry = create_label_and_entry(input_frame, 'Peso (kg):', 2, 0)
height_entry = create_label_and_entry(input_frame, 'Altura (m):', 3, 0)

calculate_button = tk.Button(button_frame, text='Calcular', font=font_button, command=calculate_imc, bg='#50fa7b', fg='white', relief='solid', bd=0, padx=10, pady=5)
calculate_button.pack(pady=10)

result_label = tk.Label(window, text='IMC: ', font=font_label, bg='#44475a', fg='white')
result_label.pack()

category_label = tk.Label(window, text='', font=font_label, bg='#44475a', fg='white')
category_label.pack()

# Centering the title label
title_label = tk.Label(window, text='Calculadora IMC', font=('Arial', 18, 'bold'), bg='#44475a', fg='white')
title_label.pack(pady=20)

window.mainloop()
