print('============= Exercício 011 ==============')
larg=float(input('Qual a largura de sua parede em metros ?'))
alt=float(input('Qual a altura de sua parede em metros ?'))
area = larg * alt
tinta =  area / 2
print('A sua parede tem a dimensão de {} x {} e sua área é de {}m²'.format(larg, alt, area))
print('Será necessário : {} litros de tinta.'.format(tinta))
