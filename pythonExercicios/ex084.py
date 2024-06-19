print('=-'*40)
teste = list()
lista = []
mai = men = 0
while True:
    teste.append(str(input('Nome: ')))
    teste.append(float(input('Peso: ')))
    if len(lista) == 0:
        mai = men = teste[1]
    else:
        if teste[1] > mai:
            mai = teste[1]
        if teste[1] < men:
            men = teste[1]

    lista.append(teste[:])
    teste.clear()
    qnt = len(lista)
    r = str(input('Deseja continuar[S/N]? ')).strip().upper()[0]
    if r in 'N':
        break
print(f'Foram cadastradas {qnt} pessoas.')

for p in lista:
    if p[1] == mai:
        print(f'O(s) mais pesado(s) da lista:{p[0]} com {mai}kg')
    elif p[1] == men:
        print(f'O(s) mais leve(s) da lista: {p[0]} com {men}kg')