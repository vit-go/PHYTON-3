# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

a = float(input('Primeira reta: '))
b = float(input('Segunda reta: '))
c = float(input('Terceira reta: '))

conta = a + b > c and a + c > b and b + c > a

if conta is True:
    print('As medidas dadas podem formar um triângulo.')
else:
    print('As medidas dadas \033[1;31mNÂO\033[m podem formar um triângulo.')