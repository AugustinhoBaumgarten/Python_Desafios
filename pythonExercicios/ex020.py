print('============= Exercício 020 ==============')
import random
a= str(input('Aluno Nº1: '))
b= str(input('Aluno N°2: '))
c= str(input('Aluno N°3: '))
d= str(input('Aluno N°4: '))
lista = [a, b, c, d]
random.shuffle(lista)
print('A ordem da apresentação será: ')
print(lista)

