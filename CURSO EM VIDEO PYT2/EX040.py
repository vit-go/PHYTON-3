# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# Á vista dinheiro/cheque: 10% de desconto;
# Á vista no cartão: 5% de desconto;
# Em até 2x no cartão: preço normal;
# 3x ou mais no cartão: 20% de juros.

from time import sleep

v = float(input('Preço original do produto: R$'))
pagm = input('Escolha a forma de pagamento: PIX ou CARTÃO: ').lower()
if pagm == 'cartão' or pagm == 'cartao':
    condpag = input(f'{"-="*5}Digite{"=-"*5}\n1 para Á VISTA\n2 para ATÉ 2X\n3 para 3X OU MAIS\n')
    if condpag == '1':
        desconto = 0.05
    elif condpag == '2':
        desconto = 0
    elif condpag == '3':
        juros = 0.2
else:
    condpag = 'pix'
    desconto = 0.1

print('\n\033[1mPROCESSANDO...\033[m')
sleep(1.5)

if condpag != '3':
    vfinald = v - (v * desconto)
    print(f'Valor a ser pago pelo produto: \033[1;32mR${vfinald:.2f}\033[m')
else:
    vfinalj = v + (v * juros)
    print(f'Valor a ser pago pelo produto, com 20% de juros: \033[1;32mR${vfinalj:.2f}\033[m')