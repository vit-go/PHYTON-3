# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

numero = float(input('Digite um número: '))

dobro = numero*2
triplo = numero*3
raiz = numero**(1/2)

print('O dobro de {} é {} \nO triplo de {} é {} \nA raiz de {} é {}'.format(numero, dobro, numero, triplo, numero, raiz))
