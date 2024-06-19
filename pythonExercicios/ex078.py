maior = 0
menor = 0

valor = []

for v in range(0, 5):
    valor.append(int(input(f'Digite um valor na posição {v}: ')))
    if v == 0:
        maior = menor = valor[v]
    else:
        if valor[v] > maior:
            maior = valor[v]

        if valor[v] < menor:
            menor = valor[v]
print(f'OS valores digitados foram: {valor}')
print(f' O maior valor é {maior} nas posições: ', end='')
for pos, nu in enumerate(valor):
    if nu == maior:
        print(f'{pos}... ', end='')

print(f'\n O menor valor é {menor} nas posições: ', end='')
for pos, nu in enumerate(valor):
    if nu == menor:
        print(f'{pos}...', end='')