palavras = (
    'aprender', 'programar', 'linguagem',
    'python', 'curso', 'gratis',
    'estudar', 'praticar', 'trabalhar',
    'mercado', 'programador', 'futuro'
)
vogais = 'aeiouAEIOU'

for word in palavras:
    print(f'\nNa palavra {word} temos as vogais:', end=' ')
    for letter in word:
        if letter in vogais:
            print(letter, end=' ')
