def área(larg, comp):
    a = larg * comp
    print(f'A área desse terreno é {a}m²')

print('-'*30)
print('Controle de terrenos')
print('-'*30)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
área(l, c)
