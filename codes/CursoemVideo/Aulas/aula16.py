lanche = ("Hamburguer", "Suco", "pizza", "Pudim")

print(lanche)
print(lanche[1])
print(lanche[3])
print(lanche[-2])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])
print(lanche[-2:])

#Tuplas são imutáveis
print("-----" * 20)
#print(lanche[1])
#lanche[1] = "Refrigerante"
#print(lanche[1])
#Esta parte de cima dá erro se for executada, e esta parte de baixo é a parte que usamos o for
for comida in lanche:
    print(f"Eu cou comer {comida}")

for cont in range(0, len(lanche)):
    print(f"Eu vou comer {lanche[cont]} na posição {cont}")

for pos, comida in enumerate(lanche):
    print(f"Eu vou comer {lanche[pos]} na posição {pos}")

print("Comi pra caramba!")

#usando o método sorted
print("-----" * 20)
print(sorted(lanche))

#
print("-----" * 20)
a = (2, 5, 4)
b = (5, 8, 1 , 2)
c = a + b

print(c)
print(c.count(9))
print(c.index(8))
print(c.index(5, 1))

#
print("-----" * 20)
pessoa = ("Miguel", 14, "M", 85)
#del(pessoa)
print(pessoa)
