from random import randint

c = 0

print('=-=-=-' * 10)
print('Vamos jogar Par ou Ímpar!')
print('=-=-=-' * 10)

while True:
    print()
    
    try:
        nj = int(input('Digite um valor (inteiro): '))
    except ValueError:
        print('Entrada inválida. Digite um número inteiro.')
        continue
    
    j = input('Par ou Ímpar? [P/I] ').strip().upper()
    if j not in ('P', 'I'):
        print('Opção inválida. Digite "P" para Par ou "I" para Ímpar.')
        continue
    
    nc = randint(0, 10)
    total = nj + nc
    is_par = (total % 2 == 0)
    
    print(f'Você jogou {nj} e o computador {nc}. Total = {total} -> {"Par" if is_par else "Ímpar"}.')
    
    if (is_par and j == 'P') or (not is_par and j == 'I'):
        c += 1
        print('Você venceu!!! Vamos jogar novamente...')
    else:
        print('Você perdeu!!!')
        break
print()
print(f'GAME OVER! Você venceu {c} vez(es).')
