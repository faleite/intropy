""" Faça uma programa que dada a entrada de uma lista ele faça o cálculo acumulativo da mesma:

- Exemplo de entrada: [1, 2, 3, 4]
- Exemplo de saída: [1, 3, 6, 10]
"""
print('Olá, vamos criar uma lista para fazer seu calcúlo acumulativo?')
print('Insira os numeros para somar, ou digite 0 para terminar\n')

entrada = []

indice = 0

while True:
    indice += 1
    numeros = int(input(f'Digite o {indice}º numero da lista: '))
    if numeros != 0:
        entrada.append(numeros)
    elif numeros == 0:
        break

acumulador = 0
saida = []

for numero in entrada:
    acumulador += numero
    saida.append(acumulador)

print()
print(f'Lista de entrada: {entrada}')
print(f'Lista de saída: {saida}')
