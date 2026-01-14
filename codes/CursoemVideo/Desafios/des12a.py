#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

p = float(input('Quanto custa o produto? Coloque só os números e no lugar da virgula use ponto. R$'))
v = p-(p*0.05)

print('O valor do produto com 5% de desconto é: RS${:.2f}'.format(v))
