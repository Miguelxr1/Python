from colorama import Style, Fore

def leiaInt(conferir):
    while True:
        num = input(conferir)
        if num.isdigit():
            break
        else: 
            print(Fore.RED + 'ERRO! Digite um número inteiro válido.')
            print(Style.RESET_ALL)
    return int(num)

print('-----'*20)
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
print('-----'*20)
