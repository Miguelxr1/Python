#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos doláres ela pode comprar.
#Considere:  US$1,00 = R$3,27

r = float(input('Quantos reais você tem? Use pontos no lugar de vígulas. R$'))
d = float(r/3.27)

print('Com essa quantidade de dinheiro você pode comprar US${:.2f}'.format(d))
