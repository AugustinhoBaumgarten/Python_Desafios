
print('{:=^60}'.format('Progressão aritmética '))
print('---'*10)
print('{:=^''}'.format('10 termos de uma PA'))
print('---'*10)
t1 = int(input('Primeiro termo: '))
raz = int(input('Razão: '))
dec = t1 + (10 - 1) *raz
for c in range (t1, dec, raz):
    print('{}'.format(c), end=' ')
print('Acabou')