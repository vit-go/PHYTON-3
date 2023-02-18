# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor

numero = int(input('Digite um número'))

be = numero - 1
af = numero + 1

print('O antecessor de {} é {} \nO sucessor de {} é {}'.format(numero, be, numero, af))