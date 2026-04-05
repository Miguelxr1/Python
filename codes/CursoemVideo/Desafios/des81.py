c = 0
ns = []

while True:
    ns.append(int(input('Digite um número: ')))
    c += 1
    p = input('Você quer continuar? [S/N] ').upper().strip()
    if p == 'N':
        break
print()
ns.sort(reverse=True)

print(f'Foram digitados {len(ns)} na lista.')
print(f'A lista em ordem decrescente é: {ns}')
if 5 in ns:
    print('O valor 5 está na lista!')
else:
    print('O valor 5 não está na lista!')
