jogador = dict()
gols = list()
total = 0

jogador['nome'] = str(input('Nome do Jogador: '))
np = int(input(f'Quantas partidas {jogador['nome']} jogou? '))

for c in range(0, np):
    gols.append(int(input(f'Quantos gols na partida {c}? ')))
    total += gols[c]
jogador['gols'] = gols.copy()
jogador['total'] = total

print('-='*30)
print(jogador)
print('-='*30)

for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-='*30)

print(f'O jogador {jogador['nome']} jogou {np} partidas.')
for c in range(0, np):
    print(f'    => Na partida {c}, fez {gols[c]} gols.')
print(f'Foi um total de {jogador['total']} gols.')
