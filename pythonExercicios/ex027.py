import random #pode usar tbm from random import randint para facilitar a lista exemplo [0,5]
from time import sleep
lista = [0,1,2,3,4,5]
lista1 = random.choice(lista) # computador pensando, se fosse from randit era só usar na lista [0,5]
print('-=-' * 20)
print('Vou pensar em um número entre 0 a 5, tente adivinhar...')
print('-=-' * 20)
pensar = int(input('Em que número eu pensei?: '))
print('PROCESSANDO...')
sleep(3)
if lista1 == pensar:
    print('Você acertou! o número que eu pensei era exatamente {}'.format(lista1))
else:
    print('Que pena, você errou! o número que eu pensei era {}'.format(lista1))

#from rangom import randint
