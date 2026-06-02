#variables
n_50 = 0
n_20 = 0
n_10 = 0
n_1 = 0

while True:
    valor = int(input("Qual é o valor (número inteiro) que deseja sacar? R$"))
    
    if (valor // 50) >= 1:
        n_50 = (valor // 50)
        valor -= (valor // 50) * 50
    elif valor == 0:
        break
    if (valor // 20) >= 1:
        n_20 = (valor // 20)
        valor -= (valor // 20) * 20
    elif valor == 0:
        break
    if (valor // 10) >= 1:
        n_10 = (valor // 10)
        valor -= (valor // 10) * 10
    elif valor == 0:
        break
    if (valor // 1) >= 1:
        n_1 = (valor // 1)
        valor -= (valor // 1) * 1
    elif valor == 0:
        break
    if valor == 0:
        break

if n_50 >= 1:
    print(f"Total de {n_50} cédulas de R$50")
if n_20 >= 1:
    print(f"Total de {n_20} cédulas de R$20")
if n_10 >= 1:
    print(f"Total de {n_10} cédulas de R$10")
if n_1 >= 1:
    print(f"Total de {n_1} cédulas de R$1")
