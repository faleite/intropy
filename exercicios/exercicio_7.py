""" Faça um programa que receba uma string e responda se ela tem alguma vogal,
se sim, quais são? E também diga se ela é uma frase ou não. """

string = str(input('Digite uma string: ')).lower()

vogais = 'aeiou'

lista_vogais = list(vogais)

lista = list(string)

vogais_da_string = []

for i in lista:
    for x in lista_vogais:
        if i in x:
            vogais_da_string += i

if vogais_da_string == []:
    print('A string não possui vogais.')
else:
    print('A string possui as seguintes vogais:', vogais_da_string)

if ' ' in lista:
    print('E a string é uma frase')
else:
    print('E a string não é uma frase.')
