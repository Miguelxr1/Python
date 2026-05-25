temp = list()
princ = list()
maior = menor = 0

while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    
    princ.append(temp[:])
    resp = str(input('Quer continuar? [S/N] '))
    temp.clear()
    if resp in 'Nn':
        break
print('-----'*20)
print(f'Você cadastrou {len(princ)} pessoas.')
print(f'O maior peso foi de {maior}Kg', end=' ')
for p in princ:
    if p[1] == maior:
        print(p[0], end=' ')
print(f'\nO menor peso foi de {menor}Kg', end=' ')
for p in princ:
    if p[1] == menor:
        print(p[0], end=' ')
