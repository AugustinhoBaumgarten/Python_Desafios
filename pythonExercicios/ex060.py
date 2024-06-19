print('==='*40)

cont = 1
nu = int(input('Digite um número: '))
c = nu
f = 1

print('Calculando {}!'.format(nu), end='')

while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f = f * c
    c = c - cont
print('{}'.format(f))