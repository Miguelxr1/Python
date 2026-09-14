import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de R${p:.2f} é R${moeda.metade(p)}')
print(f'O dobreo de R${p:.2f} é R${moeda.dobro(p)}')
print(f'Aumentando 10% de R${p:.2f}, temo R${moeda.aumentar(p, 10)}')
print(f'Reduzindo 13% de R${p:.2f}, temos R${moeda.diminuir(p, 13)}')

