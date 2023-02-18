# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

valorc = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite seu salário: R$'))
anos = int(input('Em quantos anos deseja pagar? '))

meses = anos*12
prest = valorc/meses
calp = salario * 0.3

if prest <= calp:
    print(f'Empréstimo bancário \033[1;32mAPROVADO\033[m\nPrestação mensal no valor de R${prest:.2f}, durante {anos} anos ou {meses} meses.')
else:
    print(f'Empréstimo bancário \033[1;31mNEGADO\033[m\nInfelizmente, a prestação mensal(R${prest:.2f}) excedeu 30% do seu salário(R${calp:.2f}).')

print('AGRADECEMOS A PREFERÊNCIA.')