""" Faça um programa, com uma função, que calcule a dispersão de uma lista

Funções embutidas que podem te ajudar:

- min(lista) -> retorna o menor valor
- max(lista) -> retorna o maior valor
"""

def dispersao_amplitude(*lista):
    """ Calcula a dispersão (amplitude) de uma lista """
    lista = list(lista)
    amplitude = max(lista) - min(lista)
    return amplitude

print(dispersao_amplitude(1, 2, 3, 4))
print(dispersao_amplitude(2.1, 2.0, 2.2, 2.9, 2.4))
