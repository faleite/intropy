"""
Dada uma lista de entradas de usuários de números inteiros, construa um dicionário com a lista
padrão, a lista dos valores elevados ao quadrado e a lista dos valores elevado ao cubo.
"""

#2b
def eleva_numero(lista_de_numeros, numero_elevado):
    lista_resposta = []
    for numero in lista_de_numeros:
        lista_resposta.append(numero ** numero_elevado)

    return lista_resposta

#1
lista_valores = [] # lista vazia

for valor in range(10): # range(10) -> repetir o for dez vezes
    lista_valores.append(
        int(input('Fala um numero aí: '))
    )

#2a
dicionario = {
    'lista padrão': lista_valores,
    'lista quadrada': eleva_numero(lista_valores, 2),
    'lista cúbica': eleva_numero(lista_valores, 3)
}

print(dicionario)
