print('--='*40)
print('------ DIGA O TAMANHO DAS RETAS E VEREMOS SE FORMARÁ UM TRIÂNGULO E O SEU TIPO ------ \n (CONDIÇÃO ANINHADA)')
a = int(input('Primeiro segmento: '))
b = int(input('Segundo segmento: '))
c = int(input('Terceiro segmento: '))
if a < b + c and b < a + c and c < a + b:
    print('Os segmentos formam um triângulo!')
    if a != b != c != a: #condição aninhada está aqui! if dentro de if
        print(' Os segmento formam um triângulo ESCALENO. ')
    elif a== b == c:
        print('Os segmentos formam um triângulo EQUILÁTERO. ')
    else:
        print('Os segmentos formam um triângulo ISÓCELES. ')
else:
    print('Os segmentos acima não podem formar um triângulo!')