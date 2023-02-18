# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

m=0
nm=0
for i in range(0,7):
    nasc = int(input('Ano de nascimento: '))
    idade = date.today().year - nasc
    if idade >= 18:
        m += 1
    else:
        nm += 1
if m == 0:
    print('Nenhuma pessoa atingiu a maioridade.')
elif nm == 0:
    print('Todas pessoas atingiram a maioridade.')
else:
    print(f'{m} pessoas já atingiram a maioridade.')
    print(f'{nm} pessoas ainda não atingiram a maioridade.')