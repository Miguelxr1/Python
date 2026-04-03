colocados = (
    "Palmeiras", "São Paulo", "Fluminence", "Flamengo", "Bahia",
    "Atlético Paranaense", "Coritiba", "Grêmio", "Vasco Da Gama", "Vitória",
    "Conrinthians", "Internacional", "Atlético Mineiro", "RB bragantino", "Chapecoense-SC",
    "Santos", "Botafogo", "Mirassol", "Remo", "Cruzeiro"
)
print("=-=-=-"*22)
print(colocados)
print(f"Os 5 primeiros colocados são: {colocados[:5]}")
print("=-=-=-"*22)
print(f"Os últimos 4 colocados são: {colocados[-4:]}")
print("=-=-=-"*22)
print(f"Os times em ordem alfabética são: {sorted(colocados)}")
print("=-=-=-"*22)
print(f'O time Chapecoense-SC está na posição {colocados.index("Chapecoense-SC")}')
