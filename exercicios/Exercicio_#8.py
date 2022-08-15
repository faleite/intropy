""" Faça um programa que receba uma data de nascimento (15/07/87) e imprima:
‘Você nasceu em <dia> de <mês> de <ano>’ """

# Minha Resolução
data = input('Digite a sua data de nascimento: ')

data2 = data.split('/')

print(f"\n‘Você nasceu em {data2[0]} de {data2[1]} de {data2[2]}’")

# Resolução do professor
dia, mes, ano = data.split('/')

print(f"\n‘Você nasceu em {dia} de {mes} de {ano}’")
