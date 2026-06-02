m18 = 0 # pessoas com mais de 18 anos
m20 = 0 # mulheres com menos de 20 anos
h = 0 # homens

while True:
    while True:
        i = input('IDADE: ')
        if i.isdigit():
            age = int(i) # idade
            break
        else:
            print('Entrada inválida, digite somente números.')
    
    while True:
        s = str(input('SEXO [M/F]: ')).strip().upper()
        if s == 'M' or s == 'F':
            break
        else:
            print('Digite um sexo válido.')
    
    if age > 18:
        m18 += 1
    if age < 20 and s == 'F':
        m20 += 1
    if s == 'M':
        h += 1
    
    while True:
        c = input('Quer continuar? [S/N] ').strip().upper()
        if c == 'S' or c == 'N':
            break
        else:
            print('Digite uma opção válida.')
    
    if c == 'N':
        print('-' * 20)
        break
    
    print('-' * 20)

print(f'{m18} tem mais de 18 anos.')
print(f'{h} homens foram cadastrados.')
print(f'{m20} mulheres em menos de 20 anos.')
