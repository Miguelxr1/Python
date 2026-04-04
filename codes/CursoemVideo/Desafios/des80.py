valores = []

for c in range(0, 5):
    print(valores)
    n =  int(input('Digite um númro: '))
    for v in valores:
        if n < v:
            valores.insert(valores.index(v), n)
            break
    else:
        valores.append(n)
print(valores)
