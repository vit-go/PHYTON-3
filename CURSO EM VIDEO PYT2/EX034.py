# Escreva um programa que leia um número interio qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário; 2 para octal; 3 para hexadecimal.

from time import sleep

n = int(input('Digite um número inteiro: '))
usuario = int(input('\033[1;34mEscolha qual será a base de conversão\033[m\nDigite 1 para binário; 2 para octal; 3 para hexadecimal. '))

print('PROCESSANDO..')
sleep(1)

if usuario == 1:
    print(f' \nNúmero \033[1;32m{n}\033[m convertido para binário: \033[1;34m{bin(n)[2:]}\033[m')
elif usuario == 2:
    print(f' \nNúmero \033[1;32m{n}\033[m convertido para octal: \033[1;34m{oct(n)[2:]}\033[m')
elif usuario == 3:
    print(f' \nNúmero \033[1;32m{n}\033[m convertido para hexadecimal: \033[1;34m{hex(n)[2:]}\033[m')
else:
    print(' \n\033[1;31m---ERRO---\nESCOLHA INVÁLIDA!\033[m Tente novamente.')