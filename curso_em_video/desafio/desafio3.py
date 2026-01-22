# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostra a sua média.
n1 = int(input('Qual foi a nota 1: '))
n2 = int(input('Qual foi a nota 2: '))
m = (n1 + n2) / 2
print('As suas notas forma {} e {}, a média entre elas é {}'.format(n1, n2, m))