import time

#\n para quebrar linha
#para não quebrar linha: end=' ' no final do print
#Operador '+' adição
#Operador '-' subtração
#Operador '*' multiplicação
#Operador '/' divisão
#Operador '**' potência, pode ser feita assim: pow(a,b), porém perde a precedência
#Operador '//' divisão inteira
#Operador '%' resto da divisão
#raiz quadrada: a**(1/2)
#o sinal de '==' quer dizer que é igual

#ordem de precedência:
#1º '()';
#2º '**';
#3º '*', '/', '//', '%';
#4º '+', '-'

nome = input('Qual é seu nome?')
print('Prazer em te conhecer {}!'.format(nome))
print('Prazer em te conhecer {:20}!'.format(nome)) #aparecer o que está na variável em 20 espaços
print('Prazer em te conhecer {:>20}!'.format(nome)) #aparecer o que está na variável alinhado na direita em 20 espaço
print('Prazer em te conhecer {:<20}!'.format(nome)) #aparecer o que está na variável alonhado na esquerda em 20 espaços
print('Prazer em te conhecer {:^20}!'.format(nome)) #aparecer o que está na variável centralizado em 20 espaços

time.sleep(0.25)

n1 = int(input('Digite um valor:'))
n2 = int(input('Outro valor:'))
s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1**n2

print('A soma é {}, \na multiplicação é {} \ne a divisão é {:.3f}'.format(s, m, d), end=' ')
print('e a divisão inteira é {} \ne a potência é {}'.format(di, e))
