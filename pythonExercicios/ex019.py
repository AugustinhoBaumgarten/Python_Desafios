print('============= Exercício 019 ==============')
import random
print('Um professor quer sortear um dos seus quatro alunos para apagar o quadro sendo eles:')
a = str(input('Aluno N°1:'))
b = str(input('Aluno Nº2:'))
c = str(input('Aluno N°3:'))
d = str(input('Aluno N°4:'))
lista = [a,b,c,d]
print('O(A) aluno escolhido foi : {}.'.format(random.choice(lista)))


#ou pode fazer
#from random import choice
#ai nao precisa por (random.choice(lista)) só coloca choice(lista)
