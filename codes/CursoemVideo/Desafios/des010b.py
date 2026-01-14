r = float(input('Quantos reais você tem? Use pontos no lugar de vígulas.'))
c = float(input('Qual é a cotação do dolár atual?'))
d = float(r/c)

print('Com essa quantidade de dinheiro você pode comprar US${:.2f}'.format(d))
