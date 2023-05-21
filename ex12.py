largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = largura * altura
print(f'Sua parede tem a dimensão de {largura} e {altura} e a sua area é de {area}m²')
tinta = area / 2
print(f'Para pintar essa parede, voce precisará de {tinta}L de tintas.')