from time import sleep

s = ''
ss = ['M', 'F']

while s not in ss:
    s = str(input('Digite seu sexo [M/F]: ')).upper().strip()
    sleep(1)
    if s != 'M' and s != 'F':
        print('Dado inválido, por favor digite-o novamente.')
        sleep(1)
if s == 'M':
    print('Entõ você é um Homem!')
elif s == 'F':
    print('Então você é uma mulher!')
