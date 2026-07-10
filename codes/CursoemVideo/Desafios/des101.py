def voto(ano):
    global idade
    global v
    idade = 2018 - ano
    v = ''
    if idade < 16:
        v = 'voto NEGADO'
    elif idade == 16 or idade == 17 or idade >= 70:
        v = 'voto OPCIONAL'
    elif idade >= 18:
        v = 'voto OBRIGATÓRIO'

nascimento = int(input('Em que ano você nasceu? '))
voto(nascimento)
print(f'Com {idade} anos: {v}')
