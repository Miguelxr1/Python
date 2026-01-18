valido = False

while not valido:
    entrada = input("Digite um inteiro não-negativo: ").strip()
    try:
        n = int(entrada)
        if n < 0:
            print("Número negativo. Digite um inteiro não-negativo.")
        else:
            valido = True
    except:
        print("Entrada inválida. Digite um número inteiro.")

resultado = 1
partes = []

for i in range(n, 0, -1):
    partes.append(str(i))
    resultado = resultado * i

if n == 0:
    partes = ["1"]
    resultado = 1

expressao = " X ".join(partes)

print(f"{n}! = {expressao} = {resultado}")
