# Conjuntos -> Set:
# São abstrações de conjuntos da matemática
# São valores fixos
# Sua estrutura de dados é no formato de arvore
# Não é possivel pegar certo valor por posição
# Pede conter tuplas, mas não pode conter listas
# Não pode conter coisas que mudam

# Métodos
# >>> x = {1,2,3}; y =  {3,4,5}
# x.union(y) -> cria um novo conjunto com a união de x com y -> {1,2,3,4,5}
# x.intersection(y) -> valor que esta em x e y: {3}
# x.difference(y) -> diferança de x em y -> {1,2}
# x.update(y) -> trazer y para dentro de x -> {1,2,3,4,5}
# x.discard(1) -> descartar elemento de x -> {2,3}
# x.pop() -> descarta qualquer valor de x -> {1,3}

A = {'Fabricio', 'Fabricio'}
lista = [1,1,1,1,1,1,2,2,2,2,2,4,54,5,54,354,36]
print(A)

#  >>> print(A)
#  >>> {'Fabricio'}

#  >>> lista
#  [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 4, 54, 5, 54, 354, 36]
#  >>> set(lista)
#  {1, 2, 354, 4, 5, 36, 54}
#  >>> list(set(lista))
#  [1, 2, 354, 4, 5, 36, 54]
#  >>> tuple(set(lista))
#  (1, 2, 354, 4, 5, 36, 54)
