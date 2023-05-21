print('       BOLETIM ESCOLA      ')
print('-' * 35)
aluno = str(input('Aluno: '))
nota1 = float(input('1° Bimestre nota: '))
nota2 = float(input('2° Bimestre nota: '))
nota3 = float(input('3° Bimestre nota: '))
nota4 = float(input('4° Bimestre nota: '))
media = (nota1 + nota2 + nota3 + nota4) /4
print('-' * 35)

print(f'A media do aluno {aluno} e {media}')
if media <= 3:
    print(f'{aluno} INFELIZMENTE VOCE FOI REPROVADO')
elif media <= 5:
    print(f'{aluno} RECUPERAÇÃO')
elif media >= 5.5:
    print(f'{aluno} PARABENS VOCE FOI APROVADO')

print('SISTEMA ENCERRADO')