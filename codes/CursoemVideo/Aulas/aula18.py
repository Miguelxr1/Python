teste = list()
teste.append('Miguel')
teste.append(14)
galera1 =list()
galera1.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera1.append(teste[:])
print(galera1)

galera2 = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera2)
#Se eu mandar somente [0], ele printará a primeira lista, mas se eu mandar [0][0], ele printará o primeiro elemento da primeira lista. Veja o exemplo:
print(galera2[0]) # Printa a primeira lista dentro da lista
print(galera2[0][0]) # Printa o primeiro item da primeira lista dentro da lista
for p in galera2:
    print(p)
    

galera3 = list()
dados = list()

for c in range(0, 3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    galera3.append(dados[:])
    dados.clear()
print(galera3)
