produto = str(input('Nome do produto? '))
preco = float(input('Qual é o preço do produto? '))
desconto = preco - (preco * 5/100)
print(f'{produto} que custava R$ {preco:.2f} na promoção com desconto de 5% esta saindo a R$ {desconto:.2f}')