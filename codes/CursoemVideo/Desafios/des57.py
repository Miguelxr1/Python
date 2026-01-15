from time import sleep

s = ''

while s != 'M' and s != 'F':
    s = str(input('Digite seu sexo [M/F]: '))
    sleep(1)
    if s != 'M' and s != 'F':
        print('Dado inválido, por favor digite-o novamente.')
        sleep(1)
if s == 'M':
    print('Entõ você é um Homem!')
elif s == 'F':
    print('Então você é uma mulher!')
