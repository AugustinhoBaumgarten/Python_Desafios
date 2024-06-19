import random

pc = random.randint(0, 10)
soma = 1
print('Sou seu computador...')
print('''Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi?''')
p = int(input('Qual é seu palpite? '))

while p != pc:
    soma = soma + 1
    if p > pc:
        p = int(input('Menos... Tente mais uma vez: '))
    elif p < pc:
        p = int(input('Mais... Tente mais uma vez: '))
print('Você acertou com {} tentativas. Parabéns! '.format(soma))

