print('=='*30)

while True:
    nu = ('Zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
    digite = int(input('Digite um número entre 0 e 20:'))
    while digite < 0 or digite > 20:
        digite = int(input('Inválido, digite novamente um número entre 0 e 20:'))
        print(f'Você digitou: {nu[digite]}')
        print('=='*30)
        perg = str(input('Deseja continuar? ')).strip().upper()[0]
        if perg in 'N':
            break
print('=='*30)
print('Fim do programa, obrigado por participar!')