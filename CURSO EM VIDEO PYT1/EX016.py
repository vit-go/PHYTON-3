# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

import random
aluno1 = str(input('Nome 1° aluno: '))
aluno2 = str(input('Nome 2° aluno: '))
aluno3 = str(input('Nome 3° aluno: '))
aluno4 = str(input('Nome 4° aluno: '))
lista = [aluno4, aluno3, aluno2, aluno1]

sorteado = random.choice(lista)
print('O aluno sorteado para apagar o quadro é: {}'.format(sorteado))

