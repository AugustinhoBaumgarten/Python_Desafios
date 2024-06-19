print('=='*30)

print('--'*20)
print('Cadastre uma pessoa')
print('--'*20)
maior = 0
homem = 0
fsub20 = 0

while True:
    sex = ' '
    id = int(input('Idade: '))
    while sex not in 'MmFf':
        sex = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if id > 18:
        maior += 1
    if sex == 'M':
        homem += 1
    if sex == 'F' and id < 20:
        fsub20 += 1
    print('--' * 20)
    perg = ' '
    while perg not in 'SsNn':
        perg = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if perg == 'N':
        break
print(f'''Total de pessoas com mais de 18 anos: {maior}
Ao todo temos {homem} homens cadastrados e 
Temos {fsub20} mulheres com menos de 20 anos. ''')

