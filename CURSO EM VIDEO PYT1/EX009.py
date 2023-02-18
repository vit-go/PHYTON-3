# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

valor = float(input('Preço original do produto: R$'))

des = (valor-(valor*(5/100)))

print('O valor do produto com desconto de 5% é R${:.2f}'.format(des))

