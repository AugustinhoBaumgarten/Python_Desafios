print('--='*20)
from datetime import date
nasc = int(input('Ano nascimento: '))
ano = date.today().year
idade = ano - nasc
print('O atleta tem {} anos. '.format(idade))
if idade <= 9:
    print('Classificação MIRIM ')
elif idade <=14:
    print('Classificação INFANTIL ')
elif idade <= 19:
    print('Classificação: JÚNIOR ')
elif idade <= 25:
    print('Classificaçã: SÊNIOR ')
else:
    print('Classificação: MASTER ')
    