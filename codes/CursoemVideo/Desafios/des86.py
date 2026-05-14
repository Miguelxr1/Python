matriz = list()
n = list()
c = 0

for i in range(0, 9):
    if c == 0:
        n.append(int(input('Digite um número para a posição [0, 0]: ')))
    elif c == 1:
        n.append(int(input('Digite um número para a posição [0, 1]: ')))
    elif c == 2:
        n.append(int(input('Digite um número para a posição [0, 2]: ')))
    elif c == 3:
        n.append(int(input('Digite um número para a posição [1, 0]: ')))
    elif c == 4:
        n.append(int(input('Digite um número para a posição [1, 1]: ')))
    elif c == 5:
        n.append(int(input('Digite um número para a posição [1, 2]: ')))
    elif c == 6:
        n.append(int(input('Digite um número para a posição [2, 0]: ')))
    elif c == 7:
        n.append(int(input('Digite um número para a posição [2, 1]: ')))
    elif c == 8:
        n.append(int(input('Digite um número para a posição [2, 2]: ')))
    c += 1
    matriz.append(n[:])
    n.clear()

print(matriz[0], matriz[1], matriz[2])
print(matriz[3], matriz[4], matriz[5])
print(matriz[6], matriz[7], matriz[8])
