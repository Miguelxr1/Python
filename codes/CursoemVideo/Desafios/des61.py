from time import sleep

a1 = int(input('Digite o primeiro termo da P.A.: '))
r = int(input('digite a razão da P.A.: '))

print('-----' * 20)
sleep(1)

c1 = 1

c2 = 1
while c1 <= 10:
    print(f'{c1}° termo da P.A.: {a1 + (c1 - 1) * r}')
    c1 += 1
    sleep(0.5)

sleep(2)

print('-----' * 20)

print('Essa forma que acabou de ser escrita na tela agora é a forma mais matemática.')
sleep(2)
print('Essa que vai aparecer embaixo é a menos matemática.')

print('-----' * 20)

sleep(2)

while c2 <= 10:
    if c2 == 1:
        print(f'{c2}° termo da P.A.: {a1}')
        a2 = a1 + r
    else:
        print(f'{c2}° termo da P.A.: {a2}')
        a2 += r
    c2 += 1
    sleep(0.5)
    
print('-----' * 20)
