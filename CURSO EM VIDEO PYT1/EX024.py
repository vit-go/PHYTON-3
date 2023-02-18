# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente.

nome = input('Nome completo: ').strip()
nomelista = nome.split()

# Primeiro nome #
print('Primeiro nome: {}'.format(nomelista[0]))

# Ultimo nome #
print(f'Último nome: {nomelista[len(nomelista)-1]}')
