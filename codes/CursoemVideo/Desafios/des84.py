pessoas = list()
dados = list()
c = 0

while True:
    c += 1
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    p = input('Deseja continuar? [S/N] ').upper().strip()
    if p == 'N':
        break

maior_peso = pessoas[0][1]
maior_nome = pessoas[0][0]   
menor_peso = pessoas[0][1]
menor_nome = pessoas[0][0]

for pessoa in pessoas:
    nome = pessoa[0] 
    peso = pessoa[1] 
    if peso > maior_peso:
        maior_peso = peso
        maior_nome = nome
    if peso < menor_peso:
        menor_peso = peso
        menor_nome = nome

print(f'Foram cadastradas {c} pessoas.')
print(f'O maior peso foi de {maior_peso}Kg. Peso de {maior_nome}')
print(f'O menor peso foi de {menor_peso}Kg. Peso de {menor_nome}')
