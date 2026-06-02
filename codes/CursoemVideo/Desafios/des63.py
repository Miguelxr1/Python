parts = ['0', '1']
f1 = 0
f2 = 1

num = int(input('Digite quantos números da sequencia de fibonacci você quer ver: '))

if num <= 0:
    print('Obrigado por usar nosso programa!')
elif num == 1:
    print('A sequencia de fibonacci até o termo que você digitou é:')
    print('0')
elif num == 2:
    print('A sequencia de fibonacci até o termo que você digitou é:')
    print('0 - 1')
else:
    for _ in range(num - 2):
        n_t = f1 + f2
        parts.append(str(n_t))
        f1 = f2
        f2 = n_t
    sequencia = " - ".join(parts)
    print('A sequencia de fibonacci até o termo que você digitou é:')
    print(sequencia)
