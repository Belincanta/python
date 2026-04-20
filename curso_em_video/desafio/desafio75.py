# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

while True:
    numero = (int(input("Digite um número: ")),
            int(input("Digite outro número: ")),
            int(input("Digite mais um número: ")), 
            int(input("Digite o último número: ")))
    print(f"Os números digitados foram {numero}")
    opcao = " "
    while opcao not in "SN":
        opcao = input("Quer mudar os números? S/N: ").strip().upper()[0]
    if opcao == "N":
        break
if 9 in numero:
    print(f"O valor 9 apareceu {numero.count(9)} vezes.")
else:
    print("O número 9 não foi digitado!")
if 3 in numero:
    print(f"O primeiro número 3 apareceu na posição {numero.index(3)+1}º.")
else:
    print("O número 3 não foi digitado! ")
pares = [n for n in numero if n % 2 == 0]
if pares:
    print(f"Os números pares são: {pares}")
else:
    print("Não foram digitados números pares.")
    
