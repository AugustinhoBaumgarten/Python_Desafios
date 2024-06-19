print('============= Exercício 012 ==============')
preço=float(input('Qual o valor do produto desejado? '))
desconto = preço * 5 / 100
resultado = preço - desconto
print('O valor do produto que custava {:.2f} reais, na promoção com 5% de desconto será de R$ {:.2f} reais'.format(preço, resultado))