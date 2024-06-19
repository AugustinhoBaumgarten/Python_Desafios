times = ('corinthians', 'palmeiras', 'santos', 'grêmio',
         'cruzeiro', 'flamengo', 'vasco da gama',
         'chapecoense', 'atlético',' botafogo', 'atlético pr',
         'bahia', 'são paulo', 'Fluminense', 'Sport recife',
         'Ec vitória', 'coritiba', 'Avai', 'Ponte preta', 'Atlético Go')
print(f'Lista do brasileirão: {times}')
print('=='*40)

print(f'>>Os primeiros 5 times foram: `{times[0:5]}')
print('=='*40)

print(f'>> Os últimos 4 times foram: {times[16:]}')
print('=='*40)

print(f'>> Os times em ordem alfabética: {sorted(times)}')
print('=='*40)

print(f'>> O times chapecoense se encontra na posição Nº{times.index("chapecoense")}')
print('=='*40)