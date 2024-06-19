print('--='*20)
print('Anaisador de triângulos')
print('--='*20)

r1 = int(input('Qual é o tamanho da primeira reta?'))
r2 = int(input('Qual é o tamanho da segunda reta?'))
r3 = int(input('Qual é o tamanho da terceira reta?'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print('Os segmentos acima podem formar um triângulo.')
else:
    print('Os segmentos acima não podem formar um triângulo.')
