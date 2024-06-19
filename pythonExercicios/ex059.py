print('===' * 30)

verdade = True
n1 = float(input('Digite primeiro valor: '))
n2 = float(input('Digite Segundo valor: '))
opcao = 0

print('xxx'* 10)
print('''[1] Soma \n[2] Multiplicar \n[3] Maior \n[4] Novos números \n[5] Sair do programa''')
print('xxx'* 10)

while opcao != 5:
    opcao = int(input('>>>>>> Qual é sua opção? '))
    soma = n1 + n2
    mult = n1 * n2
    print('xxx' * 10)
    if opcao == 1:
        print('A soma entre {} + {} é {}'.format(n1, n2, soma))
    elif opcao == 2:
        print('A multiplicação entre {} x {} é {}'.format(n1, n2,mult))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        elif n2 > n1:
            maior = n2
        else:
            maior = ('NÃO HÁ, AMBOS SÃO IGUAIS')
        print('O maior número entre {} e {}: {}'.format(n1, n2, maior))
    elif opcao == 4:
        n1 = float(input('Digite o primeiro valor: '))
        n2 = float(input('Digite o segundo valor: '))
    elif opcao > 5 or opcao < 1:
        print('*INVÁLIDO*, DIGITE UM NÚMERO VÁLIDO!!')
print('Fim do programa, obrigado por participar.')
