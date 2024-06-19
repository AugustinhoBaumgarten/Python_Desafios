print ('~~//' *20)

vel = int(input('Escreva a velocidade do carro em Km/h '))
multa = (vel - 80) * 7
if vel > 80:
    print('Você passou o limite de velocidade! \nDevido esta infração você foi multado em R$ {} reais'.format(multa))
else:
    print('Tudo ok! você está dentro do limite de velocidade.')
    