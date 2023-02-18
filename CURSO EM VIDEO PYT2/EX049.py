# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

frase = input('Digite uma frase: ').upper().strip().replace(' ','')
invertida = frase[::-1]
print(invertida)
if frase == invertida:
    print(f'{invertida}\nA frase é um Palíndromo')
else:
    print('Não é um Palíndromo')


