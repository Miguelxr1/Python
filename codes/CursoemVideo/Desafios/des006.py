import time

#Desafio: Crie um código que leia um número e mostre seu dobro, tripo e raiz quadrada.

#Pensei assim:

n1 = int(input('Digite um número:'))
d = n1*2
t = n1*3
r = n1**(1/2)

print('O dobro desse número é: {}, o tripo desse número é: {} e a raiz quadrada desse número é, aproximadamente: {:.2f}'.format(d, t, r))

time.sleep(0.5)  #E assim:

n2 = int(input('Digite outro número:'))

print('O dobro desse número é: {}, o tripo desse número é: {} e a raiz quadrada desse número é, aproximadamente: {:.2f}'.format(n2*2, n2*3, n2**(1/2)))
