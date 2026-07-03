from time import sleep

def contagem(início, fim, passo):
    if passo == 0:
        passo = 1
    if passo < 0:
        passo *= -1
    
    print('-='*20)
    print(f'Contagem de {início} até {fim} de {passo} em {passo}')
    sleep(1)
    
    if início < fim:
        while início <= fim:
            print(início, end=' ; ', flush=True)
            início += passo
            sleep(0.5)
        print('FIM!')
    elif início > fim:
        while início >= fim:
            print(início, end=' ; ', flush=True)
            início -= passo
            sleep(0.5)
        print('FIM!')
        sleep(1)

contagem(1, 10, 1)
contagem(10, 0, 2)

print('-='*20)
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contagem(i, f, p)
