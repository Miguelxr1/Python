def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato')

n = input('Nome do jogador: ')
g = input('Número de Gols: ')
ficha(
    nome=n or '<desconhecido', 
    gols=int(g) if g else 0
      )
