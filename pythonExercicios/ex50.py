soma = 0
cont = 0
print('')
for c in range(1, 7, 1):
    nu = int(input('Numero {}: '.format(c)))
    if nu % 2 == 0:
        soma = soma + nu
        cont = cont + 1
if cont == 1:
    print('O resultado da soma é {}, voce informou {} número par. '.format(soma, cont))
elif cont > 1:
    print('O resultado da soma é `{}, você informou {} números pares. '.format(soma, cont))
else:
    print('não há número PAR na contagem! ')

