n = [2, 5, 3, 1] #Criação da lista
print()
print(n)
print()

n[1] = 3 #alteração de um dado na lista
print(n)
print()

n.append(7) #adicionando um elemento no final da lista
print(n)
print()

n.sort() #colocando a lista em ordem
print(n)
print()

n.sort(reverse=True) #colocando a lista em ordem reversa
print(n)
print()

n.insert(2, 2) # adicionando um novo elemento em qualquer lugar da lista, aonde o primeiro número é o local e o segundo é o número que será inserido.
print(n)
print()

#n.pop(2)  O comando pop remove um elemento da lista, se ele estiver vazio por dentro ele remove o último elemento

n.remove(2) # O comando remove remove o primeiro caso de ocorrência na lista, ou seja, se tiver um elemento repetido ele vai remover somente o primeiro, como no caso dos dois números 2 nessa lista
print(n)
print()

#
valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for c, v in enumerate(valores):
    print(f"Na posição {c} encontrei o valor {v}")
print('Cheguei ao final da lista.')
print()

# No exemplo a seguir vai ocorrer uma ligação entre listas:

a = [2, 3, 4, 7]
b = a
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
print()

# Amaniera correta de se copiar uma lista é a seguinte:
x = [2, 3, 4, 7]
y = x[:]
y[2] = 8
print(f'Lista X: {x}')
print(f'Lista Y: {y}')
print()
