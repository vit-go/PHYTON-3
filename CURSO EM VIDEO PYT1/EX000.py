# Faça um programa que leia o nome de uma pessoa e mostre uma mensagem.
# Crie um programa que leia dois números e mostre a soma entre eles.

nome = input ('Qual seu nome? ')
print (nome,', Bem vinda a calculadora 2.0')

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

r = (n1 + n2)

if  nome=='Lucilia' or nome=='lucilia':
      print('Parabéns Mamãe linda,', n1, '+', n2, ('='), r, ':)')
else:
      print('Parabéns', nome, ',', n1, '+', n2, ('='), r, ':)')