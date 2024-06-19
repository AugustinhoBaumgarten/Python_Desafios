import random
print('-='*20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-='*20)
v = 0

while True:
    jogador = int(input('Diga um valor: '))
    pc = random.randint(0, 10)
    soma = jogador + pc
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I]: ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {pc}. Total de {soma}')
    print('...Deu par' if soma % 2 == 0 else '...Deu Impar')
    if tipo == 'P':
        if soma % 2 == 0:
            print('VocÊ venceu')
            v += 1
        else:
            print('VocÊ perdeu!')
            break


    elif tipo == 'I':
        if soma % 2 == 1:
            print('VocÊ venceu!!')
            v += 1
        else:
            print ('Voce perdeu!')
            break
    print('Vamos jogar novamente')
print(f'Game over, voce venceu {v} vezes')


