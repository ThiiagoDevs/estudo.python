from random import choice

aluno1 = str(input('1° aluno: '))
aluno2 = str(input('2° aluno: '))
aluno3 = str(input('3° aluno: '))
aluno4 = str(input('4° aluno: '))
lista = [aluno1, aluno2, aluno3, aluno4]

escolhido = choice(lista)
print(f'O aluno(a) escolhido foi {escolhido}')