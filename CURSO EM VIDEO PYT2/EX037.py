# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# Até 9 anos: Mirim;
# Até 14 anos: Infantil;
# Até 19 anos: Junior;
# Até 20 anos: Sênior;
# Acima: Master.

from datetime import date

nasc = int(input('Digite o ano de nascimento do atleta: '))
idade = date.today().year-nasc

if idade <= 9:
    categoria = 'Mirim'
elif 9 < idade <= 14:
    categoria = 'Infantil'
elif 14 < idade <= 19:
    categoria = 'Junior'
elif idade == 20:
    categoria = 'Sênior'
elif idade > 20:
    categoria = 'Master'

print(f'O atleta tem {idade} anos')
print(f'Categoria do atleta: \033[1;7m{categoria.upper()}\033[m')