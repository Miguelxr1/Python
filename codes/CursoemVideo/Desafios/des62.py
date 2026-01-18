from time import sleep

a1 = int(input('Digite o primeiro termo da P.A.: '))
r = int(input('digite a razão da P.A.: '))

print('-----' * 20)
sleep(1)

c = 1

c = 1
while c <= 10:
    print(f'{c}° termo da P.A.: {a1 + (c - 1) * r}')
    c += 1
    sleep(0.5)
    

n = int(input('Deseja ver mais quantos termos? (digite 0 para sair) '))

while n != 0:
    cont = 0
    while cont < n:
        termo = a1 + (c - 1) * r
        print(f'{c}° termo da P.A.: {termo}')
        c += 1
        cont += 1
        sleep(0.5)
    n = int(input('Deseja ver mais quantos termos? (digite 0 para sair) '))
    
print('Obrigado por usar nosso programa!')
