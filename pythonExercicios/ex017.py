print('============= Exercício 017 ==============')
from math import sqrt
ca=float(input('digite um número referente ao cateto adjacente: '))
co=float(input('digite um número referente ao cateto oposto (não pode ser igual ao número anterior: '))
potencia = (ca**2) + (co**2)
print('A hipotenusa do triângulo retângulo é {:.2f}'.format (sqrt(potencia)))


