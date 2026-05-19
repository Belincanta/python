# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

dicionario = dict()
dicionario["Nome:"] = input("Digite o nome do aluno: ")
dicionario["Nota: "] = float(input("Digite a nota do aluno: "))
print("=-"*30)
print(f"O nome do aluno é {dicionario["Nome:"]}")
print(f"A nota do aluno é {dicionario['Nota: ']}")
if dicionario["Nota: "] >= 7:
    print("Aluno está aprovado!")
else:
    print("Aluno está reprovado!")