"""
Faça um programa que receba uma string, com um número de ponto flutuante,
e imprima qual a parte dele que não é inteira

EX:

n = ‘3.14’

resposta: 14
"""

n = '10.55'

#  ('10', '.', '55')
lista = n.partition('.')

# ['10', '55']
lista2 = n.split('.')

print(lista2[-1])

print(lista[-1])
