""" Faça um programa que: Dada uma lista [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] e um número inteiro,
imprima a tabuada desse número. """

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

n_int = int(input('Digite um numero inteiro: '))

for n in lista:
    print(f'{n:<2} X {n_int} = {n_int * n}')


# Resolução sem lista

#  n = 0

#  while n < 10:
    #  n += 1
    #  print(f'{n:<2} X {n_int} = {n_int * n}')
