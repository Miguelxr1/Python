matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
sp = 0
s3 = mai = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-----'*20)

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            sp += matriz[l][c]
        if l == 1:
            if matriz[l][c] > mai:
                mai = matriz[l][c]
    s3 += matriz[l][c]
    print()
print('-----'*20)

print(f'A soma dos valores pares é: {sp}')
print(f'A soma dos valores da terceira coluna é: {s3}')
print(f'O maior valor da segunda linha é da segunda linha é: {mai}')
