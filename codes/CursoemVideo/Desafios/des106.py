import pydoc
import builtins
from colorama import Back, Fore, Style, init

init(autoreset=True)

def PyHELP():
    while True:
        print(Back.GREEN + '~' * 20)
        print(Back.GREEN + 'SISTEMA DE AJUDA PyHELP')
        print(Back.GREEN + '~' * 20)
        f = input('Função ou Biblioteca > ').strip()

        if f.lower() == 'sair':
            print(Fore.BLACK + Back.RED + 'Saindo do PyHELP...')
            break

        objeto = getattr(builtins, f, None)

        if objeto is None:
            try:
                objeto = __import__(f)
            except ImportError:
                print(Fore.RED + f'ERRO: "{f}" não foi encontrado!')
                continue

        texto = pydoc.render_doc(objeto, renderer=pydoc.plaintext)
        print(Back.WHITE + Fore.BLACK + texto)

PyHELP()
