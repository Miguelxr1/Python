from random import randint
from time import sleep

jogadores = dict()

print('Valores Sorteados: ')
for c in range(0, 4):
    jogadores[f'jogador {c+1}'] = randint(1, 6)
    sleep(1)
    print(f'    O jogador {c+1} tirou: {jogadores[f'jogador {c+1}']}')

jogadores = dict(sorted(jogadores.items(), key=lambda item: item[1], reverse=True))
c = 1

print('\nRanking dos jogadores: ')
for k, v in jogadores.items():
    sleep(1)
    print(f'    {c}° Lugar: {k} com {v}')
    c += 1
