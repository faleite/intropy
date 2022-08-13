# função

# def -> define, definir
# nome (
# argumento ou parâmetro
# ):
# return -> retorno ou retorne, devolver

# sum -> soma (função de somar)
# len -> tamanho (função que obtem o tamanho)

# default -> na falta de qualquer coisa
"""
definir nome (parametro 1, parametro 2):
    devolve alguma_coisa
"""

def nome(
    argumento_posicional,
    *pacote_de_argumentos
):
    print(
        argumento_posicional,
        pacote_de_argumentos
    )

def nome2(
    argumento_nomeado='n tem nada',
    **pacote_nomeado
):
    print(
        argumento_nomeado,
        pacote_nomeado
    )
