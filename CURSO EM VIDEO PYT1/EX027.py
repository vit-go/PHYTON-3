# Crie um programa que leia um número inteiro e mostre na tela se ele é par ou impar.
import math

print('Verifique se um número é PAR ou IMPAR.')
numero = int(input('Digite um número inteiro: '))

if numero%2 == 0:
    print(f'{numero} é um número PAR')
else:
    print(f'{numero} é um número IMPAR')
