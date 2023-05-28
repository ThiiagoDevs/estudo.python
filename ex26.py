frase = str(input("Esta é uma frase de exemplo. ")).upper().strip()
quantidade = frase.count('A')

print("A letra 'a' aparece", quantidade, "vezes na frase.")
print('A primeira letra A apreceu na posição {}'.format(frase.find('A')+1))
print('A ultima letra A aparece na posição {}'.format(frase.rfind('A')+1))