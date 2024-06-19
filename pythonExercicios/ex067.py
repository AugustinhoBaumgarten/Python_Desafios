print('==='*30)
nu = 0

print('----- Tabuada ----- ')

while True:
    nu = int(input('Digite um número para saber sua tabuada: '))
    if nu < 0:
        break
    for c in range(1, 11):
        a = nu * c
        print(f'{nu} x {c} = {a}')
    if nu < 0:
        break
print('PROGRAMA TABUADA ENCERRADO, VOLTE SEMPRE!!')