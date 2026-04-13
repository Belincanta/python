# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

total = 0
mais18 = 0
mulher20 = 0
homem = 0

while True:
    print("="*20)
    print("CADASTRO DE PESSOAS")
    print("="*20)
    idade = int(input("Qual a idade: "))
    sexo = " "
    while sexo not in "MF":
        sexo = input("Qual é o sexo [M/F]: ").strip().upper()[0]
    total += 1
    if sexo == "M":
        homem += 1
    if idade < 20 and sexo == "F":
        mulher20 +=1
    if idade > 18:
        mais18 += 1
    opcao = " "
    while opcao not in "SN":
        opcao = input("Cadastrar outra pessoa? [S/N]: ").strip().upper()[0]
    if opcao == "N":
        break
print("="*20)
print("CADASTRO ENCERRADO")
print(f"""Ao todo foram cadastradas {total} pessoas.
Destas, {homem} são homens.
Ainda, {mulher20} são mulheres que possuem idade inferior à 20 anos.
E ao todo foram cadastradas {mais18} pessoas que possuem idade superior à 18 anos.""")