print('--='*20)
imovel = float(input('Qual é o valor do imóvel? R$'))
sal = float(input('Qual o valor de sua renda? R$'))
tempo = int(input('Em quantos anos pretende pagar o imóvel?'))
meses = tempo * 12
prestacao = imovel / meses
triporcento = (sal / 100) * 30
if prestacao > triporcento:
    print('Para pagar uma casa de R${:.2f} reais em {} anos a prestação será de R${:.2f} reais '.format(imovel, tempo, prestacao))
    print('Empréstimo NEGADO.')
else:
    print('Para pegar uma casa de R$ {:.2f} reais em {} anos a prestação será de {:.2f} reais. '.format(imovel, tempo, prestacao))
    print('Empréstimo Aceito')