pessoas = {'nome':'Gustavo', 'sexo':'M', 'idade':22}
print(f'{pessoas['nome']} tem {pessoas['idade']} anos')
print('-----'*20)

print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
print('-----'*20)

for k in pessoas.keys():
    print(k)
print('-----'*20)

for k, v in pessoas.items():
    print(f'{k} = {v}')
print('-----'*20)

# del pessoas['sexo'] apaga o local sexo
pessoas['nome'] = 'Miguel' # Modifica o nome
pessoas['Peso'] = 80 # adiciona o item peso

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla: '))
    brasil.append(estado.copy())
print('-----'*20)

for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')
    print()
print('-----'*20)

for e in brasil:
    for v in e.values():
        print({v}, end=' - ')
    print()
print('-----'*20)
