def aumentar(n, a):
    f = n + (n * (a / 100))
    return f

def diminuir(n, a):
    f = n - (n * (a / 100))
    return f


def dobro(n):
    return n * 2

def metade(n):
    return n / 2

def resumo(n, a, d):
    print('-----'*5)
    print('     RESUMO     ')
    print('-----'*5)
    print(f'Preço analisado: R${n:.2f}')
    print(f'Dobro do preço: RS{(n * 2):.2f}')
    print(f'Metade do preço: R${(n / 2):.2f}')
    print(f'{a}% de aumento: R${(n + (n * (a / 100))):.2f}')
    print(f'{d}% de redução: R${(n - (n * (d / 100))):.2f}')
    print('-----'*5)
