""" Faça um programa que pergunte o preço de três produtos e informe qual produto você deve
comprar, sabendo que a decisão é sempre pelo mais barato. """

produto_1 = float(input('Digite o valor do primeiro produto: '))
produto_2 = float(input('Digite o valor do segundo produto: '))
produto_3 = float(input('Digite o valor do terceiro produto: '))

print()

# Resolução 2
produtos = (produto_1, produto_2, produto_3)

mais_barato = min(produtos)

if mais_barato == produto_1:
    print('Compre o produto #1')
elif mais_barato == produto_2:
    print('Compre o produto #2')
else:
    print('Compre o produto #3')

print()

# Resolução 1
if produto_1 < produto_2 and produto_2 < produto_3:
    print('Compre o produto #1')
elif produto_2 < produto_1 and produto_1 < produto_3:
    print('Compre o produto #2')
else:
    print('Compre o produto #3')
