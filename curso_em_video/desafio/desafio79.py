# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
numeros = list()
while True:
    n = int(input("Digite um número: "))
    if n not in numeros:
        numeros.append(n)
        print("Valor adicionado com sucesso...")
    else:
        print("O número está duplicado, não será adicionado")
    opcao = " "
    while opcao not in "SN":
        opcao = input("Quer continuar? S/N: ").strip().upper()[0]
    if opcao == "N":
        break
numeros.sort()
print(f"Fim do cadastro, os números são {numeros}")
    
