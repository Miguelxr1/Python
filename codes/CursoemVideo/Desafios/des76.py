listagem = (
    ('Lápis', 1.75),
    ('Borracha', 2.00),
    ('caderno', 15.00),
    ('Estojo', 25.00,),
    ('Transferidor', 4.20),
    ('Compasso', 9.99),
    ('Mochila', 120.32),
    ('Canetas', 22.30),
    ('Livro', 34.90),
)

print("=-=-=-" * 7)
print("          LISTAGEM DE PREÇOS          ")
print("=-=-=-" * 7)

for name, price in listagem:
    print(f"{name:.<30}R${price:>8.2f}")
print("=-=-=-" * 7) 
