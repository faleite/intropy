""" Dada uma lista de entradas de usuário de números inteiros,
construa um dicionário com a lista padrão, a lista dos valores elevados ao quadrado
e a lista dos valores elevados ao cubo.
"""


lista = []
lista_ao_quadrado = []
lista_ao_cubo = []

qtd = int(input('Quantos numeros você quer por na lista? '))

for n in range(qtd):
    n += 1
    num = int(input(f'Digite o {n}º numero inteiro: '))
    lista.append((n))

for i in lista:
    elevado = i ** 2
    lista_ao_quadrado.append(elevado)

for i in lista:
    elevado = i ** 3
    lista_ao_cubo.append(elevado)

dic = {
    'lista_padrao': lista,
    'lista_elev_quadrado': lista_ao_quadrado,
    'lista_elev_cubo': lista_ao_cubo,
}

print(f"""
Lista padrão: {dic['lista_padrao']}
Lista elavado ao quadrado: {dic['lista_elev_quadrado']}
Lista elavado ao cubo: {dic['lista_elev_cubo']}
""")

# Outra forma para fins de estudo
dic_2 = {
    'lista_padrao': [1, 2, 3],
    'lista_elev_quadrado': [x**2 for x in [1, 2, 3]],
    'lista_elev_cubo': [x**3 for x in [1, 2, 3]],
}
