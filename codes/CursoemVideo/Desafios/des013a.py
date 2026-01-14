#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo sslário, com 15% de aumento

s = float(input('Qual é o seu salário atual? Use somente números e no lugar das vígulas coloque pontos. R$'))
v = s+(s*0.15)

print('Com 15% de aumento você passará a receber: R${:.2f}'.format(v))
