from time import sleep

op = 0

print('Digite 2 números.')
sleep(0.5)
n1 = float(input('1°: '))
n2 = float(input('2°: '))
sleep(0.5)
print('O que quer fazer com eles?')
sleep(1)

while op != 5:
    print('[1] Somar')
    sleep(0.5)
    print('[2] Multiplicar')
    sleep(0.5)
    print('[3] Maior')
    sleep(0.5)
    print('[4] Novos números')
    sleep(0.5)
    print('[5] Sair do programa')
    sleep(0.5)
    op = int(input('Digite o número da opção: '))
    sleep(1)
    if op == 1:
        print(f'A soma dos números é: {n1 + n2}')
        sleep(2)
        print('=-=-=-' * 20)
    elif op == 2:
        print(f'A multiplicação de um número pelo outro resulta em: {n1 * n2}')
        sleep(2)
        print('=-=-=-' * 20)
    elif op == 3:
        if n1 > n2:
            print(f'O maior número é: {n1}')
            sleep(2)
            print('=-=-=-' * 20)
        elif n1 == n2:
            print('Os dois número são iguais.')
            sleep(2)
            print('=-=-=-' * 20)
        else:
            print(f'O maior número é: {n2}')
            sleep(2)
            print('=-=-=-' * 20)
    elif op == 4:
        print('=-=-=-' * 20)
        print('Digite 2 números.')
        sleep(0.5)
        n1 = float(input('1°: '))
        n2 = float(input('2°: '))
        sleep(0.5)
        print('O que quer fazer com eles?')
        sleep(1)
    elif op == 5:
        print('Obrigado por usar o programa!')
        sleep(1)
    else:
        print('Digito inválido! Reiniciando o programa...')
        sleep(2)
        print('=-=-=-' * 20)
        print('Digite 2 números.')
        sleep(0.5)
        n1 = float(input('1°: '))
        n2 = float(input('2°: '))
        print('O que quer fazer com eles?')
        sleep(1)
