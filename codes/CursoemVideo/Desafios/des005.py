import time

#Desafio: Faça um programa que leia um número e mostre na tela o seu sucessor e antecessor.

#Pensei assim:

n1 = int(input('Digite um número'))
s1 = n1+1
s2 = n1-1

print('O sucessor do seu número é: {}\ne seu antecessor é: {}'.format(s1, s2))

time.sleep(0.5)  #Ou assim:

n2 = int(input('Digite outro número:'))

print('O sucessor desse número é: {}\ne o antecessor é: {}'.format(n2+1, n2-1))
