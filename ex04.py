import customtkinter

janela = customtkinter.CTk()
janela.geometry('500x300')

def clique():
    print('Fazer Login')

texto = customtkinter.CTkLabel(janela, text='Fazer Login')

Usuario = customtkinter.CTkEntry(janela, placeholder_text='Usuario')

senha = customtkinter.CTkEntry(janela, placeholder_text='Senha', show='*')

botao = customtkinter.CTkButton(janela, text='Login', command='Clique')

texto.pack(padx=10, pady= 10)
Usuario.pack(padx=10, pady= 10)
senha.pack(padx=10, pady= 10)
botao.pack(padx=10, pady= 10)

janela.mainloop()