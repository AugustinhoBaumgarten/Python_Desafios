print('===========Desafio 04 ============')
n=input ('Digite algo: ')
print('qual é o tipo primitivo deste valor: ', type(n))
print('só tem espaços?', n.isspace())
print('é um numero?',n.isnumeric())
print('é alfabético?', n.isalpha())
print('é alfanumérico?', n.isalnum())
print('está em maiúsculo?', n.isupper() )
print('está em minúsculo?', n.islower())
print ('está capitalizada?', n.istitle())