# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

print('CONVERSOR DE MEDIDAS')
metros = float(input('Valor em metros: '))

cm = metros * 100
mm = metros * 1000

if metros == 1:
    print('{} metro em centímetros é {}cm \n{} metro em milímetros é {}mm'.format(metros, int(cm), metros, int(mm)))
else:
    print('{} metros em centímetros é {}cm \n{} metros em milímetros é {}mm'.format(metros, int(cm), metros, int(mm)))
