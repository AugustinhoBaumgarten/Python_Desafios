p = list()
i = list()
while True:
    n = int(input('Digite um numero'))
    if n % 2 == 0:
        p.append(n)
    else:
        i.append(n)
    r= str(input('Quer continuar?'))
    if r in 'n':
        break
print(p)
print(i)