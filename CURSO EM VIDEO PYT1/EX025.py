# Escreva um programa que façao computador "pensar"em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu

from random import choice
from time import sleep

cores = {'vermelho': '\033[1;31m',
         'verde': '\033[1;32m',
         'azul': '\033[1;34m',
         'limpa': '\033[m'}
'''ESCOLHER UM NÚMERO INTEIRO DE 0 A 5'''
numeros = [1, 2, 3, 4, 5]
n = choice(numeros)

print(('\033[1;34m-=-'*18),'\nTENTE ADIVNHAR O NÚMERO QUE ESTOU PENSANDO DE 0 a 5\n',('-=-'*18),'\033[m')
test = int(input('Qual número eu pensei? '))
if test > 5:
    sleep(1)
    test = int(input('{}---ERRO---{}\nTENTE NOVAMENTE, UM NÚMERO DE 0 A 5: '.format(cores['vermelho'], cores['limpa'])))
print('\nPROCESSANDO...')
print('')
sleep(1.5)

print('{}-Parabéns você acertou-{}'.format(cores['verde'],cores['limpa'])if test == n else '{}VOCÊ ERROU!{} o número pensado foi {}{}{} e não {}'.format(cores['vermelho'],cores['limpa'],cores['azul'],n,cores['limpa'],test))
