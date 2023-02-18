# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math
angulo = float(input('Digite um ângulo: '))
s = math.sin(math.radians(angulo))
c = math.cos(math.radians(angulo))
t = math.tan(math.radians(angulo))

print('Analisando o ângulo {} temos o valor de: \nsen : {:.2f}\ncosseno : {:.2f}\ntangente : {:.2f}'.format(angulo, s, c, t))