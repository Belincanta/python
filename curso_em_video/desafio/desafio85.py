# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

principal = [[],[]]
numero = 0
for c in range(0,7):
    numero = int(input(f"Digite o {c+1}º numero: "))
    if numero % 2 == 0:
        principal[0].append(numero)
    else:
        principal[1].append(numero)
principal[0].sort()
principal[1].sort()
print(f"Os números pares digitados foram {principal[0]}")
print(f"Os números ímpares digitados foram {principal[1]}")