# Faça um programa que leia o ano de um nascimento de um jovem e informe, de acordo com sua idade:
# Se ela ainda vai se alistar ao serviço militar; Se é a hora de se alistar; Se ja passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

nasc = int(input('Em que ano você nasceu? ')) #Lê o ano de nascimento informado.
idade = date.today().year - nasc #Calcula a idade.

if idade == 18: #Se tiver 18 anos:
    print('De acordo com sua idade, você tem que se alistar IMEDIATAMENTE.')
elif idade < 18: #Se tiver menos de 18 anos:
    if 18-idade == 1: #Se tiver menos de 18 anos e faltar 1 ano:
        print('De acordo com sua idade, você ainda não completou a idade correta para o alistamento.\nFalta apenas 1 ano, será em {}'.format(date.today().year+1))
    else: #Se tiver menos de 18 anos e faltarem mais de 1 ano:
        print('De acordo com sua idade, você ainda não completou a idade correta para o alistamento.\nFaltam {} anos, será em {}.'.format(18-idade, date.today().year+(18-idade)))
elif idade > 18: #Se tiver mais de 18 anos:
    if idade-18 == 1: #Se tiver mais de 18 anos e passar 1 ano:
        print('De acordo com sua idade, você deveria ter se alistado em {}.\nSe passou 1 ano'.format(date.today().year-1))
    else: #Se tiver mais de 18 anos e passar mais de 1 ano:
        print('De acordo com sua idade, você deveria ter se alistado em {}.\nSe passaram {} anos'.format(date.today().year-(idade-18), idade-18))


