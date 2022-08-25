""" Baseando-se nos exercícios passados, monte um dicionário com as seguintes chaves:
- lista, somatório, tamanho, maior valor e menor valor
  """

d = {'lista': [1, 2, 3]}

def valores():
    """ Função que retorna valores de um dicionario """
    somatorio = sum(d['lista'])
    tamanho = len(d['lista'])
    maior_valor = max(d['lista'])
    menor_valor = min(d['lista'])
    return f"""Valores da chave "lista":
somatorio = {somatorio}
tamanho = {tamanho}
maior_valor = {maior_valor}
menor_valor = {menor_valor}"""

print(valores())
