print('============= Exercício 018 ==============')
import math
angulo = float(input('Digite o angulo que voce deseja: '))
seno = math.sin(math.radians(angulo))
print('O ângulo de {} tem seno de{:.2f}'.format(angulo, seno))
cos = math.cos(math.radians(angulo))
print('O ângulo de {} tem Cosseno de {:.2f}'.format(angulo, cos))
tan = math.tan(math.radians(angulo))
print('O ângulo de {} tem como Tangente {:.2f}'.format(angulo, tan))


#from math import radians, sin, cos,tan
#an = float(input('digite um numero'))
#seno = sin(radians(angulo))#

