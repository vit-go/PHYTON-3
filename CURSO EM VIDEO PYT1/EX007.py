# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar
## Considere US$1.00=R$3,27

reais = float(input('Quantos reais você tem na carteira? R$'))

dol = reais/3.27

print('Com R${} você consegue comprar US${:.2f}'.format(reais, dol))