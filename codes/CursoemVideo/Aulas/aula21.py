def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela
    Args:
        i (int): início da contagem
        f (int): final da contagem
        p (int): passo da conatagem
    return: sem retorno
    """
    
    c = 1
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM!')

#help(contador)

def somar(a=0, b=0, c=0):
    """
    Faz a soma de três valores e mostra o resultado na tela
    Args:
        a (int): o primeiro valor
        b (int): o segundo valor
        c (int): o terceiro valor
    """
    s = a + b + c
    return s

r1 = somar(3, 2, 5)
r2 = somar(1, 7)
r3 = somar(4)
print(f'Meus resultados fora: {r1}; {r2}; {r3}')

def teste():
    #global n
    n = 3
    x = 8
    print(f'Na função o valor de n é {n}')
    print(f'Na função o valor de x é {x}')

n = 2
print(f'No programa principal n vale {n}')
teste()

#Parte prática da aula:

def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f 

n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')
#OU
f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial(3)
print(f'Os fatoriais foram {f1}, {f2} e {f3}')

def par(nm=0):
    if nm % 2 == 0:
        return True
    else:
        return False

lern = int(input('Digite um número: '))
if par(lern):
    print('É par')
else:
    print('Não é par')
