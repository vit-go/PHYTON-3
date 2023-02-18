# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ele.

a = input('Digite algo: ')

print('O tipo é:', type(a))
print('É um número? ', (a.isnumeric()))
print('É uma letra? ', (a.isalpha()))
print('É um alphanumerico? ', (a.isalnum()))
print('É um espaço? ', (a.isspace()))

# //TIPOS PRIMITIVOS
# int - inteiro
# float - ponto/virgula
# bool - True/False
# str - string/tudo "Ola" "10" "1.0" ""
