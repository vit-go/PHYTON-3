# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pinta-la, sabendo que cada litro de tinta pinta uma área de 2m².

alt = float(input('Informe a ALTURA da parede em metros? '))
larg = float(input('Informe a LARGURA da parede em metros? '))

area = alt*larg
ltinta = area/2

print('A parede com área de {:.2f}m² necessita de {:.3f} litros de tinta para pinta-la'.format(area, ltinta))