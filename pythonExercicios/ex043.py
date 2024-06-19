print('--='*20)
alt = float(input('Escreva a sua altura:'))
peso = float(input('Escreva seu peso: '))
imc = peso / (alt ** 2)
if imc < 18.5:
    print('Você está a baixo do peso.')
elif imc > 18.5 and imc <= 25:
    print('Você está com o peso ideal.')
elif imc > 25 and imc <= 30:
    print('Você está com sobrepeso.')
elif imc > 30 and imc <= 40:
    print('Você está com obesidade.')
else:
    print('Você está com obesidade morbida.')

