# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira

from math import trunc
n = float(input('Digite um número qualquer: '))
print('A parte inteira de {} é: {}'.format(n, trunc(n)))


# ou
'''n = float(input('Digite um número qualquer: '))
print('A parte inteira de {} é: {}'.format(n, int(n)))'''