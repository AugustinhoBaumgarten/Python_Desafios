print('-'*30)
print('      JOGA NA MEGA SENA       ')
print('-'*30)
from random import randint
from time import sleep
jogos = [0, 0, 0, 0, 0, 0]

tot = int(input('Quantos jogos você quer que eu sorteie? '))
print()
print('-='*3, f'Sorteando {tot} jogos', '-='* 3 )

for pos in range(0, tot):
    for l in range(0, 6):
        jogos[l] = randint(1, 60)
    jogos.sort()
    print(f'jogo {pos + 1}: {jogos}')
    sleep(1)
print('-='*3, f'< BOA SORTE ! >', '-='* 3 )


