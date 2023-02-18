# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

city = input('Nome da cidade: ')
city2 = city.split()
print('{} começa com o nome Santo? {}'.format(city, 'Santo' in city2[0]))