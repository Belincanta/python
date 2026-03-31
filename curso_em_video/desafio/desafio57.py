# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.
sexo = input("Digite o seu sexo [M/F]: ").upper().strip()
while sexo not in "MF": # enquando o usuário não digitar a opção certa, vai cair na operação abaixo.
    sexo = input("Dados inválidos, favor digitar novamente [M/F]: ").upper().strip()
print(f"Sexo {sexo} cadastrado com sucesso!") #quando digitar a opção certa, vai sair da repetição.
