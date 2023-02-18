# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# Abaixo de 18.5: Abaixo do peso; Entre 18.5 e 25: Peso ideal; 25 até 30: Sobrepeso; 30 até 40: Obesidade; Acima de 40: Obesidade mórbida.

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso/(altura**2)

if imc < 18.5:
    status = 'abaixo do peso'
elif 18.5 <= imc < 25:
    status = 'peso ideal'
elif 25 <= imc < 30:
    status = 'sobrepeso'
elif 30 <= imc < 40:
    status = 'obesidade'
else:
    status = 'obesidade mórbida'

print(f'De acordo com os dados informados:\nSeu IMC é \033[1m{imc:.1f}\033[m e seu status é \033[1m{status.upper()}\033[m')