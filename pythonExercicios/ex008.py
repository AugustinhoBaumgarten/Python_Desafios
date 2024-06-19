print('============= Exercício 008 ==============')
n1 = float(input('Escreva qual o tamanho em metros:'))
km = n1 / 1000
hm = n1 / 100
dam = n1 / 10
dm =  n1 * 10
cm =  n1 * 100
mm =n1 * 1000
print('A medida convertida em todas medidas de comprimento fica:')
print('KM : {} \n HM: {} \n dam: {} \n M: {} \n DM: {} \n CM: {} \n MM: {}'. format(km, hm, dam, n1, dm, cm, mm))
