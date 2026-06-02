n = 0
np = 0
s = 0

while np != 999:
    np = int(input('Digite quaisquer números (digite 999 quando quiser encerrar o programar): '))
    if np != 999:
        n = np
        s += np
print(f'A soma de todos os números que você digitou é: {s}')
