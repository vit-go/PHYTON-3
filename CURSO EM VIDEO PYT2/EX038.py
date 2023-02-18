# Refaça o desafio dos triângulos, acescentando o recurso de mostrar que tipo de triângulo será formado:
# Equilátero: todos os lados iguais; Isósceles: dois lados iguais; Escaleno: todos os lados diferentes.

a = float(input('Primeira reta: '))
b = float(input('Segunda reta: '))
c = float(input('Terceira reta: '))

conta = a + b > c and a + c > b and b + c > a

if conta is True:
    print('As medidas dadas podem formar um triângulo.')
    if a==b==c:
        tipo = 'equilátero'
    elif a==b or b==c or a==c:
        tipo = 'isósceles'
    elif a!=b!=c:
        tipo = 'escaleno'
    print(f'{"-"*5}Será formado um triângulo {tipo.upper()}{"-"*5}')
else:
    print('As medidas dadas \033[1;31mNÂO\033[m podem formar um triângulo.')

