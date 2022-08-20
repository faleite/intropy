""" Faça um programa que dada a entrada de uma lista o programa calcule
a combinatória de dois elementos e nos retorne as combinações em uma nova lista.

 - Exemplo de entrada: [1, 2, 3, 4]

 - Exemplo de saída: [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
"""

# Essa foi a resolução que cheguei. É preciso melhorar.

entrada = [1, 2, 3, 4]

saida = []

lista = []

index = 0
index2 = 1

for n in entrada:
    lista.append(entrada[index])
    if index2 < len(entrada):
        lista.append(entrada[index2])
        saida.append(lista)
        index2 += 1
        lista = []

entrada.pop(0)

lista2 = []

index = 0
index2 = 1

for n in entrada:
    lista2.append(entrada[index])
    if index2 < len(entrada):
        lista2.append(entrada[index2])
        saida.append(lista2)
        lista2 = []
        index2 += 1

entrada.pop(0)

lista2 = []

index = 0
index2 = 1

for n in entrada:
    lista2.append(entrada[index])
    if index2 < len(entrada):
        lista2.append(entrada[index2])
        saida.append(lista2)
        lista2 = []
        index2 += 1

print(saida)
