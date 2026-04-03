np = []
ns = []

for i in range(4):
    if i == 0:
        ns.append(int(input("Digite um número: ")))
    else:
        ns.append(int(input("Digite outro número: ")))
ns = tuple(ns)

for par in ns:
    if (par % 2) == 0:
        np.append(par)
np = tuple(np)

print(f"o número 9 apareceu {ns.count(9)} vez(eses)")
if 3 in ns:
    print(f"O primeiro número três apareceu na posição {(ns.index(3)) + 1}")
else:
    print("O número 3 não foi digitado")
if np == ():
    print("Não houve valores pares digitados")
else:
    print(f'Os valores pares digitados foram: {np}')
