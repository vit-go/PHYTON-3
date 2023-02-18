# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1.250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Salário do funcionário: R$'))

if salario > 1250:
    novo = salario + salario * 0.10
    print(f'Aumento de R${salario*0.10:.2f}, novo salário: R${novo:.2f}')
else:
    novo = salario + salario * 0.15
    print(f'Aumento de R${salario*0.15:.2f}, novo salário: R${novo:.2f}')