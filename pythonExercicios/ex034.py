print('--='*20)
print('----Aumento salarial ----')
print('--='*20)

sal = float(input('Qual é o seu salário atual? '))
if sal > 1250.00:
    aumento = (sal/100) * 10
    tot = sal + aumento
    print('Houve um aumento de R${:.2f} reais, totalizando R${:.2f} reais'.format(aumento, tot))
else:
    aumento = (sal/100) * 15
    tot = sal + aumento
    print('Houve um aumento de R${:.2f} reais, totalizando R$ {:.2f} reais'.format(aumento, tot))