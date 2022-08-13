""" Faça um programa que peça 2 números inteiros e um número float. Calcule e mostre:
● O produto do dobro do primeiro com metade do segundo.
● A soma do triplo do primeiro com o terceiro.
● O terceiro elevado ao cubo. """

numero_1 = int(input('Digite um número inteiro: '))
numero_2 = int(input('Digite outro número inteiro: '))
numero_3 = float(input('Agora digite um número float: '))

questao_1 = (numero_1 * 2) + (numero_2 / 2)

questao_2 = (numero_1 * 3) + numero_3

questao_3 = numero_3 ** 3

print('\n'f'O produto do dobro do primeiro com metade do segundo. É igual a: {questao_1}\n')
print(f'A soma do triplo do primeiro com o terceiro. É igual a: {questao_2}\n')
print(f'O terceiro elevado ao cubo. É igual a: {questao_3}')
