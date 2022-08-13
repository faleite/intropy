# Tuplas

# Lista são imutaveis
# Tem apenas dois metodos: .count(), .index()
# count -> contagem
# index -> indice, onde esta cada valor

minha_tupla = (
    'Fabricio', 27, '8584858', 'R cosmica', 7
)

# desenpacotamento
# * -> agrupa coisas
# *coisa_que_nao_quero, esta agrupando as coisas que não foi usada na tupla
# é possivel criar apenas um empacotamento

nome, idade, *coisa_que_nao_quero = minha_tupla

nome, idade = idade, nome

# ambos são tuplas:
# nome, idade = (idade, nome)
# nome, idade = idade, nome

def minha_fuc():
    return 1, 2, 3 # retorna -> (1, 2, 3) uma tupla

