def fatorial(num, show=False):
    """_Calcula o Fatorial de um número

    Args:
        num (_int_): número a ser calculado 
        show (_boll_): (opcional) Mostrar ou não mostrar a conta

    Returns:
        _int_: O valor do fatorial do número
    """
    global f
    f = 1
    for c in range(num, 0, -1):
        f *= c
        if show:
            if c != 1:
                print(f'{c} X ', end = '')
            else:
                print(f'{c} = ', end='')
    return f 

print('-----'*20)
print(fatorial(5, show=True))
help(fatorial)
