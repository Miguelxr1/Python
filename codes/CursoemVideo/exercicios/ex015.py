d = int(input('quantos dias você rodou no carro? '))
Km = float(input('quantos Km você rodou? '))
a = (d*60) + (Km*0.15)

print('O preço a pagar é: R${:.2f}'.format(a))
