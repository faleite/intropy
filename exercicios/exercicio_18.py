""" Faça um programa, com uma função que dado uma lista e uma posição da mesma
faça o quartil dessa posição.

p_index = int(p * len(lista))
"""

def primerio_quartil(*args):
    """ Calcula a mediana de uma lista """
    lista = sorted(list(args))
    posicao = int(0.25 * len(lista))
    quartil = lista[posicao]
    return f'Primeiro Quartil -> Q1 = {quartil}'

print(primerio_quartil(41, 7, 39, 15, 40, 36))
print(primerio_quartil(6, 47, 49, 15, 42, 41, 7, 39, 43, 40, 36))
