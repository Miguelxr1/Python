from random import randint

numeros = list()

def sorteia():
    print('Sorteando 5 valores para a lista: ')
    for c in range(0, 5):
        numeros.append(randint(0, 10))
        print(numeros[c], end=' ; ')
    print('PRONTO!')

def somaPar():
    s = 0
    print(f'Somando os valores pares de {numeros}, temos ', end='')
    for n in numeros:
        if n % 2== 0:
            s += n
    print(s)


sorteia()
somaPar()
