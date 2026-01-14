#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

m = float(input('Digite um número qualquer:'))
cm = m*100
mm = cm*10

print('O número que você digitou em metros é: {}m, em centímetros é: {}cm e em milímetros é:{}mm.'.format(m, cm, mm))
