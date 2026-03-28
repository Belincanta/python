# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

soma_idade = 0
maior_idade_homem = 0
nome_homem_maior_idade = 0
mulher = 0
for c in range(1 , 5):
    print(f"{"="*10} {c}º pessoa {"="*10}")
    nome = input("Qual é o seu nome? ")
    idade = int(input("Qual é a sua idade? "))
    sexo = input("Sexo Masculino ou Feminino (M/F): ")
    if idade > 0:
        soma_idade += idade

    if idade > maior_idade_homem and sexo in "Mm": # o uso de in permite que o usuário adicione M ou m.
        maior_idade_homem = idade
        nome_homem_maior_idade = nome        

    if sexo in "Ff" and idade < 20:
        mulher += 1

print("="*20)
print(f"A média das idades é {soma_idade/4:.1f}")
print(f"A maior idade entre os os homens é do {nome_homem_maior_idade} com {maior_idade_homem} anos.")
print(f"Possui {mulher} mulher(es) com menos de 20 anos.")
