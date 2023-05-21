import math
co = float(input('Comprimento do cateto: '))
ca = float(input('Comprimento do cateto adicional: '))
hi = math.hypot(co, ca)

print(f'A hipotenusa vai medir {hi:.2f}')