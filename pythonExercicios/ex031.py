print('--='*20)

dist = float(input('Qual é a distância da viagem em KM? '))
if dist <= 200:
    preco = 0.50 * dist
    print('O preço da passagem será de R${:.2f} reais'.format(preco))
else:
    preco = 0.45 * dist
    print('O preço da passagem será de R${:.2f} reais'.format(preco))

print('--='*20)