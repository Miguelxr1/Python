galera = list()
pessoa = dict()
s = 0

while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Digite somente M ou F.')
    
    pessoa['idade'] = int(input('Idade: '))
    s += pessoa['idade']
    galera.append(pessoa.copy())
    
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('Digite somente S ou N.')
    
    if resp == 'N':
        break
print('-='*30)

print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
m = s / len(galera)

print(f'B) A média de idades é {m:5.2f} anos.')
print(f'C) As melheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(p['nome'], end='')
print()

print(f'D) Lista de pessoas que estão acima da média:  ')
for p in galera:
    if p['idade'] >= m:
        for k, v in p.items():
            print(f'{k} = {v}: ', end='')
        print()

print('<<ENCERADO>>')
