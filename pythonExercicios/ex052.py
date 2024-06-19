nu = int(input(' Digite um número: '))
tot = 0
for c in range (1, nu + 1):
    if nu % c == 0:
        tot = tot + 1
        print('\033[33m', end='')
    else:
        print('\033[31m', end='')

    print('{} '.format(c), end='')
print('\n\033[mO numero {} foi divisível {} vezes'.format(nu, tot))
if tot ==2 :
    print('Por isso é primo.')
else:
    print('Por isso não é primo.')