import random
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
print(f'Sua senha é {senha}')