s = float(input('Qual é o seu salário atual? Use somente números e no lugar das vígulas coloque pontos. R$'))
d = float(input('Quantos porcento de aumento você receberá?'))
v = s+(s*(d/100))

print('Com {}% de aumento você passará a receber: R${:.2f}'.format(d, v))
