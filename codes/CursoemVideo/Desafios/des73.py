colocados = (
    "Palmeiras",
    "São Paulo",
    "Fluminence",
    "Flamengo",
    "Bahia",
    "Atlético Paranaense",
    "Coritiba",
    "Grêmio",
    "Vasco Da Gama",
    "Vitória",
    "Conrinthians",
    "Internacional",
    "Atlético Mineiro",
    "RB bragantino",
    "Chapecoense-SC",
    "Santos",
    "Botafogo",
    "Mirassol",
    "Remo",
    "Cruzeiro"
)

print(f"Os 5 primeiros colocados são: {colocados[:5]}")
print("------" * 20)
print(f"Os últimos 4 colocados são: {colocados[16:]}")
print("-----" * 20)
print(f"Os times em ordem alfabética são: {sorted(colocados)}")
print("-----" * 20)
for c in range(0, len(colocados)):
    if colocados[c] == "Chapecoense-SC":
        print(f"O time Chapecoense-SC está na posição {c}")
