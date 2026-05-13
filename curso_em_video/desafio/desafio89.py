# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

boletim = []
while True:
    aluno = input("Digite o nome do aluno: ")
    nota1 = float(input("Digite a 1ª nota: "))
    nota2 = float(input("Digite a 2ª nota: "))
    media_notas = (nota1+nota2) / 2
    boletim.append([aluno, [nota1, nota2], media_notas])
    opcao = input("Quer continuar? [S/N]: ").strip().upper()[0]
    if opcao == "N":
        break     
print("-="*30)   
print(f"{"No.":<4}{"NOME":<10}{"MÉDIA":>8}")
print(f"-="*30)
for i, a in enumerate(boletim):
    print(f"{i:<4}{a[0]:<10}{a[2]:>8.1f}")
print("-="*30) 
while True:
    base_notas = int(input("Quer conferir as notas de qual aluno? [999 para terminar] "))
    if base_notas == 999:
        print("FINALIZANDO...")
        break
    if base_notas <= len(boletim) - 1:
        print(f"As notas do aluno {boletim[base_notas][0]} são {boletim[base_notas][1]}")
print("<<<<< VOLTE SEMPRE >>>>>")





