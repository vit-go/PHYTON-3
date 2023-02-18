# Faça um programa que leia três números e mostre qual é maior e qual é menor.

n1 = input('Primeiro número: ')
n2 = input('Segundo número: ')
n3 = input('Terceiro número: ')

if n1>n2>n3:
    print(f'O maior número é {n1}, e o menor é {n3}')
elif n1>n3>n2:
    print(f'O maior número é {n1}, e o menor é {n2}')
elif n3>n2>n1:
    print(f'O maior número é {n3}, e o menor é {n1}')
elif n3>n1>n2:
    print(f'O maior número é {n3}, e o menor é {n2}')
elif n2>n3>n1:
    print(f'O maior número é {n2}, e o menor é {n1}')
else:
    print(f'O maior número é {n2}, e o menor é {n3}')

'''ou'''
'''
primeiro = int(input('Digite o primeiro número:'))
segundo = int(input('Digite o segundo número:'))
terceiro = int(input('Digite o terceiro número:'))
numeros = [primeiro, segundo, terceiro]

print('O maior valor digitado foi {}'.format(max(numeros)))
print('O menor numero digitado foi {}'.format(min(numeros)))'''