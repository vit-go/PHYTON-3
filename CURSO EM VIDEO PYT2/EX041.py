# Crie um programa que faça o computador jogar jokenpô com você.

from random import choice
from time import sleep

opc = ['pedra', 'papel', 'tesoura']
pc = choice(opc)

print(f' \n\033[1;35m{"-="*8}JOKENPÔ{"=-"*8}\033[m\n')
usuario = input('\033[1mESCOLHA: PEDRA, PAPEL OU TESOURA?\033[1m ').lower().strip()

if usuario == pc:
    resultado = 'emp'
elif pc=='pedra':
    if usuario=='papel':
        resultado = 'ggu'
    else:
        resultado = 'ggpc'
elif pc=='papel':
    if usuario=='pedra':
        resultado = 'ggpc'
    else:
        resultado = 'ggu'
elif pc=='tesoura':
    if usuario=='papel':
        resultado = 'ggpc'
    else:
        resultado = 'ggu'
sleep(1.5)
if resultado == 'ggpc':
    print(f' \n\033[1;31mVOCÊ PERDEU. EU ESCOLHI {pc.upper()} HAHA\033[m\n\033[1mTENTE DE NOVO.\033[m')
elif resultado == 'ggu':
    print(f' \n\033[1;32mVOCÊ GANHOU, PARABÉNS. EU ESCOLHI {pc.upper()} :(\033[m\n\033[1mDúvido ganhar de novo.\033[m')
elif resultado == 'emp':
    print(f' \n\033[1;34mEMPATEE. NA PRÓXIMA EU GANHO HAHA\033[m')

print(f' \n\033[1;35m{"-="*19}\033[m')