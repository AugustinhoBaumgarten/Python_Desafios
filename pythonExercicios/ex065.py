print('==='*30)
cont = 1
nu = int(input('Digite um número: '))
sn = str(input('Deseja continuar [S/N]: ')).strip().upper()
soma = nu
maior = nu
menor = nu

while sn != 'N':
    cont = cont + 1
    nu = int(input('Digite um número: '))
    sn = str(input('Deseja continuar [S/N]: ')).strip().upper()
    soma = soma + nu
    media = soma / cont
    if maior == nu:
        menor = nu
    if nu > maior:
        maior = nu
    if nu < menor:
        menor = nu


print('Você digitou {} números a soma de todos daria {} e a média foi {:.1f}'.format(cont, soma, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))