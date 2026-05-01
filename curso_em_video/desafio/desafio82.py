# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
lista = []
lista_par = []
lista_impar = []
while True:
    n = int(input("Digite um número: "))
    lista.append(n)
    if n % 2 == 0:
        lista_par.append(n)
    else:
        lista_impar.append(n)
    opcao = " "
    while opcao not in "SN":
        opcao = input("Quer continuar? S/N: ").strip().upper()[0]
    if opcao in "N":
        break
print(f"A lista completa digitada é {lista}")
print(f"A lista com números pares é {lista_par}")
print(f"A lista com números impares é {lista_impar}")