# Dicionários
# São estruturas que agromeram outras estruturas
# É dividido entre chaves e valores
# É hashable -> não da para pegar por posição
# Os valores podem se qualquer coisa
# Similar a um JSON

#  dicionario = {
    #  'chave': 'valor'
#  }

dicionario = {
    'chave': ['valor1', 'valor2'],
    'chave2': ['valor3', 'valor4']
}


pessoa = {
    'nome': 'Fabricio',
    'idade': 37,
    'telefone': '38487352'
}

#  >>> pessoa
#  {'nome': 'Fabricio', 'idade': 37, 'telefone': '38487352'}
#  >>> pessoa['nome']
#  'Fabricio'
#  >>> pessoa['idade']
#  37
#  >>> pessoa['telefone']
#  '38487352'
#  >>>

pessoa = {
    'nome': 'Fabricio',
    'idade': 37,
    'telefones': {
        'residencial': 5466464,
        'celuar': 64657734,
        'comercial': 64658835
    }
}

#  >>> pessoa
#  {'nome': 'Fabricio', 'idade': 37, 'telefones': {'residencial': 5466464, 'celuar': 64657734, 'comercial': 64658835}}
#  >>> pessoa['telefones']
#  {'residencial': 5466464, 'celuar': 64657734, 'comercial': 64658835}
#  >>> pessoa['telefones'] ['residencial']
#  5466464
