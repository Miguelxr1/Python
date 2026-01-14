#Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada

n = int(input('Digite um número inteiro qualquer:'))
n2 = n*2
n3 = n*3
n4 = n*4
n5 = n*5
n6 = n*6
n7 = n*7
n8 = n*8
n9 = n*9
n10 = n * 10

print('A tabuada completa do seu número é:\n{}\n{} X  1 = {}\n{} X  2 = {}\n{} X  3 = {}\n{} X  4 = {}\n{} X  5 = {}'.format(('-'*20),n,n,n,n2,n,n3,n,n4,n,n5))
print('{} X  6 = {}\n{} X  7 = {}\n{} X  8 = {}\n{} X  9 = {}\n{} X 10 = {}\n{}'.format(n,n6,n,n7,n,n8,n,n9,n,n10, ('-'*20)))
#Pode se usar, também, operações dentor do format Ex. de multiplicado por 5: print('{} X 5 = {}'.format(n, (n*5)))
#Use caso não precise gerar variáveis para isso, pois não irá usa-las depois
