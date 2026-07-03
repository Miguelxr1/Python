from time import sleep

def contagem(início, fim, passo):
    if passo == 0:
        passo = 1
    elif passo < 0:
        passo *= -1
    
    print('-='*20)
    print(f'Contagem de {início} até {fim} de {passo} em {passo}')
    
    if início < fim:
        while início <= fim:
            print(início, end=' ; ')
            início += passo
    elif início > fim:
        while início >= fim:
            print(início, end=' ; ')
            início -= passo
    
    print('FIM!')

contagem(1, 10, 1)
contagem(10, 0, 2)

print('-='*20)
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contagem(i, f, p)
