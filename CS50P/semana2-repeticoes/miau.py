i = 0
while i < 3:
    print('miau')
    i += 1

# o loop for itera usando um tipo iterável
for _ in range(3):
    print('MIAAUUUU')

# evita-se uma saída do tipo 'miaumiaumiau'
print('miauzimm\n' * 3, end = '')
