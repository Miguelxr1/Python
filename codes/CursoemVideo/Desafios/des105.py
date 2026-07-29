dados = {'total': 0, 'maior': 0, 'menor': 0, 'média': 0}

def notas(*num, sit=False):
    """Programa que recebe notas de alunos, conta quantas elas são, mostra a maior, a menor e a média delas, além da situação que é opcional.

    Args:
        sit (bool, optional): usada para mostrar a situação do aluno. Defaults to False.

    Returns:
        dict : dicionário contendo todos os dados
    """
    dados['total'] = len(num)
    
    maior = num[0]
    for n in num:
        if n > maior:
            maior = n
    dados['maior'] = maior
    
    menor = num[0]
    for n in num:
        if n < menor:
            menor = n
    dados['menor'] = menor
    
    s = 0
    for n in num:
        s += n
    dados['média'] = s/len(num)
    
    if sit:
        if dados['média'] <= 5:
            dados['situação'] = 'RUIM'    
        elif dados['média'] <= 7:
            dados['situação'] = 'RAZOÁVEL'
        else:
            dados['situação'] = 'BOA'
    return dados

resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)
