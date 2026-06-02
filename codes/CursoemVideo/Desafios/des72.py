nums = ("Zero", "Um", "Dois", "Três", "Quatro", "Cinco", "Seis", 
        "Sete", "Oito", "Nove", "Dez", "Onze", "Doze", "Treze", 
        "Catorze", "Quinze", "Dezesseis", "Dezessete", "Dezoito", "Dezenove", "Vinte")

while True:
    n = int(input("Digite um número de 0 a 20: "))
    if n >= 0 and n <= 20:
        break
    else:
        print("Tente Novamente. ", end="")
print(f"Você digitou o número {nums[n]}")
