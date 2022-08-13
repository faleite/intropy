# Dicionários
# São estruturas que agromeram outras estruturas
# É dividido entre chaves e valores
# chave -> recomenda ser sempre um string (mas pode ser numero)
# valor -> pode ser qualquer coisa
# chaves não são mutáveis, mas os valores são sempre mutáveis
# É hashable -> não da para pegar por posição
# Os valores podem se qualquer coisa
# Similar a um JSON



#  dicionario = {
    #  'chave': 'valor'
#

# Métodos
# >>> x = {'Maria': 50, 'Juana': 25}
# >>> x['Maria'] acessa pela chave, retorna valor -> 50
# >>> x['Maria'] = 10 atribui um novo valor a chave
# >>> x.keys() -> pega todas as chaves -> retorna uma lista só com as chaves
# >>> x.values() -> pega todas as valores -> retorna uma lista só com as valores
# >>> x.setdefault('Carlos') -> define chave 'Carlos' com o valor defalt -> None
# >>> x.popitem() -> retira um item qualquer do dicionario, sem saber qual é
# Consigo eliminar item por nome


nome_idade = {
    'Maria': 50,
    'Joana': 25
}

#  >>> nome_idade['Maria']
#  50
#  >>> nome_idade['Maria'] = 4
#  >>> nome_idade
#  {'Maria': 4, 'Joana': 25}
#  >>> nome_idade['Joana'] = 20
#  >>> nome_idade
#  {'Maria': 4, 'Joana': 20}

#  >>> nome_idade.keys()
#  dict_keys(['Maria', 'Joana'])
#  >>> nome_idade.values()
#  dict_values([50, 25])

nome = input('nome: ')
cpf = int(input('cpf: '))
telefone = int(input('telefone: '))

pessoa = {
    'nome': nome,
    'cpf': cpf,
    'telefone': telefone
}

def imprime_relatorio(pessoa):
    return f"""
    Relátorio parcial

    {pessoa['nome']},
    portador do cpf {pessoa['cpf']},
    que usa o número {pessoa['telefone']}

    está oficialmente de férias

    Ass. Direção
    """
print(imprime_relatorio(pessoa))
