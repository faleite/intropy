""" Faça um programa que leia 5 números e informe o maior número. """

n = 1
lista = []
while n < 6:
    numero = input(f'Digite o {n}º numero: ')
    n += 1
    lista += numero

print(f'\nO maior número é: {max(lista)}')
