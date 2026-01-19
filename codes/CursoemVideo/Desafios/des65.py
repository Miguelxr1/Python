n = 0
s = 0
c = 0
l = []
finish = ''

while finish != 'N':
    n = int(input('Digite um número qualquer: '))
    s += n
    c += 1
    l.append(n)
    finish = str(input('Quer escrever mais números? [S/N] ')).upper().strip()

m = s/c

print(f'A média artimética de todos os números que você escreveu é: {m}')
print(f'O meno número foi {min(l)} e o maior foi {max(l)}')
