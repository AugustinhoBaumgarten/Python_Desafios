print('--='*20)
from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
sexo = str (input('Digite (M) masculino ou (F) feminino:')).upper()
idade = (atual - nasc)
if sexo == 'M' and idade < 18:
    falta = 18 - idade #vai me indicar quantos anos falta pra fazer 18
    ano = atual + falta #vai indicar o ano de serviço
    print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
    print('Ainda falta {} anos para o alistamento.'.format(falta))
    print('Seu alistamento será em {}'.format(ano))
elif sexo == 'M' and idade == 18:
    print('Você deve se alistar IMEDIATAMENTE!!')
elif sexo == 'M' and idade > 18:
    atraso = idade - 18
    ano = atual - atraso
    print('Você já deveria ter se alistado há {} anos'.format(atraso))
    print('Seu alistamento foi em {}'.format(ano))
elif sexo == 'F':
    print('Como seu sexo é feminino, o alistamento não é obrigatório. ')
else:
    print('Sexo inválido!')