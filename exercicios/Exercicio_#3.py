""" Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados
da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados
e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
"""

# Método "ceil()" aredonda numero para cima

from math import ceil

area = float(input('Qual é o tamanho da área a ser pintada? '))

cobertura = area / 3

quantidade_latas = 0

if cobertura <= 18:
    quantidade_latas += 1
    print(f'É preciso comprar {quantidade_latas} lata de tinta')
else:
    quantidade_latas_sem_sobra = cobertura / 18
    resto = cobertura % 18
    if resto > 0:
        resto = 1
    quantidade_latas = int(quantidade_latas_sem_sobra) + ceil(resto)
    print(f'É preciso comprar {quantidade_latas} latas de tinta')
print(f'Preço total a pagar: R$ {quantidade_latas * 80:.2f}')
