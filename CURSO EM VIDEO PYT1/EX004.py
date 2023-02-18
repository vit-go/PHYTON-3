# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua media

aluno = input("Nome do aluno(a): ")
nota1 = float(input("Nota na primeira prova: "))
nota2 = float(input("Nota na segunda prova: "))

media = (nota1 + nota2)/2

if media >= 6:
    print("A media do aluno(a) {} é: {:.1f} \nALUNO APROVADO".format(aluno, media))
else:
    print("A media do aluno(a) {} é: {:.1f} \nALUNO REPROVADO".format(aluno, media))
