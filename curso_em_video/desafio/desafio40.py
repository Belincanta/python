#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#– Média abaixo de 5.0: REPROVADO
#– Média entre 5.0 e 6.9: RECUPERAÇÃO
#– Média 7.0 ou superior: APROVADO

nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))
media = (nota1 + nota2) / 2
if media >= 7.0:
    print(f"Com as notas {nota1} e {nota2} o aluno(a) teve a média final de {media:.2f}!\nO aluno(a) está APROVADO(A)!")
elif media >= 5.0 and media <= 6.9:
    print(f"Com as notas {nota1} e {nota2} o aluno(a) teve a média final de {media:.2f}!\nO aluno(a) está em RECUPERAÇÃO!")
else:
    print(f"Com as notas {nota1} e {nota2} o aluno(a) teve a média final de {media:.2f}!\nO aluno(a) está REPROVADO(A)!")
