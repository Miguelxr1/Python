while True:
    n = int(input('Digite o número que deseja ver a tabuada [número negativo para sair do programa]: '))
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} X {c} = {n * c}')
    print('-----' * 20)
print('-----' * 20)
