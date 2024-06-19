contador = 0
soma = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        contador = contador + 1
        soma = soma + c
print('A soma de todos os valores citados é {}'.format(soma))
print('A soma de todos valores executados é {}'.format(contador))
