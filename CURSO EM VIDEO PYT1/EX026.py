# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

velo = int(input('Velocidade do carro em Km/h: '))
lvelo = velo - 80
multa = lvelo * 7
if lvelo >= 1:
    print('\033[1;31mVocê foi multado.\033[m')
    print('Ultrapassou {}Km/h da velocidade permitida, sua multa é no valor de \033[1;31mR${:.2f}\033[m'.format(lvelo, multa))
else:
    print('..Velocidade permitida')