# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# Média abaixo de 5.0: Reprovado Média entre 5.0 e 6.9: Recuperação Média 7.0 ou superior: Aprovado.

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1+n2)/2

if media < 5.0:
    print(f'Sua média é {media:.1f}, você está \033[1;31mREPROVADO\033[m.')
elif 5.0 <= media <= 6.9:
    print(f'Sua média é {media:.1f}, você está de \033[1;33mRECUPERAÇÃO\033[m.')
elif media >= 7.0:
    print(f'Sua média é {media:.1f}, você está \033[1;32mAPROVADO\033[m.')