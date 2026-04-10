c = 0

expression_str = input('Digite a expressão: ')
expression = list(expression_str)

for v in expression:
    if v == '(':
        c += 1
    elif v == ')':
        c -= 1
    if c < 0:
        break
if c == 0:
    print('Sua expressão está correta e é válida!')
else:
    print('Sua expressão está incorreta e não é válida!')
