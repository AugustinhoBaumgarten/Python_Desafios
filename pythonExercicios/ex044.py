import time
import random

print('--=' * 20)
print(''' SUAS OPÇÕES
[0] PEDRA \U0001f48e
[1] PAPEL  \U0001f9fb
[2] TESOURA \u2702\uFE0F ''')

itens = ('Pedra', 'Papel', 'Tesoura')
fig = ('\U0001f48e', '\U0001f9fb', '\u2702\uFE0F')
esc = input('Qual é sua jogada? ')
pc = random.randint(0, 2)
valido = True

if esc == '0':
    esc = 0
elif esc == '1':
    esc = 1
elif esc == '2':
    esc = 2
else:
    print('INVÁLIDO, DIGITE UM NÚMERO VÁLIDO! ')
    valido = False

if not valido:
    print('Acabou')
else:
    time.sleep(0.7)
    print('JOO')
    time.sleep(0.7)
    print('KEEN')
    time.sleep(0.7)
    print('POOO!!')
    time.sleep(1)
    print('--=' * 30)

    print('{:=^50}'.format(
        ' Computador {} / {}  Jogador '.format(fig[pc], fig[esc])))

    if pc == 0:
        if esc == 0:
            print('EMPATE')
        elif esc == 1:
            print('JOGADOR VENCEU')
        elif esc == 2:
            print('COMPUTADOR VENCEU')
    elif pc == 1:
        if esc == 0:
            print('COMPUTADOR VENCEU')
        elif esc == 1:
            print('EMPATE')
        elif esc == 2:
            print('JOGADOR VENCEU')
    elif pc == 2:
        if esc == 0:
            print('JOGADOR VENCEU')
        elif esc == 1:
            print('COMPUTADOR VENCEU')
        elif esc == 2:
            print('EMPATE')