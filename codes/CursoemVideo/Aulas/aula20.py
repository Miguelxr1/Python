def lin():
    print('-'*30)

def soma(*v):
    lin()
    s = 0
    for num in v:
        s += num
    print(f'Somando os valores {v} temos {s}')

#Programa Principal 1
soma(5, 2)
soma(2, 9, 4)
soma(2, 1, 5, 7,6 )
lin()

def contador(*n):
    print(n)

#Programa principal 2
contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)
lin()

def dobra(lst):
    p = 0
    while p < len(lst):
        lst[p] *= 2
        p += 1

valores = [7, 2, 5, 0, 4]
dobra(valores)
print(valores)
lin()
