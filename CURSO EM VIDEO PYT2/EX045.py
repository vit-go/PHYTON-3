# Refaça o desafio mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

print('-TABUADA-')
n = int(input('Digite um número: '))

print('\033[1;35m=x='*3,f'TABUADA DO {n}','=x='*3,'\033[m')
for c in range(1,11):
    print(f'{n} x {c} = {c*n}')
print('\033[1;35m=x=\033[m'*11)