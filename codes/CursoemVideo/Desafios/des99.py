from time import sleep

def maior(*n):
    print('-='*20)
    print('Analisando os valores informados...')
    for c in n:
        print(c, end=' ; ')
        sleep(0.5)
    print(f'Foram informados {len(n)} valores ao todo.')
    sleep(0.3)
    print(f'O maior valor informado foi {max(n)}')

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
