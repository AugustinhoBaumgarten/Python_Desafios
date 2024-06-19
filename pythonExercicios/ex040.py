print('--='*20)
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2) / 2
if m < 5.0:
    print('Sua média foi {:.1f}, REPROVADO! '.format(m))
elif m >= 5.0 and m <= 6.9:
    print('Sua média foi {:.1f}, em RECUPERAÇÃO '.format(m))
elif m >= 7.0 and m <= 10:
    print('Sua média foi {:.1f}, APROVADO!'.format(m))
else:
    print('Média inválida,valor não está entre 0 a 10.')