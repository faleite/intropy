# função

# def -> define, definir
# nome (
# argumento ou parâmetro
# ):
# return -> retorno ou retorne, devolver

# sum -> soma (função de somar)
# len -> tamanho (função que obtem o tamanho)
"""
definir nome (parametro 1, parametro 2):
    devolve alguma_coisa
"""

def soma(numero_1, numero_2):
    return numero_1 + numero_2


def media(lista_de_numeros):
    return sum(lista_de_numeros) / len(lista_de_numeros)

def imprime_relatorio(nome, cpf, telefone):
    return f"""
    Relátorio parcial

    {nome}, portador do cpf {cpf}, que usa o número {telefone}

    está oficialmente de férias

    Ass. Direção
    """

print(
    imprime_relatorio(
        'Fabricio',
        12344556,
        9867473
    )
)

#  print(
    #  imprime_relatorio(
        #  nome='Fabricio',
        #  cpf=12344556,
        #  telefone=9867473
    #  )
#  )
