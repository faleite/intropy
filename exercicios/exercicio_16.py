""" Faça um programa, com uma função, que calcula a média de uma lista.
Funções embutidas que podem te ajudar:

- len(lista) -> calcula o tamanho da lista
- sum(lista) -> faz o somatório dos valores
"""

def calcula_media_lista(*lista):
    media = sum(lista) / len(lista)
    return media


#  print(calcula_media_lista(1, 2, 3, 4, 5))
