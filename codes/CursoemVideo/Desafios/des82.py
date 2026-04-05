n = []
np = []
ni = []

while True:
    n.append(int(input('Digite um número: ')))
    while True:
        p = input('Você quer continuar? [S/N] ').upper().strip()
        if p == 'N':
            break
    if p == 'N':
        break
print()

for c in n:
    if c % 2 == 0:
        np.append(c)
    else:
        ni.append(c)
print(f'Lista de todos os números: {n}')
print(f'Lista dos números pares: {np}')
print(f'Lista dos números ímpares: {ni}')
