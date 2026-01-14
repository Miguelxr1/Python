from math import hypot

c_a = int(input('Digite o valor do cateto oposto: '))
c_b = int(input('Digitte o valor do cateto adjasente: '))
h = hypot(c_a, c_b)

print(f'O valor da hipotenusa é: {h:.2f}')
