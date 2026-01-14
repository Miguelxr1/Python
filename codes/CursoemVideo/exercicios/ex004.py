a = input('Digite algo:')

print('Tipo primitivo:', type(a)) #mostra o tipo primitivo. Ex.: 'str'
print('Só tem espaços?', a.isspace()) #mostra se é somente espaços. Ex.: '   '
print('É um número?', a.isnumeric()) #mostra se é numérico. Ex.: '5'
print('É alfabético?', a.isalpha()) #mostra se é alfabético. Ex.: 'a'
print('É alfanumérico?', a.isalnum()) #mostra se é alfanumérico. Ex.: '5a'
print('Está em maiúsculo?', a.isupper()) #mostra se está em maiúsculo. Ex.: 'PYTHON'
print('Está em minúsculo?', a.islower()) #mostra se está em minúsculas. Ex.: 'python'
print('Está capitalizada?', a.istitle()) #mostra se está capitalizada. Ex.: 'Python'
