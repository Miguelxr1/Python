m = float(input('Digite a distamcia em metros:'))
km = m/1000
hm = m/100
dam = m/10
dm = m*10
cm = m*100
mm = m*1000

print('A medida de: {}m, corresponde a:'.format(m))
print('{}km'.format(km))
print('{}hm'.format(hm))
print('{}dam'.format(dam))
print('{}m'.format(m))
print('{}dm'.format(dm))
print('{}cm'.format(cm))
print('{}mm'.format(mm))
#Pode se usar tambem de operações dentro do format caso não seja nescessário o uso de uma var, ou seja,
#não for usar ela depois Ex. de cm: print('{}cm'.format(m*100))
