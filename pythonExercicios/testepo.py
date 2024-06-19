print('===========Desafio 04 ============')
n=input ('Digite algo: ')
print('qual é o tipo primitivo deste valor: '
print('só tem espaços? {}'
print('é um numero?{}'
print('é alfabético?{}'
print('é alfanumérico?{}'
print('está em maiúsculo{}?'
print('está em minúsculo?{}'
print ('está capitalizada?{}',.format (n.isspace(), n.isnumeric(),n.isalpha(),n.isalnum(),n.isupper(),n.islower(),n.istitle())