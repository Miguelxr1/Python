#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

nome = input('Seu nome:')
n1 = float(input('Sua primeira nota:'))
n2 = float(input('Sua segunda nota:'))
s = n1+n2
m = s/2  #Ou assim: m = (n1+n2)/2 | Desse jeito não é nescessario a var s

print('{} a média das sua notas é: {:.1f}'.format(nome, m))
