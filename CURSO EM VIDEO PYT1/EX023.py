# Faça um programa que leia uma frase pelo teclado e mostre

frase = input('Digite uma frase: ').upper().strip()

""" Quantas vezes aparece a letra 'A' """
print('A letra A aparece {} vezes'.format(frase.count('A')))

""" Em que posição a letra 'A' aparece a primeira vez """
print('A primera vez que aparece a letra A é na posição {}'.format(frase.find('A')+1))

""" Em que posição ela aparecea ultima vez """
print('A ultima vez que aparece é na posição {}'.format(frase.rfind('A')+1))