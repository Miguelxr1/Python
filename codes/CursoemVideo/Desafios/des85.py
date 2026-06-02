n = [[], []]
v =0

for i in range(0, 7):
    v = int(input("Digite um número: "))
    if v % 2 == 0:
        n[0].append(v)
    elif v % 2 != 0:
        n[1].append(v)
n[0].sort()
n[1].sort()
print('-----'*20)
print(f'Os valores Pares são: {n[0]}')
print(f'Os valores impares são: {n[1]}')
