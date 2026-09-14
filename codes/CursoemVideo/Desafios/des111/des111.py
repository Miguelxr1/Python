from modulos import moeda

p = float(input('Digite o preço: R$'))
aumento = float(input('Digite o valor percentual de aumento: '))
redução = float(input('Digite o valor percentual de redução: '))
moeda.resumo(p, aumento, redução)
