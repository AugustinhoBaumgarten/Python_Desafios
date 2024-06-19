print('-=' * 30)
time = []
jogador = {}
gols = []
from time import sleep

while True:
    jogador.clear()
    gols.clear()

    jogador['Nome'] = str(input('Nome do jogador: ')).capitalize()
    partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    for c in range(0, partidas):
        gols.append(int(input(f' >Quantos gols na partida {c + 1}? ')))

    jogador['Gols'] = gols[:]
    jogador['Total'] = sum(gols)

    time.append(jogador.copy())

    while True:
        perg = str(input('Deseja continuar? '))
        if perg in 'SsNn':
            break
        print('ERRO! Digite S ou N.')
    if perg in 'Nn':
        break

print('-=' * 40)
print('Cod', end='')
for k in jogador.keys():
    print(f'  {k:<15}', end='')
print()
print('-=' * 40)

for k, v in enumerate(time):
    print(f'{k:>4}', end='')
    for d in v.values():
        print(f' {str(d):<15}', end='')
    print()
print('-='*40)

while True:
    esc = int(input('(999 para parar) Mostrar dados de qual jogador? '))
    if esc == 999:
        break
    if esc >= len(time):
        print(' >ERRO! digite um número válido ou 999 para parar')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[esc]["Nome"]}: ')
        for i, g in enumerate(time[esc]["Gols"]):
            print(f'No jogo {i + 1} fez {g} gols.')
            sleep(1)
print('~~~ FIM DE OPERAÇÃO, VOLTE SEMPRE ! ~~~')

    #tambem deu certo
     #   for c in range(0, len(time[esc]["Gols"])):
          #  print(f'No jogo {c + 1} fez {time[esc]["Gols"][c]} gols.')
