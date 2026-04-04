valores = []

while True:
    n = int(input('Digite um valor: '))
    if n not in valores:
        valores.append(n)
        print('Valor adicionado com sucesso!')
    elif n in valores:
        print('Valor duplicado, não vou adicionar...')
    p = input('Você quer continuar? [S/N] ').upper().strip()
    if p == "N":
        valores.sort()
        break
print(valores)
