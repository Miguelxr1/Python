p = float(input('Quanto custa o produto? Coloque só os números e no lugar da virgula use ponto. R$'))
a = int(input('De quantos porcento será o desconto?'))
v = p-(p*(p/100))

print('O valor do produto com {}% de desconto é: RS${:.2f}'.format(a, v))
