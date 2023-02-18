# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.
"""
n = int(input('Digite um número de 0 a 9999: '))
len(n)

if len(n) == 4:
    print('unidade:{}'.format(n[3]))
    print('dezena:{}'.format(n[2]))
    print('centena:{}'.format(n[1]))
    print('milhar:{}'.format(n[0]))
if len(n) == 3:
    print('unidade:{}'.format(n[2]))
    print('dezena:{}'.format(n[1]))
    print('centena:{}'.format(n[0]))
if len(n) == 2:
    print('unidade:{}'.format(n[1]))
    print('centena:{}'.format(n[0]))
if len(n) == 1:
    print('unidade:{}'.format(n[0]))"""
# OU
num = int(input('Informe um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Unidade: {}'.format(u))
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')