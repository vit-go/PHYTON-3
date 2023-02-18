# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

ano = int(input('Verifique se um ano é BISSEXTO\nDigite um ano: '))

if ano%4 == 0 and ano%100 != 0 or ano%400 == 0:
    print(f'O ano de {ano} é BISSEXTO, com 366 dias')
else:
    print(f'O ano de {ano} NÃO é BISSEXTO, pois possuí 365 dias')