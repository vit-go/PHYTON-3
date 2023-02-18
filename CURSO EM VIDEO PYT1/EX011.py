# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit

tempC = float(input('Temperatura em graus Celsius: '))
tempF = tempC*(9/5)+32

print('{:.1f}°C em Fahrenheit é: {:.1f}°F'.format(tempC, tempF))