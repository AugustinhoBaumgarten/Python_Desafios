print('==='*30)
nu = 0
cont = 0
soma = 0

while True:
    nu = int(input('Digite um número: '))
    if nu == 999:
        break
    soma += nu
    cont = cont + 1
print(f'A soma dos {cont} valores foi: {soma}')
