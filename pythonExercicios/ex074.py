a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor:'))
c = int(input('Digite o terceiro valor: '))
d = int(input('Digite o quarto valor: '))

tupla = (a, b, c, d)
print(f'Você digitou os valores `{tupla}')
print(f'O valor 9 apareceu {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'O valor 3 apareceu na posição Nº{tupla.index(3)}')
else:
    print('O valor 3 não foi digitado.')
print('Os valores pares são:')
for e in tupla:
    if e % 2 == 0:
        print(e, end=', ')
