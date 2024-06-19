print('==='*40)

print(' ----- Loja Super Barato ----- ')
compra = 0
totmil = 0
barato = 0
prodbarato = ''

while True:
    prod = str(input('Nome do produto: '))
    preco = int(input('Preço R$: '))
    compra = compra + preco
    if preco > 1000:
        totmil += 1

    if barato == 0:
        barato = preco
        prodbarato = prod

    if preco < barato:
        barato = preco
        prodbarato = prod

    perg = ' '
    while perg not in 'SN':
        perg = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if perg == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi de R${compra:.2f} reais.')
print(f'Temos {totmil} produtos a cima de R$1000.00 reais.')
print(f'O produto mais barato foi {prodbarato} que custou R${barato:.2f} reais.')