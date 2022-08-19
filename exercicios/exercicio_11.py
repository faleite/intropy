""" Faça um programa que itera em uma palavra e toda vez que uma vogal aparecer na sua string
print o seu nome entre as letras

string = bananas

b
eduardo
n
eduardo
n
...

"""

#1 forma extensa
# for letra in palavra:
#     if letra == 'a':
#         print('Eduardo')
#     elif letra == 'e':
#         print('Eduardo')
#     elif letra == 'i':
#         print('Eduardo')
#     elif letra == 'o':
#         print('Eduardo')
#     elif letra == 'u':
#         print('Eduardo')
#     else:
#         print(letra)

nome = 'Fabricio'

palavra = 'bananas'

vogais = 'aeiou'

#2 Minha resolução
for letra in palavra:
    if letra in vogais:
        letra = nome
    print(letra)

#3 Resolução do professor
#  for letra in palavra:
    #  if letra in vogais:
        #  print(nome)
    #  else:
        #  print(letra)
