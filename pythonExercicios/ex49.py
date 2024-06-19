nu = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11, 1):
    print('{} x {:2} = {}'.format(nu, c, nu * c))