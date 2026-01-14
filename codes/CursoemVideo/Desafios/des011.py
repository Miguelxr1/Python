#Faça um programa que leia a largura e a altura de uma parede em metros, calculea sua área e a quantidade de
#tinta necessária para pinta-la, sabendo que cada litro de tinta pinta uma área de 2m²

print('Vou te ajudar a calcular o quanto de tinta será necessário para pintar a sua parede. Mas preciso de algumas informações:')

h = float(input('Qual a largura da sua parede em metros?'))
b = float(input('Qual a altura da sua parede em metros?'))
a = b*h
t = a/2

print('A sua parede tem {}m² de área, e você precisara de {}L de tinta para pintar ela.'.format(a, t))
#para fazer o elevado ao quadrado de m², use Alt Gr + 2
