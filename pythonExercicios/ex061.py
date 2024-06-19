print('==='*40)

cont = 0
soma = 0

print(''' - Gerador de PA - 
(10 primeiros termos)''')
print('--='*10)

termo1 = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))

print('--='*10)

while cont != 10:
    cont = cont + 1
    print('{} - '.format(termo1), end='')
    if cont < 10:
        termo1 = termo1 + razao
print('FIM')