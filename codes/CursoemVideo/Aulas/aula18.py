teste = list()
teste.append('Miguel')
teste.append(14)
galera =list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)
