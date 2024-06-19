print('=' * 40)
print(f'{"Separador de Vogais":^40}')
print('=' * 40)
pal = ('APRENDER',
       'PROGRAMAR',
       'LINGUAGEM',
       'PYTHON',
       'CURSO',
       'GRATIS',
       'ESTUDAR',
       'PRATICAR',
       'TRABALHAR',
       'MERCADO',
       'PROGRAMADOR',
       'FUTURO')


for c in pal:
    print(f'\n na palavra :{c} temos:', end='')
    for letra in c:
        if letra.upper() in 'AEIOU':
            print(letra, end=' ')
