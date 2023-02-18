# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

from math import hypot
co = float(input('Comprimento do cateto oposto do triângulo retângulo: '))
ca = float(input('Comprimento do cateto adjacente de um triângulo retângulo: '))
hipotenusa = hypot(co,ca)
print('A hipotenusa do triângulo retângulo de acordo com os comprimentos informado é: {:.2f}'.format(hipotenusa))
