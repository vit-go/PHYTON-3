# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de ate 200Km e R$0,45 para viagens mais longas.

distancia = int(input('Distância em Km da viagem: '))

if distancia <= 200:
    print(f'Valor da viagem: \033[1;30;42mR${distancia * 0.5}\033[m')
else:
    print(f'Valor da viagem: \033[1;30;42mR${distancia * 0.45:.2f}\033[m')