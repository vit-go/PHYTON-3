# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

nome = str(input('Nome do funcionário: '))  #RECEBE O VALOR DE NOME
salario = float(input('Salário do funcionário {}: R$'.format(nome)))  #RECEBE O VALOR DE SALARIO
# aumento = salario*0.15
novosalario = salario+(salario*0.15)  #CALCULA O NOVO SALARIO COM AUMENTO DE 15%

print('Salário atualizado do funcionário {}, com 15% de aumento: R${:.2f}'.format(nome, novosalario))  #MOSTRA O NOME DO FUNCIONÁRIO E SEU NOVO SALÁRIO

