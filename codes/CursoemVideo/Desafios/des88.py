from random import randint
from time import sleep

count = 0
jogos = list()
ns = list()

while True:
    p = int(input('Quantos jogos serão gerados? '))
    for c in range(0, p):
        for i in range(0, 6):
            n = randint(1, 60)
            ns.append(n)
        jogos.append(ns[:])
        ns.clear()
    break

print(f'----------< SORTEANDO {p} JOGOS >----------')
sleep(0.5)

while True:
    if count != p:
        print(f'Jogo {count + 1}: {jogos[(count - 1)]}')
    else:
        break
    sleep(0.5)
    count += 1
print('----------< BOA SORTE >----------')
