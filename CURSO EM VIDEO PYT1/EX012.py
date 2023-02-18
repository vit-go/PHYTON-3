# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por
# Km rodado.

km = float(input('Quantos Km foi percorrido pelo carro? '))
dias = int(input('Quantos dias o carro foi alugado? '))

preco = dias*60 + 0.15*km
print('O valor total a pagar é R${:.2f}'.format(preco))