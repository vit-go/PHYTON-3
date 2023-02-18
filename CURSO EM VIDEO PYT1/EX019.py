# Crie um programa que leia o nome completo de uma pessoa e mostre

ncompleto = str(input('Seu nome completo: ')).strip()

""" O nome com todas as letras maiúsculas """
print(ncompleto.upper())

""" O nome com todas minúsculas """
print(ncompleto.lower())

""" Quantas letras ao todo sem considerar espaços """
print('Seu nome tem {} letras'.format(len(ncompleto) - ncompleto.count(' ')))

""" Quantas letras tem o primeiro nome """
pn = ncompleto.split()[0]
print('Seu primeiro nome tem {} letras'.format(len(pn)))