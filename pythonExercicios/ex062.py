print('==='*40)
print(''' - Gerador de PA - 
(10 primeiros termos)''')
print('--='*10)

primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))
mais = 10
termo = primeiro
cont = 1
total = 0
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} - '.format(termo), end='')
        termo = termo + razao
        cont = cont + 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais?'))
print('Programa encerrado com {} termos mostrados, obrigado por participar!'.format(total))
