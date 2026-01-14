#Coisas que eu aprendo e treino nas aulas

import time

nome = input('Qual é seu nome?')

print('Olá {}. Seja bem vindo.'.format(nome))

time.sleep(0.5)

dia = int(input('Que dia você nasceu?'))
mes = str(input('Que mês você nasceu?'))
ano = int(input('Que ano você nasceu?'))

print('Você nasceu no dia {}, no mês {} e no ano {}'.format(dia, mes, ano))

time.sleep(1)

n1 = int(input('{}, digite um número inteiro:'.format(nome)))
n2 = int(input('Digite outro número inteiro:'))
s1 = n1 + n2
n3 = float(input('{}, agora digite um número real, ou seja, com uma, ou mais, casas décimais:'.format(nome)))
n4 = float(input('Digite outro número real:'))
s2 = n3 + n4

print('A soma dos números inteiros, {} e {}, é: {}'.format(n1, n2, s1))
print('a soma dos números reais, {} e {}, é: {}'.format(n3, n4, s2))

time.sleep(0.5)

print('Obrigado pela participação {}. Tchau!'.format(nome))
