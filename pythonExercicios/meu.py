print('=='*25)
print('{:~^50}'.format(' RECURSOS HUMANOS '))
print('=='*25)
c = 0
catmaior = 0
catmenor = 0
nomemaior = ''
nomemenor = ''
maiorsal = 0
menorsal = 0
cont = 0
totbru = 0
insento = 0
cat = 0
ir = 0
saliq = 0

emp = str(input('> Nome da Empresa: ')).capitalize().strip()
nu = int(input('> Número de Funcionários: '))

while cont < nu:
    cont += 1

    nome = str(input('> Nome do funcionário: ')).strip().capitalize()
    hora = int(input('> Número de horas trabalhadas: '))
    while cat < 1 or cat > 3:
        cat = int(input('> Categoria do trabalhador: '))
    if cat == 1:
        cat = 15
        c = 1
    elif cat == 2:
        cat = 30
        c = 2
    elif cat == 3:
        cat = 50
        c = 3


    if hora > 160:
        extra = (hora - 160)
        totextra = (extra * cat / 100) * 50
        sal = (hora - extra) * cat
        salb = sal + totextra
        inss = (salb / 100) * 8
        dinss = salb - inss
    else:
        salb = hora * cat
        inss = (salb / 100) * 8
        dinss = salb - inss

    if dinss <= 2500:
        ir = '> INSENTO <'
        saliq = salb
        insento += 1

    elif dinss > 2500 or dinss <= 5000:
        ir = (salb / 100) * 10
        saliq = salb - ir

    elif dinss > 5000 or dinss <= 8000:
        ir = (salb / 100) * 20
        saliq = salb - ir
    elif dinss > 8000:
        ir = (salb / 100) * 30
        saliq = salb - ir

    totbru += salb

    if menorsal == 0:
        menorsal = saliq
        nomemaior = nome
        maiorsal = saliq
        nomemenor = nome
        catmenor = c
        catmaior = c

    if saliq > maiorsal:
        maiorsal = saliq
        nomemaior = nome
        catmaior = c

    if saliq < menorsal:
        menorsal = saliq
        nomemenor = nome
        catmenor = c

    print('=='*25)
    print(f'''
            >> Funcionário N°{cont}\n          
            >> NOME DA EMPRESA: {emp}\n
            >> NOME: {nome}\n 
            >>CATEGORIA: {c}\n 
            >>SALÁRIO BRUTO: {salb}\n 
            >>DESC.INSS: {inss}\n 
            >>DESC. IR: {ir}\n 
            >>SALÁRIO LIQUIDO: {saliq}  ''')
    print('=='*25)

print('{:-^25}'.format(f'{emp}'))
print(f'> O total de salários bruto é de {totbru}')
print(f'> A média de salários bruto é de {totbru / nu}')
print(f'> O total de incentos do Imposto de renda é {insento} (percentual de funcionários:{(insento * 100) / nu}%)')
print(f'O salário líquido de MENOR remuneração é de {nomemenor} no valor de R${menorsal} reais, '
      f'sua categoria é Nº{catmenor}')
print(f'O salário líquido de MAIOR remuneração é de {nomemaior} no valor de R${maiorsal} reais, '
      f'sua categoria é Nº{catmaior}')
