n = list()
par = list()
impar = list()

for i in range(0, 7):
    p = int(input("Digite um número: "))
    if p % 2 == 0:
        par.append(p)
    elif p % 2 != 0:
        impar.append(p)
par.sort()
impar.sort()
n.append(par[:])
n.append(impar[:])
print(f'\nOs valores Pares são: {n[0]}')
print(f'Os valores impares são: {n[1]}')
