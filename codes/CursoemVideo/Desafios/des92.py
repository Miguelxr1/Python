from datetime import date

dados = dict()
year =  2018#date.today().year

dados['nome'] = str(input('Nome: '))
ano = int(input('Ano de nascimento: '))
dados['idade'] = year - ano
dados['ctps'] = int(input('Cateira de trabalho: (0 não tem): '))

if dados['ctps'] != 0:
    dados['contratacao'] = int(input('Ano de contratacao: '))
    dados['salario'] = float(input('Salário: R$'))
    dados['aposentadoria'] = (dados['contratacao'] - ano) + 35
    
    print('-='*30)
    print(f'    -Nome tem valor de {dados['nome']}')
    print(f'    -Idade tem valor de {dados['idade']}')
    print(f'    -CTPS tem valor de {dados['ctps']}')
    print(f'    -Contratação tem o valor de {dados['contratacao']}')
    print(f'    -Salário tem valor de R${dados['salario']:.2f}')
    print(f'    -Aposentadoria tem valor de {dados['aposentadoria']}')
else:
    print('-='*30)
    print(f'    -Nome tem valor de {dados['nome']}')
    print(f'    -Idade tem valor de {dados['idade']}')
    print(f'    -CTPS tem valor de {dados['ctps']}')
