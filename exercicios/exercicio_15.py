""" Faça um programa que dada a entrada de uma lista o programa calcule
a combinatória de dois elementos e nos retorne as combinações em uma nova lista.

 - Exemplo de entrada: [1, 2, 3, 4]

 - Exemplo de saída: [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
"""

#  from itertools import combinations

entrada = [1, 2, 3, 4]
tamanho = len(entrada)
saida = []

#3 Resolução Lelzin
#  saida1 = list(combinations(entrada, 2))
#  print(saida1)

#1 Resolução Thiago Kim
#  for n in range(tamanho):
    #  lista = [[entrada[n], entrada[i]] for i in range(n + 1, tamanho)]
    #  saida.extend(lista)

#2 Resolução Thiago Kim
#  for n in range(tamanho):
    #  z = zip(entrada, entrada[n+1:])
    #  saida.extend(list(z))

#2.1 Resolução Thiago Kim
#  for n, num in enumerate(entrada):
    #  z = list(zip(entrada,entrada[n+1:]))
    #  saida.extend([list(itm) for itm in z])

#  saida.sort() # ou
#  saida = sorted(saida)

#1.1 Meu debug sobre a resolução 1
for n in range(tamanho):
    for i in range(n+1, tamanho):
        saida.append([entrada[n], entrada[i]])

print(saida)
