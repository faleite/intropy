""" Faça um programa, com uma função, que calcula a mediana de uma lista.
Funções embutidas que podem te ajudar:
- sorted(lista) -> ordena a lista
"""
# A Mediana (Md) é o valor de centro de um conjunto de dados.
#  Para calcular a mediana:
# - Devemos ordenar o conjunto de dados em ordem crescente;
# - Se o número de elementos for par, então a mediana é a média dos dois valores centrais.
#  Soma os dois valores centrais e divide o resultado por 2: (a + b)/2.
# - Se o número de elementos for ímpar, então a mediana é o valor central.

from math import ceil

def calcular_mediana(*args):
    """ Calcula a mediana de uma lista """
    lista = sorted(list(args))
    tamanho_lista = len(lista)
    impar_par = tamanho_lista % 2
    val_central = ceil(tamanho_lista / 2) - 1
    if impar_par == 0:
        mediana = (lista[val_central] + lista[val_central + 1]) / 2
        return f'Md = {mediana:.2f}'
    if impar_par == 1:
        mediana = lista[val_central]
        return f'Md = {mediana:.2f}'

print(calcular_mediana(6, 4, 7, 2))
print(calcular_mediana(6, 7, 2, 1, 8, 4, 9, 11, 10))
