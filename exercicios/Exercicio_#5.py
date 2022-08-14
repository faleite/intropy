""" Faça um programa para a leitura de duas notas parciais de um aluno.
O programa deve calcular a média alcançada por aluno e apresentar:
1. A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
2. A mensagem "Reprovado", se a média for menor do que sete;
3. A mensagem "Aprovado com Distinção", se a média for igual a dez. """

nota_1 = float(input('Digite a primeira nota: '))
nota_2 = float(input('Digite a segunda nota: '))

media = (nota_1 +  nota_2) / 2

if media == 10:
    print('\n'f'Sua média é {media} -> "Aprovado com Distinção"')
elif 7 <= media < 10:
    print('\n'f'Sua média é {media} -> "Aprovado"')
else:
    print('\n'f'Sua média é {media} -> "Reprovado"')
