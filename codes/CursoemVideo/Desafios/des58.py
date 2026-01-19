from random import randint
from time import sleep

c = 0
nc = randint(1, 10)
nj = 1

while nj != nc:
    if c == 0:
        print('Vou pensar em um número de 1 a 10!')
    nj = int(input('Tente adivinhar qual número eu pensei: '))
    c += 1
    if nj != nc:
        if nj > nc:
            print('Menos... tente de novo!')
            sleep(0.5)
        elif nj < nc:
            print('Mais... tente de novo!')
            sleep(0.5)
sleep(0.5)
if c == 1:
    print(f'Parabéns, você acertou o número de primeira!')
else:
    print(f'Parabéns, você acertou o número em {c} tentativas!')
